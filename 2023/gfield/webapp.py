#!/usr/bin/env python3
import datetime
import random
import string
from flask import Flask, request

app = Flask(__name__)
ANSWER = 'Garfield, where are you??'
TODAY = datetime.datetime.now()
EOY = datetime.datetime(day=1, month=1, year=(TODAY.year + 1))


class InvalidDate(Exception):
    pass


def answer(message, code):
    return app.response_class(
        response=message,
        status=code
    )


def check_date(date):
    try:
        parsed = datetime.datetime.strptime(date, "%Y%m%d")
        if parsed > EOY or parsed < TODAY or parsed.strftime('%A') != 'Monday':
            raise InvalidDate
        letter_pos = parsed.isocalendar().week - TODAY.isocalendar().week - 1

        return letter_pos
    except:
        raise InvalidDate


def get_random_letter():
    return random.choice(string.ascii_letters)


def get_answer_letter(idx):
    try:
        return ANSWER[idx]
    except IndexError:
        return ''


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return answer('Invalid URL', 500)


@app.route('/dt=<dt>')
def return_flag_part(dt):
    try:
        return answer(get_answer_letter(check_date(dt)), 200)
    except InvalidDate:
        return answer(get_random_letter(), 400)
