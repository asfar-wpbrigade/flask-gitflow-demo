from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define a simple route
@app.route("/")
def hello_world():
    return "Hello, World! 👋 This is my Flask GitFlow demo. First change in main branch."

# Entry point for running the app directly
if __name__ == "__main__":
    # Run the app on all interfaces, port 5000, with debug enabled
    app.run(host="0.0.0.0", port=5000, debug=True)
