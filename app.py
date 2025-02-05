from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    if not number:
        return jsonify( {"number": "alphabet", "error": True} ), 400
    try:
        number = int(number)
    except ValueError:
        return jsonify({"number": "alphabet", "error": True}), 400

    number = int(number)
    properties = get_properties(number)
    digit_sum = sum(int(digit) for digit in str(number))
    fun_fact = get_fun_fact(number)

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }

    return jsonify(response), 200

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

def get_properties(num):
    properties = []
    if is_armstrong(num):
        properties.append("armstrong")
    if num % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    return properties

def is_armstrong(num):
    digits = [int(digit) for digit in str(num)]
    return sum(digit**len(digits) for digit in digits) == num

def get_fun_fact(num):
    response = requests.get(f"http://numbersapi.com/{num}/math")
    return response.text if response.status_code == 200 else "No fun fact available"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5173)  # Ensure the app listens on port 5173
