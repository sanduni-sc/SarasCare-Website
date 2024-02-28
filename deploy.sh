#!/bin/bash

# Navigate to the project directory
cd $DEPLOYMENT_TARGET

# Create a virtual environment (if needed)
python -m venv env

# Activate the virtual environment
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Restart the application
touch web.config
