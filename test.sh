#!/bin/bash
# Run the tests
# echo to cli args
echo "Running tests with args: $1"

python -m unittest discover ./tests $1