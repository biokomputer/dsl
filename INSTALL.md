# Installation Guide

This guide will help you set up the environment for running the speech-to-text web application.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git

## Installation Steps

Run the installation script:
   ```
   chmod +x install.sh
   ./install.sh
   ```

   This script will:
   - Create a virtual environment
   - Install Python dependencies
   - Download the DeepSpeech model
   - Install system dependencies (ffmpeg)

OR:

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate
   ```

2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Start the application:
   ```
   python app.py
   ```
