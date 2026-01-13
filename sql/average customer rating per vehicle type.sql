SELECT Vehicle_Type, AVG(Customer_Rating) as avg_rating 
FROM ola_july_cleaned 
GROUP BY Vehicle_Type;