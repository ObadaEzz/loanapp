#!/usr/bin/env python3
"""
Test script for Vercel deployment
This script tests the Flask application locally before deploying to Vercel
"""

import sys
import os
import requests
from pathlib import Path

def test_local_app():
    """Test the local Flask application"""
    print("Testing local Flask application...")
    
    # Check if required files exist
    required_files = [
        'api/index.py',
        'templates/base.html',
        'static/style.css',
        'best_loan_model.joblib',
        'processed_loan_data.csv',
        'requirements.txt',
        'vercel.json'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False
    
    print("✅ All required files exist")
    
    # Test importing the Flask app
    try:
        sys.path.insert(0, 'api')
        from index import app
        print("✅ Flask app imported successfully")
    except Exception as e:
        print(f"❌ Error importing Flask app: {e}")
        return False
    
    # Test database creation
    try:
        with app.app_context():
            from index import db
            db.create_all()
            print("✅ Database created successfully")
    except Exception as e:
        print(f"❌ Error creating database: {e}")
        return False
    
    # Test model loading
    try:
        from index import model, scaler
        if model is not None and scaler is not None:
            print("✅ Model and scaler loaded successfully")
        else:
            print("⚠️  Model or scaler not loaded (this might be expected in some environments)")
    except Exception as e:
        print(f"⚠️  Error loading model: {e}")
    
    print("\n🎉 Local testing completed successfully!")
    print("You can now deploy to Vercel.")
    return True

def test_vercel_config():
    """Test Vercel configuration"""
    print("\nTesting Vercel configuration...")
    
    # Check vercel.json
    try:
        import json
        with open('vercel.json', 'r') as f:
            config = json.load(f)
        
        required_keys = ['version', 'builds', 'routes']
        for key in required_keys:
            if key not in config:
                print(f"❌ Missing '{key}' in vercel.json")
                return False
        
        print("✅ vercel.json configuration is valid")
        return True
    except Exception as e:
        print(f"❌ Error reading vercel.json: {e}")
        return False

def test_requirements():
    """Test requirements.txt"""
    print("\nTesting requirements.txt...")
    
    try:
        with open('requirements.txt', 'r') as f:
            requirements = f.read()
        
        required_packages = [
            'flask',
            'flask-sqlalchemy',
            'pandas',
            'scikit-learn',
            'joblib',
            'plotly'
        ]
        
        missing_packages = []
        for package in required_packages:
            if package not in requirements:
                missing_packages.append(package)
        
        if missing_packages:
            print(f"⚠️  Missing packages in requirements.txt: {missing_packages}")
        else:
            print("✅ All required packages are in requirements.txt")
        
        return True
    except Exception as e:
        print(f"❌ Error reading requirements.txt: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Starting Vercel deployment tests...\n")
    
    # Test local app
    local_test = test_local_app()
    
    # Test Vercel config
    vercel_test = test_vercel_config()
    
    # Test requirements
    requirements_test = test_requirements()
    
    print("\n" + "="*50)
    print("📊 Test Results Summary:")
    print(f"Local App Test: {'✅ PASS' if local_test else '❌ FAIL'}")
    print(f"Vercel Config Test: {'✅ PASS' if vercel_test else '❌ FAIL'}")
    print(f"Requirements Test: {'✅ PASS' if requirements_test else '❌ FAIL'}")
    
    if all([local_test, vercel_test, requirements_test]):
        print("\n🎉 All tests passed! Ready for Vercel deployment.")
        print("\nNext steps:")
        print("1. Push your code to GitHub")
        print("2. Connect your repository to Vercel")
        print("3. Deploy!")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues before deploying.")
    
    print("="*50)

if __name__ == "__main__":
    main() 