#!/bin/bash

# Stop the script if any command fails
set -e

echo "Generating formatted speech marks..."

# Run the first Python script
echo "Running format_daring.py ..."
python format_daring.py

# Wait for the first script to finish
wait

# Run the second Python script
echo "Running fix_punctuation.py ..."
if [[ "$filename" == *"quiz"* ]]; then
    python quiz_punctuation.py  
else 
    python fix_punctuation.py 
fi

echo "Script execution completed successfully!"
