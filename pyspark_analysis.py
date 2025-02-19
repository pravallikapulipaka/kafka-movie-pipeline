from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MovieAnalytics") \
    .config("spark.jars", "postgresql.jar") \
    .getOrCreate()  

db_url = "jdbc:postgresql://localhost:5432/airflow_db"  
db_table = "movie_events"
db_user = "admin"
db_password = "admin"

df = spark.read \
    .format("jdbc") \
    .option("url", db_url) \
    .option("dbtable", db_table) \
    .option("user", db_user) \
    .option("password", db_password) \
    .option("driver", "org.postgresql.Driver") \
    .load()

df.show()
