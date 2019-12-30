# almasw-aoc-elstack

This is a setup to process almasw xml logs and inject the entries to a
elasticsearch instance, it uses docker-compose to orchestrate and setup the
environment.

It uses a docker named volume to persist the data, this volume is created
if already not exists as `aoc_esdata0`, there's several ways to
backup the data, the named volume will not be destroyed if the environment is
bringed down, be sure to destroy it if don't want to use it any longer.

An internal network to communicate all the container is created and destroyed
during up and down time.

The default ports configured are:
- 5601 for kibana
- 5044 for filebeat
- 9200 for elasticsearch

In the host machine, be sure to update the `vm.max_map_count` like:

```
# root privileges needed
sysctl -w vm.max_map_count=262144
sysctl vm.max_map_count
```

## Useful links

- Install and configure filebeat.yml : https://logit.io/sources/configure/filebeat

## Logstash

There is a logstah configuration for processing ALMA logs for IntTest
parse and rearrange some fields, it tries to use the same fields used
in the original ALMA kibana deployment, this is an example of the generated
entry for elastic search.

```
{
    "SourceObject" => "AcsContainerRunner",
            "Data" => "{content=LOG_CompAct_Init_OK, Name=logName}",
          "source" => "/home/user/test/tmp/ACS_INSTANCE.0/all_logs.xml.233",
      "@timestamp" => 2019-03-12T19:37:03.587Z,
          "Thread" => "main",
            "text" => "AcsContainerRunner#run with arguments -OAIAddr",
         "Process" => "AcsContainerRunner",
        "LogLevel" => "Info",
           "LogId" => "1",
           "build" => "233",
            "File" => "AcsContainerRunner.java",
            "Time" => "2019-03-05T21:43:12.453",
         "Routine" => "run",
        "@version" => "1",
            "Line" => "155",
            "Host" => "user.machine.hostname"
}
```

Some of these fields are not in the xml, hence not parsed.

The json entry flattens out the `Data` sections of the XML. At this point all
of the parsing cases I know of are covered.

## Useful commands

- Manage the environment docker-compose {up|down}
- process a custom filebeat configuration: `filebeat -e -c /etc/filebeat/filebeat.yml`
- remove docker volume: `docker volume rm aoc_esdata0`

## Reinject logs

Reinject logs (ho ho ho, you are alone here my friend), be sure to use a custom
configuration just for one time: `e.g.: sudo filebeat -e -c filebeat.yml`

If the file was processed before, rename the registry to something else:
`mv /var/lib/filebeat/registry /var/lib/filebeat/registry.old`

## IntTest

Log stash will map the log file name to the build id if the log file ends with
the build id, e.g.: `all_logs.xml.233`, so be sure to rename or move the log to
a common folder in which filebeat will gather those and logstash can produce
valuable information and mapping the log entries to tne jenkins build id.

## Filebeat

Few entries are contained in multiline log entries, this filebeat pattern
should be set per machine.

```
multiline.pattern: '^<(Delouse|Debug|Emergency|Error|Header|Info|Notice|Trace|Warning) '
multiline.negate: true
multiline.match: after
```
