#!/usr/bin/env python3
import random
import string
from flask import Flask

# foxtrot_uniform_charlie_kilo
FLAG_MAP = {
    "somebody/once/told/me/": "f",
    "the/world/is/gonna/roll/me": "o",
    "i/aint/the/sharpest/tool/in/the/shed": "x",
    "she/was/looking/kind/of/dumb": "t",
    "with/her/finger/and/her/thumb": "r",
    "in/the/shape/of/an/l/on/her/forehead": "o",
    "well/the/years/start/comin/and/they/dont/stop/comin": "t",
    "fed/to/the/rules/and/i/hit/the/ground/runnin": "_",
    "didnt/make/sense/not/to/live/for/fun": "u",
    "your/brain/gets/smart/but/your/head/gets/dumb": "n",
    "so/much/to/do/so/much/to/see": "i",
    "so/whats/wrong/with/taking/the/backstreets": "f",
    "youll/never/know/if/you/dont/go": "o",
    "youll/never/shine/if/you/dont/glow": "r",
    "hey/now/youre/an/all/star": "m",
    "get/your/game/on/go/play": "_",
    "hey/now/youre/a/rock/star": "c",
    "get/the/show/on/get/paid": "h",
    "and/all/that/glitters/is/gold": "a",
    "only/shootin/stars/break/the/mold": "r",
    "its/a/cool/place/and/they/say/it/gets/colder": "l",
    "youre/bundled/up/now/wait/til/you/get/older": "i",
    "but/the/meteor/men/beg/to/differ": "e",
    "judging/by/the/hole/in/the/satellite/picture": "_",
    "the/ice/we/skate/is/gettin/pretty/thin": "k",
    "the/waters/gettin/warm/so/you/might/as/well/swim": "i",
    "my/worlds/on/fire/how/bout/yours": "l",
    "thats/the/way/i/like/it/and/ill/never/get/bored": "o",
}


app = Flask(__name__)


def get_random_letter():
    return random.choice(string.ascii_lowercase + "_")


def respond(path):
    # return random value for unknown url
    letter = FLAG_MAP.get(path, get_random_letter())
    # some fake data
    fake_headers = [
        # ("lirycs", get_random_letter()),
        # ("lirics", get_random_letter()),
        # ("lyrycs", get_random_letter()),
        # ("lyrics", get_random_letter()),
        # ("X-lyrics", get_random_letter()),
        # ("X-vsfi", get_random_letter()),
    ]
    resp = app.make_response(("", 204, fake_headers))
    # more fake data
    # resp.set_cookie("lirycs", get_random_letter())
    # resp.set_cookie("lirics", get_random_letter())
    # resp.set_cookie("lyrycs", get_random_letter())
    # and finally the needle
    resp.set_cookie("lyrics", letter)
    return resp


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return respond(path)
