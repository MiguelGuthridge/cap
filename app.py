from flask import Flask, request
from pprint import pprint

app = Flask(__name__)

@app.route("/", defaults={"path": ""}, methods=["POST", "GET", "PUT", "DELETE"])
@app.route("/<path:path>", methods=["POST", "GET", "PUT", "DELETE"])
def page(path):
    print("\n\n")
    print("Method:", request.method)
    print("URL:", request.url)
    print("Form:")
    pprint(dict(request.form))
    print("Body:")
    pprint(request.data.decode())
    print("Query:")
    pprint(dict(request.args))
    return """
<html>
<head><title>Hi</title></head>
<body>
  <h1>Hi</h1>
  <p>You're looking nice today</p>
</body>
"""

app.run(port=8625)
