#!/usr/bin/env python
"""Test script to directly test the generate route"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "webapp"))

from flask import Flask
from routes import bp, generate_stream, generate
import json

app = Flask(__name__)
app.secret_key = "test-secret"
app.register_blueprint(bp)


@app.route("/test-generate", methods=["POST"])
def test_generate():
    with app.test_request_context():
        from flask import request

        # Mock session
        from flask import session

        session["logged_in"] = True
        session["user_id"] = "test"

        # Test data
        data = {
            "mode": "create",
            "input": "Level 1 Goblin, Minion Harrier",
            "simple_validation": True,
            "model": "claude-sonnet-4-5",
        }

        # Call the generate function
        with app.test_request_context(
            environ_base={
                "REQUEST_METHOD": "POST",
                "wsgi.input": None,
                "QUERY_STRING": "",
                "CONTENT_TYPE": "application/json",
                "CONTENT_LENGTH": str(len(json.dumps(data))),
            }
        ):
            # Mock the request
            from flask import request

            request.json = lambda: data

            try:
                result = generate()
                return result
            except Exception as e:
                import traceback

                return f"Error: {str(e)}\n\n{traceback.format_exc()}"


if __name__ == "__main__":
    result = test_generate()
    print(result)
