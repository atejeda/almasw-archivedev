# alma.scheduling.online.docker

This dockerfile contains all the needed packages for an ALMASW online scheduling environment. The intention is to provide an environment for development and for smoke and integration tests.

## How to use this image

This image is available in docker hub https://hub.docker.com/r/atejeda/alma.scheduling.online.docker/, you may build it your self (there's a helper makefile for doing that) or download it from the hub.

Start adding your user to the docker group, create the group if not exists, you may need to login again.

```
groupadd docker <username>
usermod -aG docker <username>
```

Create a docker network for the future container:

```
docker network create --subnet=172.168.1.0/24 almanet
```

Bring up the container, it will automatically retrieve the latest image:

```
docker run \
  --hostname almadev --net almanet --ip 172.168.1.10 \
  --privileged \
  -t -i --name almadev \
  -v /some/path/generic.profile:/home/$USER/alma.profile \
  -v /some/path/alma/:/alma \
  -v /some/path/alma/ACS-2017DEC:/alma/ACS-current \
  -v /where/your/code/is/code:/code \
  -v /where/your/maven/is/.m2:/home/$USER/.m2 \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -e DISPLAY=$DISPLAY \
  -e ENV_USER=$USER \
  -e ENV_USER_UID=`id -u` \
  atejeda/alma.scheduling.online.docker:latest /bin/bash
```

There's a suggested `generic.profile` to use, this or any profile needs to be mounted in the container home directory as `alma.profile`, this profile automatically loaded by `/etc/bashrc`, the user may need other commands in this script to load any kind of environment.

It is important to define the `ENV_USER` and `ENV_USER_UID` in order to not mess with permissions, `entrypoint` creates a new user with the same UID as the user starting the container, if `ENV_USER` is not defined, `almadev` will be the default user, but it's critcal to define the `ENV_USER_UID` to work with mounted volumes, e.g.: generated artifacts during build time.

A few helper [dotfiles](https://github.com/atejeda/dotfiles) are retrieved from other repository, this is essentially to work with vim, tmux, etc.., review `entrypoint` and `Dockerfile` for more.

Maven local repository directory `.m2` is optional, this is intended to retrieve `almasw` artifacts from the standard installation (`$ACSROOT/lib`) which may be installed by using this (hint):

```
mvn install:install-file -Dfile=`searchFile lib/myALMASW.jar`/lib/myALMASW.jar \
-DgroupId=almasw -DartifactId=myALMASW -Dversion=local -Dpackaging=jar \
```

The purpose is to share maven artifacts with different environments, e.g.: developing on macos but building the software in the docker container.

The `DISPLAY` configuration, depending on the environment, can work to test GUIs, this strictly depends on the host OS.

## Problems?

Provide a pull request or create a ticket.
