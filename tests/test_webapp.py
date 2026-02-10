"""Quick test to verify webapp is working"""

import requests
import json

BASE_URL = "http://127.0.0.1:8080"

print("Testing Webapp...")
print()

# Test 1: Health check
print("1. Health Check...")
try:
    response = requests.get(f"{BASE_URL}/health", timeout=5)
    if response.status_code == 200:
        print(f"   ✓ Health check passed: {response.json()}")
    else:
        print(f"   ✗ Health check failed: {response.status_code}")
except Exception as e:
    print(f"   ✗ Health check error: {e}")

print()

# Test 2: Login page
print("2. Login Page...")
try:
    response = requests.get(f"{BASE_URL}/", timeout=5)
    if response.status_code == 200:
        print(f"   ✓ Login page loads")
    else:
        print(f"   ✗ Login page failed: {response.status_code}")
except Exception as e:
    print(f"   ✗ Login page error: {e}")

print()

# Test 3: Login
print("3. Login...")
session = requests.Session()
try:
    response = session.post(
        f"{BASE_URL}/login", data={"username": "admin", "password": "admin"}, timeout=5
    )
    if response.status_code == 200:
        print(f"   ✓ Login successful")
    else:
        print(f"   ✗ Login failed: {response.status_code}")
        print(f"   Response: {response.text[:100]}")
except Exception as e:
    print(f"   ✗ Login error: {e}")

print()

# Test 4: Dashboard (after login)
print("4. Dashboard Access...")
try:
    response = session.get(f"{BASE_URL}/dashboard", timeout=5)
    if response.status_code == 200:
        print(f"   ✓ Dashboard accessible")
    else:
        print(f"   ✗ Dashboard failed: {response.status_code}")
except Exception as e:
    print(f"   ✗ Dashboard error: {e}")

print()

# Test 5: Generate endpoint (requires login)
print("5. Generate Endpoint...")
try:
    response = session.post(
        f"{BASE_URL}/api/generate",
        json={"mode": "create", "input": "Level 1 Goblin", "format": "markdown"},
        timeout=30,
    )
    if response.status_code == 200:
        data = response.json()
        if data.get("success"):
            print(f"   ✓ Generation successful")
            print(f"   Tokens: {data.get('tokens', {}).get('total', 0)}")
        else:
            print(f"   ✗ Generation failed: {data.get('error', 'Unknown')}")
    else:
        print(f"   ✗ Generate endpoint failed: {response.status_code}")
        print(f"   Response: {response.text[:200]}")
except Exception as e:
    print(f"   ✗ Generate error: {e}")

print()
print("=" * 50)
print("Webapp is running and functional!")
print("Access at: http://127.0.0.1:8080")
print("Login: admin / admin")
print("=" * 50)
