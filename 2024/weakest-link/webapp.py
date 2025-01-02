import time
import hashlib
import secrets
from flask import Flask, abort
from urls import urls

app = Flask(__name__)

WEAKEST = "karika"
FLAG = "b000bb00b135b00b135b00b135b00b135b00b135"  # just random hash-alike string
MAX_DELAY = 200


def sleep(millis):
    time.sleep(millis / 1000)


def process_request(delay, response):
    sleep(delay)
    return app.make_response((response, 200))


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    if path == WEAKEST:
        return process_request(MAX_DELAY * 1.2, FLAG)
    if path in urls:
        return process_request(
            secrets.choice(range(0, MAX_DELAY)),
            hashlib.sha1(path.encode("utf-8")).hexdigest(),
        )
    abort(404)
