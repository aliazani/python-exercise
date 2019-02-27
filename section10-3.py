import sqlite3

conn = sqlite3.connect("chinook.db")

res = conn.execute("""
SELECT t.name,  s.name, a.title, g.name, t.milliseconds FROM tracks  AS t
JOIN albums AS a  ON  t.albumid = a.albumid
JOIN artists AS s ON a.artistid = s.artistid
JOIN genres AS g  ON g.genreid = t.genreid
WHERE g.name = 'Jazz' 
ORDER BY t.milliseconds DESC
""")

for r in res:
    print(r)
