USAGE
---
This repository creates and exposes a Tor proxy on port `9050`.
The rest of the repository are scripts to request onion addresses from the command line.


1. build the docker image from the Dockerfile in the `deployments` folder.
```
$ cd deployments
$ docker build -t ryaben/tor .
2cca0186f8f88694572c7c9105c4800cf9a...
```
2. Now you can run either option:
    * Run the `speedy.sh` bash script:
    ```
    $ deployments/speedy.sh <onion address>
    ```
    * Run the Python script:
    ```
    $ cd src
    $ python3 main.py <onion address> -t
    ```
