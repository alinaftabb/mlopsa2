# MLOps Automation with Apache Airflow

## Overview

This project aims to automate Machine Learning Operations (MLOps) tasks using Apache Airflow. The goal is to create a robust pipeline that handles data extraction, transformation, storage, and version control for machine learning models and datasets.

## Features

1. **Data Extraction**:
   - Utilizes data sources such as news websites (e.g., Dawn and BBC) to extract links, titles, and descriptions from articles.
   - Uses libraries like `requests` and `BeautifulSoup` for web scraping.

2. **Data Transformation**:
   - Preprocesses extracted text data, cleaning and formatting it for further analysis.
   - Implements data preprocessing techniques suitable for NLP tasks.

3. **Data Storage and Version Control**:
   - Stores processed data on Google Drive for easy access and sharing.
   - Implements Data Version Control (DVC) to track changes in datasets and models.
   - Versioning metadata is synchronized with GitHub repository commits.

4. **Apache Airflow DAG Development**:
   - Develops an Airflow DAG to automate the end-to-end MLOps pipeline.
   - Manages task dependencies and error handling within the DAG.
   - Executes tasks such as data extraction, transformation, storage, and version control in a scheduled manner.

## Project Structure

- **`dags/`**: Contains the Apache Airflow DAG file (`mlops_dag.py`) defining the workflow steps.
- **`scripts/`**: Includes Python scripts for data extraction, transformation, and loading.
- **`data/`**: Stores datasets and processed data files.
- **`logs/`**: Logs generated during pipeline execution.

## Usage

1. **Environment Setup**:
   - Install the required Python packages using `pip install -r requirements.txt`.
   - Set up Apache Airflow with necessary configurations.

2. **Run the Airflow DAG**:
   - Place the DAG file (`mlops_dag.py`) in the Airflow DAGs directory.
   - Start the Airflow scheduler and web server.

3. **Monitor Execution**:
   - Access the Airflow UI to monitor DAG execution, task statuses, and logs.

## Dependencies

- Python 3.x
- Apache Airflow
- Libraries: `requests`, `BeautifulSoup`, `google_drive_downloader`, `dvc`

## Contribution

Contributions to enhance functionality, add new features, or fix issues are welcome. Please follow the standard GitHub workflow for pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
