#!/usr/bin/env python

from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender
import json

person = Person(Locale.EN)
persons = {}

for _ in range(0, 3000):
    pers = {
            "email":person.email(),
            "id":person.identifier(),
            "phone":person.phone_number(),
            "full_name":person.full_name(),
            "username":person.username(),
    }
    persons[pers["username"]]=pers

with open('file.json', 'w') as fp:
    json.dump(persons, fp)
