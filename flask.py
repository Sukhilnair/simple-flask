from flask import Flask

app = Flask(__name__)

@app.route('/hello-world')
def helloworld():
    return 'Hello, World!'

@app.route('/')
def home():
    return "Hi, Try /hello-world in the url"

if __name__ == '__main__':
    app.run(debug=True, port=8080)
