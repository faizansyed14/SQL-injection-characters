from flask import Flask, request, jsonify

app = Flask(__name__)

def is_sanitized(input_str):
    # Check for common SQL injection patterns
    sql_injection_patterns = ["SELECT", "INSERT", "UPDATE", "DELETE", "DROP", ";", "--"]
    
    for pattern in sql_injection_patterns:
        if pattern in input_str:
            return False

    return True


@app.route('/v1/sanitized/input/', methods=['POST'])
def check_sanitization():
    data = request.get_json()
    if data is not None and 'input' in data:
        input_str = data['input']
        sanitized = is_sanitized(input_str)
        result = "sanitized" if sanitized else "unsanitized"
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Invalid JSON payload or missing 'input' field"}), 400
if __name__ == '__main__':
    app.run(debug=True)

