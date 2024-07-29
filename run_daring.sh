#!/bin/bash

# Stop the script if any command fails
set -e

echo "Generating formatted speech marks..."

# Run the first Python script
echo "Running format_daring.py ..."
python python format_daring.py

# Run the second Python script
echo "Running fix_puctuation.py ..."
python python fix_puctuation.py 

echo "Script execution completed successfully!"
