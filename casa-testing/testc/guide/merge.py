#!/usr/bin/env python

import sys

#assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import re
import json
import errno

from optparse import OptionParser

from airspeed import *

from testc import guide

__test__ = False
__all__ = ["GuideMerge"]

class GuideMerge:
    # even that is a class, it will used the methods as they were static ones
    # based that this is a proof of concept, this can be improved later

    def __init__(self, script, template, template_helper,  output, uri):
        self.__script = script
        self.__template = template
        self.__template_helper = template_helper
        self.__output_path = output
        self.__guide_uri = uri

    def __read_phrases(self, to_parse):
	""" Read the phrases and generate the data structure to be used
	by the template.

	The phrases is a 2-d array, e.g.: [ [ phrase, lines of code, counter id, normalized phrase ] ]
	to be used by the template render engine (airspeed).
	
	For every line it will evaluate if is a valid "In CASA" and if is a valid phrase as well.
	For every "In CASA" found without a phrase it will stop adding lines to the previous phrase
	founded, if a new phrase is founded it will add the phrase to the phrases[] and will add the
	lines of code of the phrase til a "In CASA" is found either ways if is a phrase or not.
	"""
        phrases = [] # for store the phrase [ [ phrase, code lines, counter, normalized phrase ] ]
        counter = 0 # it will differentiate duplicated phrases

        self.__assert_file(to_parse)

        with open(to_parse, 'r') as script:      
            phrase = None
            base_re = "(((# In CASA)+(:?)){1})+"
            append_line = False

            for line in script:
                is_incasa = re.search("%s.*" % base_re, line)
                is_phrase = re.search("%s.(\w)+" % base_re, line)

                if is_incasa:
                    phrase = None
		
		# it will be never be valid til the first ocurrence
		# of a valid phrase, is for adding the lines of code
		# of a valid phrase til the next is_incasa is True
                if phrase and len(line) and not is_incasa:
                    phrases[-1:][0][1] += line

                if is_incasa and is_phrase:
                    phrase = re.split(base_re, line)[-1:][0].strip()
                    counter_str = "0%s" % counter if counter < 10 else str(counter)
                    phrases.append([phrase, "", counter_str, self.__normalize_phrase(phrase).lower()])
                    counter += 1

        return phrases

    def __generate_code(self, template_data, template_helper):
        template = Template(template_data)
        return template.merge(locals())
    
    # deprecated    
    def __generate_snippets(self, output_path, guide_script_name, phrases):
        counter = 0
        self.__mkdir("%s/%s" % (output_path, guide_script_name))
        for phrase in phrases:
            snippet = "%s/%s/casapy_%s_0%s_%s.py" % (output_path, guide_script_name, guide_script_name, counter, self.__normalize_phrase(phrase[0]))
            self.__write(snippet, phrase[1])
            counter += 1

    def __normalize_phrase(self, phrase, char_replacement = "_"):
        replaces = ["-", "+", "_", " "]
        for replace in replaces:
            phrase = phrase.replace(replace, char_replacement)
        return phrase.lower()

    def __beautifier(self, body):
        lines = body.splitlines()
        size = len(lines)
        beautified = ""

        for i in range(0, size):
            if len(lines[i].strip()) and not len(lines[i - 1].strip()) and i:
                beautified += ("\n%s\n") % lines[i]
            elif len(lines[i].strip()):
                beautified += ("%s\n") % lines[i].rstrip()

        return beautified

    def __read(self, file):
        self.__assert_file(file)
        content = None
        with open(file, 'r') as template:
            content = template.read()
        return content

    def __write(self, file, data):
        with open(file, 'w') as output:
            output.write(data)

    def __assert_file(self, file):
        assert os.access(file, os.F_OK), "%s not exists" % file

    def __get_base_path(self, file):
        pass

    def __get_guide_name(self, guide):
        """From the absolute path, return just only the
        extracted name dir, the guide_name is normalized
        """
        return guide.split("/")[-1:][0].split(".")[0]

    def __mkdir(self, path):
        try:
            os.makedirs(path)
        #this is for python > 2.5
        except OSError as e:
            if e.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: raise e

    def merge(self):
        self.__mkdir(self.__output_path)
        
        template = self.__read(self.__template)
        helper_template = self.__read(self.__template_helper)

        phrases = self.__read_phrases(self.__script)
        guide_script_name = self.__get_guide_name(self.__script) # name already normilized

        template_helper = {}
        template_helper["phrases"] = phrases
        template_helper["guide"] = guide_script_name
        template_helper["uri"] = self.__guide_uri

        merged_raw = self.__generate_code(template, template_helper)
        merged_beautified = self.__beautifier(merged_raw)
        self.__write("%s/regression_%s.py" % (self.__output_path, guide_script_name), merged_beautified)

        helper_merged_raw = self.__generate_code(helper_template, template_helper)
        helper_merged_beautified = self.__beautifier(helper_merged_raw)
        self.__write("%s/guides_helper_%s.py" % (self.__output_path, guide_script_name), helper_merged_beautified)

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option('-c', "--config", dest="config", help="The configuration file to use", default="%s/guides.conf" % os.getcwd())
    parser.add_option("-e", "--extracted", dest="extracted", help="Where the extracted scripts are", default=os.getcwd())
    parser.add_option("-o", "--output", dest="output", help="Where the generated code will be", default=os.getcwd())

    (options, args) = parser.parse_args()

    # iterate over the configuration
    with open(options.config) as json_data:
        json_obj = json.load(json_data)
	config_base = os.path.dirname(options.config)

        for element in json_obj["guides"]:
            if element["enable"]:
                guide_uri = element["uri"].strip()
                extracted_script = "%s/%s" % (options.extracted, element["guide"].strip()) # absolute
                template = "%s/%s" %  (config_base, element["template"].strip()) # relative to the config path
                template_helper =  "%s/%s" % (config_base, element["template_helper"].strip()) # relative to the config path
                output_path = options.output

                print "- %s %s" % (guide_uri, "-" * (77 - len(guide_uri)))
                print "Script   : %s" % extracted_script
                print "Template : %s" % template
                print "Generated: %s" % output_path

                merger = GuideMerge(extracted_script, template, template_helper, output_path, guide_uri)
                merger.merge()
