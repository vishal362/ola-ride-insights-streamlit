SELECT MAX(Driver_Ratings) as max_rating, MIN(Driver_Ratings) as min_rating 
FROM ola_july_cleaned 
WHERE Vehicle_Type = 'Prime Sedan';