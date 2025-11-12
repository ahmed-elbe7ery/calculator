from flask import Flask, jsonify, request
import MyCode  # import your existing Python script

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_script():
    # Get input from browser
    data = request.json
    name = data.get("name", "World")

    # Call main() function from MyCode.py
    result = MyCode.main(name)

    # Return the result as JSON
    return jsonify({"message": result})

if __name__ == "__main__":
    # Start the Flask server on port 5000
    app.run(debug=True, port=5000)

