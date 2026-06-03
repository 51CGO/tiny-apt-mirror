import flask
import requests
import tempfile
from markupsafe import escape

DEBIAN_DISTS_URL="https://miroir.univ-lorraine.fr/debian/dists"

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/debian/dists/<path:subpath>")
def dists(subpath):

    print(DEBIAN_DISTS_URL + "/" + subpath)

    r = requests.get(DEBIAN_DISTS_URL + "/" + subpath)
    r.status_code

    fd = tempfile.TemporaryFile()
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
    fd.seek(0)
    return fd.read()

@app.route("/debian/pool/<path:subpath>")
def pool(subpath):
    return escape(subpath)
