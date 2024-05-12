import requests
from bs4 import BeautifulSoup
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from google_drive_downloader import GoogleDriveDownloader as gdd
import os
import subprocess

sources = ['https://www.dawn.com/', 'https://www.bbc.com/']
extracted_links = []
extracted_articles = []
transformed_data = []

def extract_links(source_url):
    reqs = requests.get(source_url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        extracted_links.append(link.get('href'))

def extract_articles(source_url):
    reqs = requests.get(source_url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    articles = soup.find_all('article')
    for article in articles:
        title = article.find('h3').get_text(strip=True)
        description = article.find('p').get_text(strip=True)
        extracted_articles.append({'title': title, 'description': description})

def transform_data():
    global extracted_articles
    for article in extracted_articles:
        transformed_data.append({'title': article['title'].upper(), 'description': article['description'].capitalize()})

def load_data():
    # Save extracted data to a text file
    with open('/path/to/extracted_data.txt', 'w') as file:
        file.write("Extracted Links:\n")
        for link in extracted_links:
            file.write(link + '\n')
        file.write("\nExtracted Articles:\n")
        for article in extracted_articles:
            file.write(f"Title: {article['title']}\nDescription: {article['description']}\n\n")
        file.write("\nTransformed Data:\n")
        for data in transformed_data:
            file.write(f"Title: {data['title']}\nDescription: {data['description']}\n\n")
    
    # Download DVC and initialize the repository
    subprocess.run(['pip', 'install', 'dvc'])
    subprocess.run(['dvc', 'init'])
    
    # Create a directory for data versioning and move the extracted data there
    os.mkdir('data')
    os.rename('/path/to/extracted_data.txt', 'data/extracted_data.txt')
    
    # Version the data using DVC
    subprocess.run(['dvc', 'add', 'data/extracted_data.txt'])
    subprocess.run(['git', 'add', 'data/extracted_data.txt.dvc'])
    subprocess.run(['git', 'commit', '-m', 'Versioning extracted data'])
    subprocess.run(['git', 'push'])

default_args = {
    'owner': 'airflow-demo',
    'start_date': datetime(2024, 5, 12),
}

dag = DAG(
    'mlops-dag',
    default_args=default_args,
    description='A simple MLOps DAG',
    schedule_interval='@daily',  # Define your desired schedule interval
)

extract_links_task = PythonOperator(
    task_id='extract_links_task',
    python_callable=extract_links,
    op_args=[sources[0]],  # Pass the first source URL to the extract_links function
    dag=dag,
)

extract_articles_task = PythonOperator(
    task_id='extract_articles_task',
    python_callable=extract_articles,
    op_args=[sources[1]],  # Pass the second source URL to the extract_articles function
    dag=dag,
)

transform_data_task = PythonOperator(
    task_id='transform_data_task',
    python_callable=transform_data,
    dag=dag,
)

load_data_task = PythonOperator(
    task_id='load_data_task',
    python_callable=load_data,
    dag=dag,
)

extract_links_task >> extract_articles_task >> transform_data_task >> load_data_task  # Define task dependencies