#!/bin/bash
# takes in URL, send a get response and shows response in only 200
curl -sFL "$1"
