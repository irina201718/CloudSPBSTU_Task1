from flask import Flask
app = Flask (__name__)

@app.route("/")
def hello_world():
    return "<p>Hello,World!</p>“
@app.route("/number", methods=['PUT'])
def number():
    return f"<p>result is {request.from['number']}!</p>\n"
@app.route("/command", methods=['POST'])
def command():
    return f<p>Your Command - {request.from['command'].upper()}}</p>\n"

app.run(host=' 0.0.0.0' , port=5000)
