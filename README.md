# Kafka Movie Pipeline Project
This project processes and analyzes real-time movie data using Kafka, PySpark, PostgreSQL, and Tableau for visualization.

## **Project Components**
- **Kafka Producer & Consumer**: Streams movie interactions.
- **PostgreSQL Database**: Stores movie event data.
- **PySpark Processing**: Cleans and aggregates movie interactions.
- **Tableau Visualization**: Creates interactive visual reports.

## **Components & Technology used**
Streaming: Apache Kafka
Processing: PySpark
Storage: PostgreSQL
Orchestration: Apache Airflow
Visualization: Tableau
Scripting: Python, SQL

## **Project Structure**
kafka-movie-pipeline/
│── output/
│   ├── trending_movies.csv        # Processed data for visualization
│   ├── visualizations/
│   │   ├── Tableau_Dashboard.twbx  # Tableau dashboard file
│   │   ├── Screenshot.png          # Visualization screenshot
│── scripts/
│   ├── kafka_producer.py          # Kafka Producer
│   ├── kafka_consumer.py          # Kafka Consumer
│   ├── pyspark_analysis.py        # PySpark processing script
│   ├── pyspark_exploration.py     # Data exploration script
│── postgresql.jar                  # PostgreSQL JDBC Driver
│── .gitignore                      # Git Ignore file
│── README.md                       # Project Documentation

## **Steps to run the project**

->Clone the repository
->Set up a Virtual environment
-> Install the dependencies 
-> Start Apache Kafka
-> Run Kafka Producer & Consumer .py files
-> Process data with PySpark
->Load Data into PostgreSQL
-> Visualize data in Tableau

## **If have any doubts regarding the project?**
Connect with me:
-**Linkedin**: https://www.linkedin.com/in/pravallika-pulipaka-184a12204/