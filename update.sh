#!/bin/bash

# Function to validate version number
validate_version() {
    if [[ $1 =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        return 0
    else
        return 1
    fi
}

# Ask for version number
while true; do
    read -p "Enter the new version number (in format x.y.z): " version
    if validate_version $version; then
        break
    else
        echo "Invalid version format. Please use the format x.y.z (e.g., 1.0.0)"
    fi
done

# Update CHANGELOG.md
sed -i "s/## \[Unreleased\]/## [Unreleased]\n\n## [$version] - $(date +%Y-%m-%d)/" CHANGELOG.md

# Commit changes
git add CHANGELOG.md
git commit -m "Bump version to $version"

# Create a new tag
git tag -a "v$version" -m "Version $version"

# Push changes and tag to the server
git push origin main
git push origin "v$version"

echo "Version $version has been released and pushed to the server."
