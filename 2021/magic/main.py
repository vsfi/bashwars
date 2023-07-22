#!/usr/bin/env python
# FLASK_APP=main.py FLASK_ENV=development flask run --host=0.0.0.0 --port 5000
import json
import random
import string
import re
import logging

from faker import Faker
from faker.providers import BaseProvider
from flask import Flask, redirect, request
from magic_lists import genders, email_vendors, oper_numbers

fake = Faker()
app = Flask(__name__)


class MagicProvides(BaseProvider):
    def age(self):
        return random.randint(15, 80)

    def gender(self):
        return random.choice(genders)

    def email(self):
        return "%s.%s@%s" % (fake.first_name().lower(), fake.last_name().lower(), random.choice(email_vendors))

    def s_name(self):
        if random.randint(1, 5) != 3:
            return fake.first_name()
        else:
            return "%segor%s" % (fake.first_name().title()[0:3], fake.first_name().lower()[2:-3])

    def s_surname(self):
        if random.randint(1, 5) != 3:
            return fake.first_name()
        else:
            name = "B%s" % (fake.last_name().lower()[1:])
            return name[:5]

    def s_number(self):
        if random.randint(1, 5) > 3:
            return "%s%i" % (fake.country_calling_code().strip(), random.randint(1000000, 9999999))
        else:
            while True:
                number = "+7%s%i" % (random.choice(oper_numbers),
                                     random.randint(1000000, 9999999))
                if re.match(r'\+7(?:927|937)([012345789])\1\1[012345789]{3}8', number):
                    continue
                else:
                    return number


fake.add_provider(MagicProvides)


class User():
    def __init__(self, name, surname, number, address, age, gender, email):
        self.address = address
        self.age = age
        self.email = email
        self.gender = gender
        self.name = name
        self.number = number
        self.surname = surname

    def json(self):
        return self.__dict__


_target = User('Grzegorz', 'Brzęczyszczykiewicz', '+79375559798',
               fake.address(), fake.age(), fake.gender(), fake.email())
_flag = "0PA_CHIRIK!"


def get_database():
    users = [_target.json()]
    for i in range(random.randint(1000, 1200)):
        try:
            user = User(fake.s_name(), fake.s_surname(), fake.s_number(
            ), fake.address(), fake.age(), fake.gender(), fake.email())
            users.append(user.json())
        except Exception as e:

            raise e
    random.shuffle(users)
    return users


def get_JSON_response(obj, r_status=200):
    return app.response_class(
        response=json.dumps(obj),
        status=r_status,
        mimetype='application/json'
    )


def checkHash(client_hash, level):
    fix_padding = client_hash.encode('utf-8') + b'=' * (-len(client_hash) % 4)
    decoded = base64.b64decode(fix_padding).decode('utf-8')
    return ('VSFI' in decoded and 'vsfi' in decoded and level in decoded)


@app.route('/')
def root():
    response = get_JSON_response({"error": "wyd here, boy?"}, 400)
    return response


@app.route('/usrs')
def users():
    try:
        response = get_JSON_response(get_database())
    except Exception as e:

        response = get_JSON_response({"error": str(e)}, 400)
    return response


@app.route('/ya', methods=['GET', 'POST'])
def yasdelal():
    if request.args.get('sde', None) != 'lal':
        response = get_JSON_response(
            {"error": "wyd here, boy?"}, 400)
        return response

    parameter = request.form.get('post_parameter')
    if not parameter:
        response = get_JSON_response(
            {"error": "'post_parameter' not found"}, 400)
        return response

    if _target.number != parameter:
        response = get_JSON_response(
            {"error": "wth is that?"}, 400)
        return response

    response = get_JSON_response({"flag": _flag}, 200)
    return response
