from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'ATHISUNDARARAJ S - 7376222AD118'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
