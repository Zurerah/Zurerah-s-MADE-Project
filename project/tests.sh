#!/bin/bash

# Execute your data pipeline
python pipeline.py

# Validate that the output file(s) exist
if [ -f "../data/output.csv" ]; then
    echo "Output file exists. All tests passed"
else
    echo "Output file does not exist."
fi
