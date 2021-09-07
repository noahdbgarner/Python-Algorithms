Question 1. Structure and Prep:
   - Please use Pyspark 3.1.2
   - I first open the data in Excel to browse the data I will be working with to find any top level structure and content
     issues. I begin by applying a filter, and sorting the data by each column to get a feel for what I'll be working with.
     Immediately I notice strange things going on with the Age column, and decide it would be best to run sorts and filters
     using pyspark.
   
     - Oddity: First two rows include metadata
     - Solution: Delete and move data to metadata file    

     - Oddity: Age column sort format is bad in Excel, may be interpreted as String
     - Solution: Use Excel to convert number format, or use PySpark to sort

     - Oddity: Commas in Geography column data
     - Solution: Export as CSV puts these into double quotes, and spark knows how to interpret with the
       read as csv function

     - Oddity: Space in the Geography code column title
     - Solution: Specify the header=True in the PySpark
     
     - Oddity: The Geography seems to be the unique identifier at first, but that's deceiving
     - Solution: The identifier is the Geography Code. This means if we want to 
     - look at the totals for a geography, we need to sum the geography column totals
     - Multiple codes to one Geography

   - I then converted the population estimates data to csv, moved to local-data folder to be queried by a pyspark jupyter notebook
   - Cleaning Process:
     - I began by first cleaning and applying types to the data with inferschema and casting
     - I inferred a schema, fixed the age column and casted to integer type, and added a new column for anyone above the age of 90
     - I drop records where the geography data is not present (to be safe)
     - Use regexp_replace to remove the +, and convert the column to integer type
     - I create a new column to keep the meaning of the + in age column
     - I then test the df with SQL selects, filters, and aggregations on the data to test the integrity of the data
     - Firstly, I noticed there are 3 pieces related to Geography: All, Male, and Female
     - First test is to make sure all Males+Female sum to the same as All
     - I do this by selecting Geography, and Sex, and pivoting by Sex

Question 2.1 Which geography contained the smallest total population in each year
   from 2013 - 2016?
  - Ran into an issue where I had 4 separate queries for each year, and I wanted to
    put these 4 queries together... so I chained aggregrates
  - Nuance of doing a subselect after sum aggregation, so will resort to spark sql
  - need to pre-compute the min, then join the min and select the geographic location
  - First I needed to compute the sum population of all geography
  - Then I do a subselect for each of the year columns
  - I changed Isles of Scilly to 100000 in 2013, and it correctly showed City of London as next minimum
  - Do not use geo code for this query
  - I thought of using rank isntead of subselect but this seemed simpler
  

Question 3.1 Which geography had the highest female-to-male ratio in 2013, and what was the ratio? 
  - Use the pivot function with sum to convert row into column and aggregate the data
  - says aggregate across all age groups, so we just need to pivot, and select male and females


Question 3.2 Comparing each geography's female-to-male ratio measurements in 2013 vs 2016, which 
    geography's ratio changed the most? Which changed the least?
  - Need to do a join after grabbing the pivoted data from both tables?
  - Scratch the above, actually do not need to join, we can do multiple sum aggregations
  - So powerful
  
Question 4: Plot a visualization of the 2016 age distribution, split out by sex
  - Testing results by selecting only males from 20 to 70
  - Verifying with outside data on the web because this distribution doesn't look right
  - Look at other age distribution charts to see how my data pairs    
  - This is where I should reference external sources of information for validation


Question 4.2 Anomalies: 
  1. Anomaly:
  2. Anomaly factor: 


Notes:
   1. Interpreting first part particularly as the average from 2013 through 2016
   2. Intepreting the largest change in proportion as 2016 - 2013