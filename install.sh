#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Function to print error messages
error() {
    echo "Error: $1" >&2
    exit 1
}

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    error "Python 3 is not installed. Please install Python 3.7 or higher."
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv || error "Failed to create virtual environment"

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate || error "Failed to activate virtual environment"

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip || error "Failed to upgrade pip"

pip install -U pip setuptools wheel

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt || error "Failed to install Python dependencies"

echo "Installation completed successfully!"
echo "To start the application, run:"
echo "source venv/bin/activate"
echo "python app.py"
