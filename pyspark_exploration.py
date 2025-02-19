# Required libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, count, desc, expr

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("MovieAnalyticsExploration") \
    .config("spark.jars", "postgresql.jar") \
    .getOrCreate()

# Connect to PostgreSQL
db_url = "jdbc:postgresql://localhost:5432/airflow_db"
db_table = "movie_events"
db_user = "admin"
db_password = "admin"

# Load Data from PostgreSQL into Spark
df = spark.read \
    .format("jdbc") \
    .option("url", db_url) \
    .option("dbtable", db_table) \
    .option("user", db_user) \
    .option("password", db_password) \
    .option("driver", "org.postgresql.Driver") \
    .load()

# To show first few rows
print("\nSample Data from PostgreSQL:")
df.show(10)

# print Data Schema
print("\nData Schema:")
df.printSchema()

df = df.withColumn("event_time", to_timestamp(col("event_time")))

# Count Distinct Actions
print("\nUnique Actions Performed:")
df.select("action").distinct().show()

# Most Popular Movies by Total Interactions
popular_movies = df.groupBy("title").agg(count("*").alias("interactions")) \
    .orderBy(desc("interactions"))

print("\nTop 10 Most Popular Movies:")
popular_movies.show(10)

# Most Common User Actions
action_counts = df.groupBy("action").agg(count("*").alias("count")) \
    .orderBy(desc("count"))

print("\nMost Common User Actions:")
action_counts.show()

# Trending Movies in the Last 24 Hours
df_trending = df.filter(expr("event_time >= current_timestamp() - INTERVAL 1 DAY")) \
    .groupBy("title") \
    .agg(count("*").alias("interactions")) \
    .orderBy(desc("interactions"))

print("\nTrending Movies in the Last 24 Hours:")
df_trending.show(10)

# Saving Trending Movies to PostgreSQL
df_trending.write \
    .format("jdbc") \
    .option("url", db_url) \
    .option("dbtable", "trending_movies") \
    .option("user", db_user) \
    .option("password", db_password) \
    .option("driver", "org.postgresql.Driver") \
    .mode("overwrite") \
    .save()

print("Trending movies saved to PostgreSQL.")

# Exported Trending Movies as CSV for Visualization
df_trending.coalesce(1).write.format("csv") \
    .option("header", "true") \
    .mode("overwrite") \
    .save("output/trending_movies.csv")

print("Trending movies saved as CSV in 'output' folder.")

print("Data exploration and transformation completed successfully.")
