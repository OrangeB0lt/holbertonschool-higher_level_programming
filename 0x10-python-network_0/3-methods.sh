#!/bin/bash
# displays all HTTP methods a server takes
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
