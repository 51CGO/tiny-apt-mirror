import base64
import flask
import requests
import tempfile
from markupsafe import escape

DEBIAN_DISTS_URL="https://miroir.univ-lorraine.fr/debian/dists"

DICT_ENDPOINTS = {
    "debian": "https://miroir.univ-lorraine.fr/debian",
}

app = flask.Flask(__name__)

@app.route("/<path:full_path>")
def process(full_path):

    print(full_path)

    for endpoint in DICT_ENDPOINTS:

        if full_path.startswith(endpoint):

            base_url = DICT_ENDPOINTS[endpoint]

            print("%s => %s" % (endpoint, base_url))

            url_path = full_path[len(endpoint):]

            print(url_path)

            if url_path.startswith("/dists/") or url_path.startswith("/pool/"):

                items = url_path.split("/")
                file_name = items[-1]
                print(file_name)

                r = requests.get(base_url + url_path, stream=False)
                #print(r.status_code)
                #print(r.headers)

                fd = open(file_name, "wb")
                fd.write(r.content)
                fd.close()

                return flask.send_file( file_name)

    return
