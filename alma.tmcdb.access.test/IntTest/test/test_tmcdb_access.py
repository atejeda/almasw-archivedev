#!/usr/bin/env python

import sys
import time
import logging
import traceback
import unittest

assert sys.version >= '2', "Python 2 or greater is supported"

import Acspy.Clients.SimpleClient

from TmcdbErrType import TmcdbErrorEx, TmcdbNoSuchRowEx

class TestAccessInterface(unittest.TestCase):

    client = None
    component = None

    @classmethod
    def setUpClass(cls):
        cls.client = Acspy.Clients.SimpleClient.PySimpleClient()
        cls.component = cls.client.getComponent(
            'TMCDBAccess', 
            comp_idl_type='IDL:alma/TMCDB/Access:1.0', 
            is_dynamic=True)

    @classmethod
    def tearDownClass(cls):
        cls.client.releaseComponent(cls.component.name)
        cls.component = None
        cls.client.disconnect()
        cls.client = None

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_default_can_address(self):
        self.assertIsNotNone(self.client)
        self.assertIsNotNone(self.component)

        success = self.component.getDefaultCanAddress('CONTROL/DV01', 'IFProc0')
        self.assertIsNotNone(success)

    def test_default_can_address_exception(self):
        self.assertIsNotNone(self.client)
        self.assertIsNotNone(self.component)

        with self.assertRaises(TmcdbNoSuchRowEx):
            self.component.getDefaultCanAddress('Wrong', 'Value')

if __name__ == '__main__':
    unittest.main()
