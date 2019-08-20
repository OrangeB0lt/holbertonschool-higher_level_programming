#!/bin/bash
# sends JSON POST request, displays response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
