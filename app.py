from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

saved_destinations = []


@app.route('/save-destination', methods=['POST'])
def save_destination():
    data = request.get_json()
    destination = data.get('destination')

    if destination:
        saved_destinations.append(destination)
        print(f"Destination saved: {destination}")
        return jsonify({"message": "Destination saved successfully"}), 200
    else:
        return jsonify({"error": "No destination provided"}), 400


if __name__ == "__main__":
    app.run(debug=True)
