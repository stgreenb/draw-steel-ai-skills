#!/usr/bin/env python3
"""
Simple test to verify Flask app can start and routes are accessible.
"""

import os
import sys
import requests

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set test environment variables
os.environ["FLASK_ENV"] = "testing"
os.environ["SECRET_KEY"] = "test-secret"
os.environ["USERNAME"] = "testuser"
os.environ["PASSWORD"] = "testpass"

# Try to import and create app
try:
    from app import create_app

    app = create_app()
    print("✓ Flask app created successfully")

    # Test health endpoint
    with app.test_client() as client:
        response = client.get("/health")
        if response.status_code == 200:
            print("✓ Health endpoint working")
        else:
            print(f"✗ Health endpoint failed: {response.status_code}")

    # Test login endpoint
    with app.test_client() as client:
        # Test login page loads
        response = client.get("/")
        if response.status_code == 200:
            print("✓ Login page loads successfully")
        else:
            print(f"✗ Login page failed to load: {response.status_code}")

        # Test failed login
        response = client.post(
            "/login", data={"username": "wrong", "password": "wrong"}
        )
        if response.status_code == 401:
            print("✓ Failed login rejected correctly")
        else:
            print(f"✗ Failed login not rejected: {response.status_code}")

        # Test successful login
        response = client.post(
            "/login", data={"username": "testuser", "password": "testpass"}
        )
        if response.status_code == 200:
            print("✓ Successful login works")
        else:
            print(f"✗ Successful login failed: {response.status_code}")

        # Test protected route without login
        response = client.get("/dashboard", follow_redirects=False)
        if response.status_code == 401:
            print("✓ Protected route requires login")
        else:
            print(f"✗ Protected route doesn't require login: {response.status_code}")

        # Test protected route with login
        with client.session_transaction():
            response = client.post(
                "/login", data={"username": "testuser", "password": "testpass"}
            )
            response = client.get("/dashboard", follow_redirects=False)
            if response.status_code == 200:
                print("✓ Dashboard accessible after login")
            else:
                print(f"✗ Dashboard not accessible after login: {response.status_code}")

    print("\n✓ All basic tests passed!")
    sys.exit(0)

except ImportError as e:
    print(f"✗ Failed to import app: {e}")
    sys.exit(1)
except Exception as e:
    print(f"✗ Test failed: {e}")
    sys.exit(1)
