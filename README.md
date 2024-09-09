
# python-docker

Meant to be used as template directory for python projects. No need to install Python locally.
What happens if I try to run an app that includes graphics? I should expect that to work, yes?

As it is, this is a Python sandbox that can be useful in learning Python, either as a companion to a course or as a standalone. Maybe call this repo python-docker-sandbox? But this is not the only use of this repo... hmmm, think about it.

Minimum Viable Product - must contain volume to so files added locally end up in the container automatically

1. Will however need to:
   1. Install Docker
   2. Steps differ for Windows vs Mac. Windows recommend setting a Linux partitiomn

## Build the container

```docker-compose up -d```

## Have a look what's in the container if we need to

```docker exec -it python-docker-container sh```

## Killing the container

```docker-compose down```

## Not step by step (done for you in this repo) but how to get into the trunk if you need to

    ## Produce Dr Image from DockerFile

    Go to directory containing Dockerfile then.    
    ```docker build -t my-python-image .```
    Will build an image that can run Python when run as a container.
    Will need to set up a local workdir

Shit - Windows - best solutuion where I don't need to think about it?

Not so much marketable then.