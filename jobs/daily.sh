#!/bin/sh

datearg=$(date "+%Y%m%d")

curl -X POST -H "Content-Type: application/json" \
    -d '{"args":["${datearg}"]}' \
    http://flower:5555/api/task/async-apply/dailytasks.tasks.add
