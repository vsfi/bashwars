# Telefonski imenik

SQL join + jq

## Answer

`064/555-35-35`

## Writeup

Since we've got sqlite let's check what do we have there
`sqlite3 Imenik.db`

```
sqlite> .tables
covek  data   mesto
sqlite> .schema data
CREATE TABLE data (id INTEGER PRIMARY KEY, covek INTEGER, mesto INTEGER, data TEXT);
sqlite> .schema covek
CREATE TABLE covek (id INTEGER PRIMARY KEY, ime TEXT, prezime TEXT);
sqlite> .schema mesto
CREATE TABLE mesto (id INTEGER PRIMARY KEY, mesto TEXT);
```

Looks like tables are somehow connected, the only thing to do is to prepare JOIN statement and parse JSON result. The final oneliner is:

```
sqlite3 Imenik.db "select d.data from data as d join covek as c on d.covek=c.id join mesto as m on m.id=d.mesto where c.ime = 'Šaban' and c.prezime = 'Bajramović' and m.mesto like '%Belgrade%'" | jq -r '.personal.telefon'
```
