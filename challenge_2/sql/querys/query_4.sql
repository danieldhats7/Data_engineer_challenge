SELECT b.nombre_aerolinea, COUNT(b.nombre_aerolinea) as "Numero de vuelos", dia
FROM vuelos as a
JOIN aerolineas as b ON a.id_aerolinea = b.id_aerolinea
GROUP BY b.id_aerolinea, dia
HAVING COUNT(b.nombre_aerolinea) >= 2
ORDER BY "Numero de vuelos" DESC
