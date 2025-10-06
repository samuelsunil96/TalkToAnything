#!/bin/bash

# Bump the version in the .version file
VERSION_FILE=".version"

# Read the current version
CURRENT_VERSION=$(grep -oP '(?<=# Version: )\d+\.\d+\.\d+' "$VERSION_FILE")

# Split the version into an array
IFS='.' read -r -a VERSION_ARRAY <<< "$CURRENT_VERSION"

# Increment the patch version
VERSION_ARRAY[2]=$((VERSION_ARRAY[2] + 1))

# Create the new version string
NEW_VERSION="${VERSION_ARRAY[0]}.${VERSION_ARRAY[1]}.${VERSION_ARRAY[2]}"

# Update the .version file
sed -i "s/# Version: .*/# Version: $NEW_VERSION/" "$VERSION_FILE"

echo "Version bumped to $NEW_VERSION"
