# Flask SQL Injection Detection API

This is a Flask API that checks if an input string is sanitized or unsanitized for SQL injection. It receives a JSON payload via a POST request and returns a JSON response indicating whether the input is sanitized or not.

## Problem Statement

The API checks for the presence of common SQL injection patterns in the input string. If any of these patterns are found, the input is considered unsanitized, otherwise, it is marked as sanitized.

## Usage

1. Start the Flask application by running `python app.py`.
2. Send a POST request to `http://localhost:5000/input` (or the appropriate URL) with a JSON payload containing the 'input' field. Example:

json
{
    "input": "This is a sample input"
}
