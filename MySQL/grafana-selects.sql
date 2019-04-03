SELECT
  UNIX_TIMESTAMP(Datum) as time_sec,
  Temperature as value,
  'Temperature' as metric
 FROM SensorTest
WHERE $__timeFilter(Datum)
ORDER BY Datum ASC

SELECT
  UNIX_TIMESTAMP(Datum) as time_sec,
  Temperature as value,
  'Temperature' as metric
 FROM SensorTest
WHERE $__timeFilter(Datum)
ORDER BY Datum ASC