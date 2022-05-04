SELECT b.nombre_aeropuerto, COUNT(b.nombre_aeropuerto) as "Numero de vuelos"
FROM vuelos as a
JOIN aeropuertos as b ON a.id_aeropuerto = b.id_aeropuerto
GROUP BY b.nombre_aeropuerto
ORDER BY "Numero de vuelos" DESC
