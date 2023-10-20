import re
from flask import Flask, request, jsonify


app = Flask(__name__)

import re

def is_sanitized(input_str):
    # Define a regex pattern to detect special characters
    special_characters_pattern = r'[$&+,:;=?@#|\'<>.\-^*()%!]'

    # Using re.search() to find a match
    if re.search(special_characters_pattern, input_str):
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

