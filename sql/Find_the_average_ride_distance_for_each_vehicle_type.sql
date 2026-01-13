USE ola_analysis;
SHOW TABLES;
SELECT Vehicle_Type, AVG(Ride_Distance) as avg_distance 
FROM ola_july_cleaned 
GROUP BY Vehicle_Type;