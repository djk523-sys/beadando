Topolszki Péter DJK523

A feladat egy időjárási napló, amiben lehetőség van a bevitt adatok tárolására és mentésére, dátum szerinti keresésre és a legmagasabb és legalacsonyabb hőmérséklet lekérdezésére.

Tartalmaz egy entry modult, amivel a dátumot, legalacsonyabb és legmagasabb hőmérsékletet adhatjuk meg(WeatherEnty osztályon belül, init, self és str függvényekkel).
Ezen kívül egy log modult ami az entryből(WeatherEntry) bevitt adatokat listázza és adja vissza.(WeaherLog osztállyal, add_entry, list_entry, find_by_date függvényekkel) 
Egy statisztika modult WeatherStatisticsTP osztállyal ami megmutatja a legalacsonyabb és legmagasabb bevitt hőmérséklet értéket.(maximum_temperature és minimum_temperature)
A helpers.py a main.py előhívását segít kiiratni.
Az app.py pedig egy ablakos applikáció, amivel lehetőség van a bevitt értékek mentésére is. 
