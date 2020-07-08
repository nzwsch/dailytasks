#!/bin/sh

curl -X POST -H "Content-Type: application/json" \
    -d '{"args":[2,3]}' \
    http://flower:5555/api/task/async-apply/dailytasks.tasks.mul
