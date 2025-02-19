from kafka import KafkaConsumer
import psycopg2
import json
import time  # Added time to slow down message processing for better visibility

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(
        dbname="airflow_db",
        user="admin",
        password="admin",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    print(" Connected to PostgreSQL!")
except Exception as e:
    print(f"Error connecting to PostgreSQL: {e}")
    exit(1)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS movie_events (
        id SERIAL PRIMARY KEY,
        movie_id INT,
        title TEXT,
        action TEXT,
        event_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()

# Set up Kafka Consumer with debug logs
try:
    consumer = KafkaConsumer(
        'movie-events',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',  # Reads messages from the beginning
        enable_auto_commit=True,
        group_id="movie_group",
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    print("Connected to Kafka! Listening for messages...")
except Exception as e:
    print(f"Error connecting to Kafka: {e}")
    exit(1)

# Reads messages and insert into PostgreSQL
for message in consumer:
    data = message.value  # Extract JSON data
    print(f"🔹 Received from Kafka: {data}")  # Debugging: Confirm message is received

    try:
        cursor.execute(
            "INSERT INTO movie_events (movie_id, title, action) VALUES (%s, %s, %s)",
            (data["movie_id"], data["title"], data["action"])
        )
        conn.commit()
        print(f"Stored in DB: {data}")
    except Exception as e:
        print(f"Error inserting into PostgreSQL: {e}")

    time.sleep(1)  # Adds a delay to ensure messages are processed one at a time

# Close connection (won't reach here unless script is stopped)
cursor.close()
conn.close()