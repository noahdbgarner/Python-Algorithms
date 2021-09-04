from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import IntegerType as Int, BooleanType as Bool
import pandas as pd
import seaborn as sns

spark = SparkSession \
        .builder \
        .master("local[16]") \
        .appName("population_estimates") \
        .getOrCreate()

raw_data_path = "Local-Data/population_estimates_rawdata.csv"

# Ignore records with no Geography and Geography Code, and cache the dataframe in memory for speed
pop_df = spark \
    .read \
    .option("header", "True") \
    .csv(raw_data_path, inferSchema=True, mode="DROPMALFORMED") \
    .dropna(how="any", subset=["Geography", "Geography code"]) \
    .cache()

@F.udf(returnType=Bool())
def is_above_ninety(age_string):
    if age_string >= 90:
        return True
    return False

# Clean the dataframe. Preserve the meaning of + by adding a new boolean column age >= 90
cleaned_pop_df = pop_df \
    .withColumn("Age", F.regexp_replace("Age", "\+", "").cast(Int())) \
    .withColumn("Above 90", is_above_ninety("Age"))

"""
Question 1
# Sum all populations grouped by Geography
total_pop_by_geo = cleaned_pop_df \
    .select("Geography", "2013", "2014", "2015", "2016") \
    .where("Sex in ('All')") \
    .groupBy("Geography") \
    .agg(F.sum("2013").alias("2013"), F.sum("2014").alias("2014"), F.sum("2015").alias("2015"), F.sum("2016").alias("2016")) \

# Select(F.min('2013')).head(1)[0] returns the minimum value, psuedo subquery
total_pop_by_geo \
    .select("Geography", "2013") \
    .where(F.col("2013") == total_pop_by_geo.select(F.min('2013')).head()[0]) \
    .show()

total_pop_by_geo \
    .select("Geography", "2014") \
    .where(F.col("2014") == total_pop_by_geo.select(F.min('2014')).head()[0]) \
    .show()

total_pop_by_geo \
    .select("Geography", "2015") \
    .where(F.col("2015") == total_pop_by_geo.select(F.min('2015')).head()[0]) \
    .show()

total_pop_by_geo \
    .select("Geography", "2016") \
    .where(F.col("2016") == total_pop_by_geo.select(F.min('2016')).head()[0]) \
    .show()
"""

"""
Question 2.1
cleaned_pop_df \
    .select("Geography", "Sex", "2013") \
    .groupBy("Geography") \
    .pivot("Sex") \
    .sum() \
    .withColumn("Ratio", F.col("Female") / F.col("Male")) \
    .select("Geography", "Ratio") \
    .orderBy(F.desc("Ratio")) \
    .limit(1) \
    .show()

Question 2.2
# sum outputs: All_sum(2013)|All_sum(2016)|Female_sum(2013)|Female_sum(2016)|Male_sum(2013)|Male_sum(2016)
pop_ratio_delta_df = cleaned_pop_df \
    .select("Geography", "Sex", "2013", "2016") \
    .groupBy("Geography") \
    .pivot("Sex") \
    .sum("2013", "2016") \
    .withColumn("2013 Ratio", F.col("Female_sum(2013)") / F.col("Male_sum(2013)")) \
    .withColumn("2016 Ratio", F.col("Female_sum(2016)") / F.col("Male_sum(2016)")) \
    .withColumn("2013 vs 2016 Delta", F.abs(F.col("2013 Ratio") - F.col("2016 Ratio"))) \
    
# Most change would be largest ratio delta
pop_ratio_delta_df \
    .select("Geography", "2013 vs 2016 Delta") \
    .orderBy(F.desc("2013 vs 2016 Delta")) \
    .limit(1) \
    .show()

# Least change would be lowest ratio delta
pop_ratio_delta_df \
    .select("Geography", "2013 vs 2016 Delta") \
    .orderBy(F.asc("2013 vs 2016 Delta")) \
    .limit(1) \
    .show()
"""



# Question 3.1: Plot a  visualization of the 2016 age distribution split out by sex
# First we calculate the distribution by Sex, then we use seaborn to plot them side by side on a facetgrid
cleaned_pop_df \
    .select("Age", "Sex", "2016") \
    .where("Sex in ('Male')") \
    .groupBy("Age", "Sex") \
    .agg(F.sum("2016").alias("Total Pop by Age 2016")) \
    .orderBy(F.desc("Age")) \
    .show(91)
# What are the anomalies? Describe the factors that could account for anomalies
