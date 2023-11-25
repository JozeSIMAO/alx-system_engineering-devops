#!/bin/bash

# Change to the directory containing your Puppet manifest files
cd /path/to/your/puppet/manifests

# Loop through each *.pp file and fix indentation errors
for file in *.pp; do
  echo "Fixing errors in $file..."

  # Fix arrow alignment (expected in column 13)
  sed -i 's/\(.*\)=>\(.*\)/\1 => \2/g' "$file"

  echo "Done."
done

echo "Script completed."
