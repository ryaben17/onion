CONTAINER_NAME="tor"
BUILD="ryaben/torc"
PORT=9050

echo [+] Checking tor container status...
if [ ! "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo [!] It seems to be down. Loading tor container...
    docker run \
        --rm \
        --detach \
        --name $CONTAINER_NAME \
        --publish $PORT:$PORT \
        $BUILD
else
    echo [!] Container already running!
fi

echo [+] Requesting the site "$1"

# This line should be enough to crawl whatever we need from the tor network
curl --socks5-hostname localhost:$PORT $1