SELECT SUM(Booking_Value) as total_successful_value 
FROM ola_july_cleaned 
WHERE Booking_Status = 'Success';