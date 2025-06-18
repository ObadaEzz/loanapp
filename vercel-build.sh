#!/bin/bash

# Vercel Build Script for Loan Approval System

echo "Starting Vercel build..."

# Install Python dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p static
mkdir -p templates

# Copy static files if they don't exist
if [ ! -f "static/style.css" ]; then
    echo "Creating static files..."
    # This will be handled by the build process
fi

echo "Build completed successfully!" 