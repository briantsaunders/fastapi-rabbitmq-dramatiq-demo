#!/bin/bash

# Start the first process
./entrypoint_api.sh &
  
# Start the second process
./entrypoint_dramatiq.sh &
  
# Wait for any process to exit
wait -n
  
# Exit with status of process that exited first
exit $?

