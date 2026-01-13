SELECT Customer_ID, COUNT(Booking_ID) as total_rides 
FROM ola_july_cleaned 
GROUP BY Customer_ID 
ORDER BY total_rides DESC 
LIMIT 5;