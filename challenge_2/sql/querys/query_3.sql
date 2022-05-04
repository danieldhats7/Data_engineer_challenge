SELECT dia, COUNT(*) as "Numero de vuelos"
FROM vuelos
GROUP BY dia
ORDER BY "Numero de vuelos" DESC
