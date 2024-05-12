# Project Report: Automated Data Pipeline with Apache Airflow, DVC, and Google Drive

## Workflow Overview

This project aimed to automate the end-to-end data pipeline for extracting news data from Dawn.com and BBC.com, transforming it for analysis, storing it securely on Google Drive, and implementing version control using Data Version Control (DVC). The workflow was orchestrated using Apache Airflow, ensuring task dependencies, error handling, and scheduling were managed effectively.

### Workflow Steps:

1. **Data Extraction:**
   - Utilized requests and BeautifulSoup to extract links, titles, and descriptions from the landing pages of Dawn.com and BBC.com.
   - Implemented the `extract` function in PythonOperator to perform the extraction task.

2. **Data Transformation:**
   - Preprocessed the extracted text data to clean and format it for analysis.
   - Implemented the `transform` function in PythonOperator to handle data transformation.

3. **Data Storage and Version Control:**
   - Stored the processed data securely on Google Drive for easy access and collaboration.
   - Implemented Data Version Control (DVC) to track changes in the data and version metadata.
   - Ensured each DVC push recorded accurate versioning against the GitHub repository.

4. **Apache Airflow DAG Development:**
   - Developed a DAG named 'mlops-dag' to automate the extraction, transformation, and loading (ETL) processes.
   - Configured task dependencies to ensure proper sequencing of tasks.
   - Handled errors and retries using Airflow's built-in mechanisms for fault tolerance.
   - Scheduled the DAG to run daily for continuous data processing.

## Challenges Faced

During the implementation of this project, several challenges were encountered:

1. **Module Dependencies:** 
   - Experienced issues with module dependencies, such as the absence of 'google_drive_downloader' module, which led to errors during execution. Resolving dependencies and ensuring all required modules were installed properly was crucial.

2. **File Paths and Unicode Errors:**
   - Encountered Unicode errors and file path issues, particularly when specifying file paths with backslashes on Windows systems. Resolving these errors required proper handling of file paths and Unicode encoding/decoding.

3. **Port Availability:**
   - Faced port availability issues while running containers, especially when multiple services attempted to bind to the same port. Adjusting port configurations and ensuring port availability resolved this issue.

4. **Data Preprocessing Complexity:**
   - Data preprocessing, including text cleaning and formatting, posed challenges due to the variability in text data from news sources. Implementing robust preprocessing techniques was necessary to ensure data quality.

## Future Improvements

Moving forward, several improvements can be made to enhance the functionality and reliability of the data pipeline:

1. **Dependency Management:**
   - Implement a robust dependency management system to handle module dependencies and ensure smooth execution across different environments.

2. **Error Handling Enhancements:**
   - Enhance error handling mechanisms within the Airflow DAG to provide more detailed error messages and improve fault tolerance.

3. **Data Quality Checks:**
   - Integrate data quality checks within the pipeline to validate the integrity and quality of extracted and transformed data before storage.

4. **Automated Testing:**
   - Implement automated testing for each component of the pipeline to ensure consistent performance and reliability.

## Conclusion

This project successfully automated the data pipeline for news data extraction, transformation, storage, and version control using Apache Airflow, DVC, and Google Drive. Despite encountering challenges related to module dependencies, file paths, and data preprocessing, these were overcome through troubleshooting and iterative improvements. The project lays a foundation for scalable and efficient data processing workflows, with opportunities for further enhancements and optimizations in the future.