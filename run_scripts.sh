#!/bin/bash

# Stop the script if any command fails
set -e

echo "Generating formatted speech marks..."

# Run the first Python script
echo "Running format_auto_intrepid_valiant.py ..."
python format_auto_intrepid_valiant.py

# Run the second Python script
echo "Running index_rm.py ..."
python index_rm.py

echo "Script execution completed successfully!"
