import json
from flask import Flask, abort, request

app = Flask(__name__)

FLAG = "Yo won! How do Yo do, fellow kids?"
ERROR = "Not really %s, man, not Yo enough :-/\n"
OBJ = {
    "data": {
        "birds": ["tit", "fowl", "penguin", "surfin", "ptica-sinica"],
        "my-habbits": ["chilling", "scoofing", "farting", "watching"],
        "kirill's secret": "not revealed yet",
    },
    "tik-tok": "This is a story about people who like to waste time... waste my time, waste your time, waste their time; but time is against them. Time is everyone's master, including them...",
    "bts": [
        "Nam-joon",
        "Jung-kook",
        "ChinGaChGuk",
        "Gojko Mitić",
        "Jin",
        "Yoon-gi",
        {"from": "left", "to": "right", "scope": "all"},
    ],
}


IMPROVED_OBJ = {
    "yo-data": {
        "birds": ["tit", "fowl", "penguin", "surfin", "ptica-sinica"],
        "my-habbits": ["chilling", "scoofing", "farting", "watching"],
        "kirill's secret": "not revealed yet",
    },
    "yo-tik-tok": "This is a story about people who like to waste time... waste my time, waste your time, waste their time; but time is against them. Time is everyone's master, including them...",
    "yo-bts": [
        "Nam-joon",
        "Jung-kook",
        "ChinGaChGuk",
        "Gojko Mitić",
        "Jin",
        "Yoon-gi",
        {"from": "left", "to": "right", "scope": "all"},
    ],
}


@app.route("/", methods=["GET"])
def http_get():
    return app.response_class(
        response=json.dumps(OBJ, separators=(",", ":")) + "\n",
        status=200,
        mimetype="application/json",
    )


@app.route("/", methods=["POST"])
def http_post():
    try:
        if not request.is_json:
            return app.make_response((ERROR % "JSON", 400))
        if request.get_json() == IMPROVED_OBJ:
            return app.make_response((FLAG + "\n", 200))
        return app.make_response((ERROR % "cool", 400))
    except Exception:
        return app.make_response((ERROR % "nice", 400))


@app.route(
    "/", methods=["DELETE", "PATCH", "PUT", "HEAD", "OPTIONS", "CONNECT", "TRACE"]
)
@app.route("/<path:path>")
def catch_404(path):
    abort(404)
