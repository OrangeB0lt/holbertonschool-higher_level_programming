#!/bin/bash
# sends request , displays status code of response
curl -so "$1"/dev/null -w "%{http_code}" "$1"
