#!/bin/bash

# Check if running as root and if not sudo it
if [[ $EUID -ne 0 ]]; then
  echo "This script requires root privileges. Running with sudo..."
  sudo $0 $@
  exit $?
fi

# Map container names
case $1 in
  "gsad")
    container_name="gvm-containers_gsad_1"
    ;;
  "openvas")
    container_name="gvm-containers_openvas_1"
    ;;
  "gvmd")
    container_name="gvm-containers_gvmd_1"
    ;;
  "redis")
    container_name="gvm-containers_redis_1"
    ;;
  "mosquitto")
    container_name="gvm-containers_mosquitto_1"
    ;;
  "postgres")
    container_name="gvm-containers_gvm-postgres_1"
    ;;
  *)
    echo "Invalid argument. Choose one of: gsad, openvas, gvmd, redis, mosquitto, postgres." # list names
    exit 1
    ;;
esac

# Check if container running
if docker ps -f name=$container_name | grep -q $container_name; then
  # Enter the container
  docker exec -it $container_name /bin/bash
else
  echo "Container '$1' is not running."
fi
