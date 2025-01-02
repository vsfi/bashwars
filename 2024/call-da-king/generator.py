#!/usr/bin/env python
import sqlite3
from contextlib import closing
import json
import secrets

DB_FILENAME = "Imenik.db"
NAME, SURNAME = "Šaban", "Bajramović"
PLACE = "Belgrade – Čukarica"
PHONE = "064/555-35-35"
COMMENTS = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "šta za",
    "ne znam",
    "zašto",
    "kum Dragana",
    "kumić",
    "obučar",
    "majmun",
    "neki čovek",
    "petao",
    "tajna devojka",
]
DATA = {
    "personal": {
        "datum_rodjenja": "16.4.1936",
        "ime_oca": "",
        "jmbg": "",
        "nadimak": "",
        "telefon": PHONE,
    },
    "comment": "kralj romske muzike",
    "internal_id": 31337,
}


def zip_randomly(arr1: list[str], arr2: list[str], num=1000) -> list[str]:
    res = []
    for _ in range(0, num):
        res.append("%s %s" % (secrets.choice(arr1), secrets.choice(arr2)))

    # add solve
    index = secrets.choice(range(0, len(res)))
    res = res[:index] + [" ".join([NAME, SURNAME])] + res[index:]
    # get rid of duplicates
    return list(set(res))


def read_file(filename: str) -> list[str]:
    data = []
    with open(filename, "r") as f:
        data = f.read().splitlines()
    return data


def cleanup_db():
    with open(DB_FILENAME, mode="w"):
        pass


def create_tables():
    sql = [
        "CREATE TABLE covek (id INTEGER PRIMARY KEY, ime TEXT, prezime TEXT)",
        "CREATE TABLE mesto (id INTEGER PRIMARY KEY, mesto TEXT)",
        "CREATE TABLE data (id INTEGER PRIMARY KEY, covek INTEGER, mesto INTEGER, data TEXT)",
    ]
    sql_exec(sql)


def fullfill_persons(arr: list[str]):
    values = []
    for person in arr:
        dat = person.split(" ")
        values.append("(NULL, '%s', '%s')" % (dat[0].strip(), dat[1].strip()))
    sql = "insert into covek values %s" % ",".join(values)
    sql_exec([sql])


def fullfill_places(arr: list[str]):
    values = []
    for place in arr:
        values.append("(NULL, '%s')" % place.strip())
    sql = "insert into mesto values %s" % ",".join(values)
    sql_exec([sql])


def fullfill_data(persons: list[str], places_len: int, num=20000):
    values = []
    for _ in range(0, num):
        values.append(
            "(NULL, %d, %d, '%s')"
            % (
                secrets.choice(range(1, len(persons) + 1)),
                secrets.choice(range(1, places_len)),
                get_json_data(persons),
            )
        )
    sql = "insert into data values %s" % ",".join(list(set(values)))
    sql_exec([sql])


def fullfill_all():
    persons = zip_randomly(read_file("names.txt"), read_file("surnames.txt"), 10000)
    places = read_file("places.txt")
    # create new sqlite
    cleanup_db()
    create_tables()
    fullfill_persons(persons)
    fullfill_places(places)
    fullfill_data(persons, len(places) + 1)
    add_answer()


def sql_exec(sql: list[str]):
    with closing(sqlite3.connect(DB_FILENAME)) as con, con, closing(
        con.cursor()
    ) as cur:
        for r in sql:
            cur.execute(r)


def sql_query(sql: str):
    with closing(sqlite3.connect(DB_FILENAME)) as con, con, closing(
        con.cursor()
    ) as cur:
        cur.execute(sql)
        return cur.fetchone()


def is_the_only_solve():
    sql = """select * from data as d 
                join covek as c on d.covek=c.id
                join mesto as m on m.id=d.mesto
                where 
                    c.ime = '%s'
                    and c.prezime = '%s'
                    and m.mesto like '%s'""" % (
        NAME,
        SURNAME,
        "%Belgrade%",
    )
    with closing(sqlite3.connect(DB_FILENAME)) as con, con, closing(
        con.cursor()
    ) as cur:
        cur.execute(sql)
        res = cur.fetchall()
        return len(res) == 1


def add_answer():
    place_id = sql_query('select * from mesto where mesto == "%s"' % PLACE)[0]
    person_id = sql_query(
        'select * from covek where ime == "%s" and prezime == "%s"' % (NAME, SURNAME)
    )[0]
    data_len = sql_query("select count(*) from data")[0]
    record_id = secrets.choice(range(1, data_len))
    sql = "update data set covek = %d, mesto = %d, data = '%s' where id = %d" % (
        person_id,
        place_id,
        json.dumps(DATA, separators=(",", ":")),
        record_id,
    )
    sql_exec([sql])


def get_phone_number():
    return "06%d/%d-%d-%d" % (
        secrets.choice(range(1, 6)),
        secrets.choice(range(100, 1000)),
        secrets.choice(range(10, 100)),
        secrets.choice(range(10, 100)),
    )


def get_json_data(persons: list[str]):
    data = {
        "personal": {
            "datum_rodjenja": "%d.%d.%d"
            % (
                secrets.choice(range(1, 31)),
                secrets.choice(range(1, 13)),
                secrets.choice(range(1941, 2004)),
            ),
            "ime_oca": secrets.choice(persons).split(" ")[0],
            "jmbg": "",
            "nadimak": "",
            "telefon": get_phone_number(),
        },
        "comment": secrets.choice(COMMENTS),
        "internal_id": secrets.choice(range(65536, 99999)),
    }
    return json.dumps(data, separators=(",", ":"))


if __name__ == "__main__":
    # have to check if it's the only solve or rebootstrap from scratch
    while True:
        fullfill_all()
        if is_the_only_solve():
            break
