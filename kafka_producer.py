from kafka import KafkaProducer  #main class to send data to kafka topic
import json  #python dictionaries to json
import time 
import random  

producer= KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer= lambda v:json.dumps(v).encode('utf-8')
)

movies = [
    {"movie_id": 1, "title": "Before Sunrise"},
    {"movie_id": 2, "title": "Fly Towards You"},
    {"movie_id": 3, "title": "Me Before You"},
    {"movie_id": 4, "title": "Dark Matter"},
    {"movie_id": 5, "title": "Intern"},
    {"movie_id": 6, "title": "Princess Diaries"},
    {"movie_id": 7, "title": "About Time"},
    {"movie_id": 8, "title": "The Peanut Butter Falcon"},
    {"movie_id": 9, "title": "Forrest Gump"},
    {"movie_id": 10, "title": "Gladiator"}
]
actions = ["Play", "Pause", "Stop", "Rewind", "Forward", "Like", "Dislike", "Rate"]
print("Sending movie events to Kafka... Press Ctrl+C to stop.")

while True:
    movie= random.choice(movies)
    action= random.choice(actions)

    event= {
        "movie_id": movie["movie_id"],
        "title": movie["title"],
        "action": action
    }
    producer.send('movie-events',value=event)
    print(f"Sent: {event}")

    time.sleep(random.uniform(0.5,3))
producer.flush()