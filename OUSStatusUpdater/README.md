# OUSStatusUpdater

## Build

Clone the repository and `make all` within the `src/` directory, this need to be done in a cycle6 environment configured to use the production archive.

## Help

```
> ~/workspace/OUSStatusUpdater/src 627 > ./ous-status-updater -h
usage: OUSStatusUpdater
 -f,--file <arg>   The file.csv to use
 -h,--help         Display the help
 -p,--persist      Setting this will the application will persist the
                   changes
 -t,--time         Set endtime to date.now for sessions endtime unset with
                   more than 1 EB
```

## CSV

The csv file produced by the query needs to have the delimitation set to none and headers set to true, done through sqldeveloper.

## Dry run

By default the tool will not persist the changes, `-p` will write the changes.