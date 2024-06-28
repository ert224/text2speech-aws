#!/bin/bash

# Stop the script if any command fails
set -e

echo "Generating formatted speech marks..."

# Run the first Python script
echo "Running format.py..."
python format.py

# Run the second Python script
echo "Running switch_times.py..."
python switch_times.py

echo "Script execution completed successfully!"
