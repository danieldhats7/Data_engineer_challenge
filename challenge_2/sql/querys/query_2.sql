SELECT b.nombre_aerolinea, COUNT(b.nombre_aerolinea) as "Numero de vuelos"
FROM vuelos as a
JOIN aerolineas as b ON a.id_aerolinea = b.id_aerolinea
GROUP BY b.id_aerolinea
ORDER BY "Numero de vuelos" DESC
