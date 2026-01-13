#Question 1: Successful Bookings
SELECT * FROM ola_july_cleaned 
WHERE Booking_Status = 'Success';

#Question 2: Average distance for every vehicle type:
SELECT Vehicle_Type, AVG(Ride_Distance) as avg_distance 
FROM ola_july_cleaned 
GROUP BY Vehicle_Type;

#Question 3: rides canceled by customer
SELECT COUNT(*) FROM ola_july_cleaned 
WHERE Booking_Status = 'Canceled by Customer';

#Question 4: Top 5 customers with highest bookings
SELECT Customer_ID, COUNT(Booking_ID) as total_rides 
FROM ola_july_cleaned 
GROUP BY Customer_ID 
ORDER BY total_rides DESC 
LIMIT 5;

#Question 5: rides canceled by drivers
SELECT COUNT(*) FROM ola_july_cleaned 
WHERE Canceled_Rides_by_Driver = 'Personal & Car related issue';

#Question 6: Max aur Min Driver Ratings for Prime Sedan
SELECT MAX(Driver_Ratings) as max_rating, MIN(Driver_Ratings) as min_rating 
FROM ola_july_cleaned 
WHERE Vehicle_Type = 'Prime Sedan';

#Question 7: Payments from UPI
SELECT * FROM ola_july_cleaned 
WHERE Payment_Method = 'UPI';

#Question 8: Average Customer Rating form according to vehicle type
SELECT Vehicle_Type, AVG(Customer_Rating) as avg_rating 
FROM ola_july_cleaned 
GROUP BY Vehicle_Type;

#Question 9: Booking value of successfull rides
SELECT SUM(Booking_Value) as total_successful_value 
FROM ola_july_cleaned 
WHERE Booking_Status = 'Success';

#Question 10: Incomplete rides with reason
SELECT Booking_ID, Incomplete_Rides_Reason 
FROM ola_july_cleaned 
WHERE Incomplete_Rides = 'Yes';