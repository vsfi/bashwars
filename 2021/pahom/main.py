#!/usr/bin/env python
import json
import base64
import random
import string


from flask import Flask, redirect, request

app = Flask(__name__)

LEVELS = [
    'myFirstLevel',
    'mySecondLevel',
    'TrippleAwesomePchitz',
    'wobWobDaSoundOf'
]
COOKIE_PREFIX='bashwars-cookie-'
FAIL_MESSAGE = {"error":"Sorry, your princess is in another castle"}
UA_ERROR_MESSAGE = {"error":"OK, I see, it's curl. You must be a real browser, cheater!"}
COOKIE_ERROR_MESSAGE = {"error":"Where are your cookies, son?"}
FLAG = {"flag":"VSFI_Ye4h_baby_y0uv3_found_1T"}
FLAG_DICT = {
    "glossary-biba": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    },
    "glossary-boba": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    },
    "nextUrl": None,
    "glossary-pupa": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    },
    "glossary-lupa": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}

def getJSONResponse(obj, r_status=200):
    return app.response_class(
                response=json.dumps(obj),
                status=r_status,
                mimetype='application/json'
            )

def getRnd():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

def getHash(level):
    return base64.b64encode((u'%s%sVSFI%svsfi%s' % (getRnd(), level, getRnd(), getRnd())).encode('utf-8')).decode('utf-8').rstrip('=')

def checkHash(client_hash, level):
    fix_padding = client_hash.encode('utf-8') + b'=' * (-len(client_hash) % 4)
    decoded = base64.b64decode(fix_padding).decode('utf-8')
    return ('VSFI' in decoded and 'vsfi' in decoded and level in decoded)

def checkCookieOrURL(client_cookies):
    try:
        if len(client_cookies) == 0:
            return False
        for c in client_cookies:
            if not checkHash(c[0], c[1]):
                return False
    except:
        return False
    return True

def filterCookies(cookies):
    result = []
    for f in cookies.lists():
        if COOKIE_PREFIX in f[0]:
            # don't ask me about that, that's just a piece of shit
            levels_index = int(f[0][-1])
            cookie_value = f[1][0]
            result.append((cookie_value, LEVELS[levels_index]))
    if len(result) == 0:
        # lets just raise an exception on empty cookies
        return None
    return result

def checkUA(req):
    return (not 'curl' in request.headers.get('User-Agent'))

@app.route('/')
def root():
    try:
        if not checkUA(request):
            return getJSONResponse(UA_ERROR_MESSAGE, 406)
        response = app.make_response(redirect('/' + getHash(LEVELS[0])))
        response.set_cookie(COOKIE_PREFIX + '0', getHash(LEVELS[0]))
    except Exception as e:
        response = getJSONResponse(FAIL_MESSAGE, 400)
    return response

@app.route('/<level2>')
def second(level2):
    try:
        if not checkUA(request):
            raise Exception
        conditions = [
            (level2, LEVELS[0])
        ] + filterCookies(request.cookies)
        if checkCookieOrURL(conditions):
            response = app.make_response(redirect('/%s/%s' % (level2, getHash(LEVELS[1]))))
            response.set_cookie(COOKIE_PREFIX + '1', getHash(LEVELS[1]))
        else:
            raise Exception
    except Exception as e:
        print(e)
        response = getJSONResponse(FAIL_MESSAGE, 400)
    return response

@app.route('/<level2>/<level3>')
def third(level2, level3):
    try:
        if not checkUA(request):
            return getJSONResponse(UA_ERROR_MESSAGE, 406)
        conditions = [
            (level2, LEVELS[0]),
            (level3, LEVELS[1])
        ] + filterCookies(request.cookies)
        if checkCookieOrURL(conditions):
            response = app.make_response(redirect('/%s/%s/%s' % (level2, level3, getHash(LEVELS[2]))))
            response.set_cookie(COOKIE_PREFIX + '2', getHash(LEVELS[2]))
        else:
            raise Exception
    except Exception as e:
        print(e)
        response = getJSONResponse(FAIL_MESSAGE, 400)
    return response

@app.route('/<level2>/<level3>/<level4>')
def fourth(level2, level3, level4):
    try:
        if not checkUA(request):
            return getJSONResponse(UA_ERROR_MESSAGE, 406)
        conditions = [
            (level2, LEVELS[0]),
            (level3, LEVELS[1]),
            (level4, LEVELS[2])
        ] + filterCookies(request.cookies)
        if checkCookieOrURL(conditions):
            FLAG_DICT['nextUrl'] = request.url_root + "flag/"
            response = getJSONResponse(FLAG_DICT)
        else:
            raise Exception
    except Exception as e:
        response = getJSONResponse(FAIL_MESSAGE, 400)
    return response

@app.route('/flag/')
def flag():
    conditions = filterCookies(request.cookies)
    if checkCookieOrURL(conditions):
        return getJSONResponse(FLAG)
    return getJSONResponse(COOKIE_ERROR_MESSAGE, 400)