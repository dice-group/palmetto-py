#!/bin/bash

python3 endpointtest.py
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ];then
   echo "Palmetto endpoint is working fine!"
else
  echo "Palmetto endpoint is down! restarting"
  docker restart $(docker ps | grep palmetto | cut -d' ' -f 1)
fi
