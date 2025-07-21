from flask import Flask, request, jsonify

# This creates your robot's "server"
app = Flask(__name__)

# This is the route that listens for incoming POST requests
@app.route("/api/", methods=["POST"])
def handle_request():
    # Get the file that was uploaded with the request
    file = request.files.get("file")
    
    # If there's no file, return an error
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    # Read the content of the file
    text = file.read().decode("utf-8")

    # Print the question (for your own debugging)
    print("Received question:")
    print(text)

    # Right now, we return fake/dummy answers
    answers = [
        1,                      # Fake answer 1
        "Titanic",             # Fake answer 2
        0.485782,              # Fake correlation value
        "data:image/png;base64,fakeimage=="  # Fake plot image
    ]

    # Send back the answers as a JSON list
    return jsonify(answers)

# Run the server when you type: python app.py
if __name__ == "__main__":
    app.run(debug=True)

