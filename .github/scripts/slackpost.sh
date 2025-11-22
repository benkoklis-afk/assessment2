#!/bin/bash

curl -X POST \
    -H "Content-Type: application/json" \
    -d '{ "text":"'"$SLACK_MESSAGE"'" }' \
    '"$SLACK_WEBHOOK"'
