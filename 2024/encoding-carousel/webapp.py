from flask import Flask, abort

app = Flask(__name__)

ENDPOINTS = {
    "initial": {"next": "/doggo", "encoding": "cp424"},
    "doggo": {"next": "/hedgehog", "encoding": "cp037"},
    "hedgehog": {"next": "/beaver", "encoding": "utf_32"},
    "beaver": {"next": "/wasphive", "encoding": "utf_16"},
    "wasphive": {"next": "/otter", "encoding": "koi8_r"},
    "otter": {"next": "bw2024_nice_script_u_made", "encoding": "cp1026"},
}


def response(endpoint_data):
    body, encoding = endpoint_data.get("next"), endpoint_data.get("encoding")
    return app.make_response(
        (
            body.encode(encoding),
            200,
            [
                ("Content-Type", "text/plain"),
                (
                    "Content-Encoding",
                    encoding.replace("_", "-"),
                ),
            ],
        )
    )


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    endpoint_data = ENDPOINTS.get(path, None)
    if endpoint_data:
        return response(endpoint_data)
    abort(404)
