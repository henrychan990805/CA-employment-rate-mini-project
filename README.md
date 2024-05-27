# Project 3: Data Visualization Track
## California Employment Trends

![Screenshot 2024-05-27 062812](https://github.com/henrychan990805/Project_3/assets/151655013/b4f1e733-e58e-42cb-b8d2-1cfc94279e47)


## Overview
This project provides an interactive web application to explore employment data for different industries and counties in California. The application is built using Flask, SQLAlchemy, and JavaScript libraries including Chart.js and D3.js to visualize the data. Users can view and analyze trends in employment and unemployment rates over time.

## Purpose
The primary purpose of this project is to provide users with a tool to understand employment trends in California, allowing them to make informed decisions based on historical data.

## Instructions

### How to Use the Application

1. ***Toggle Dark Mode:***

   -Use the dark mode toggle at the top to switch between light and dark themes.

   ![Screenshot 2024-05-27 061946](https://github.com/henrychan990805/Project_3/assets/151655013/c75f341f-a051-4008-b531-7dc1761caa01)


2. ***View Employment vs. Unemployment Rates:***
   - Use the date selectors to choose a start and end date.
   - Click "Update Chart" to filter the data and view the employment vs. unemployment rates for the selected period.
  
    ![Screenshot 2024-05-27 062159](https://github.com/henrychan990805/Project_3/assets/151655013/867d9fc9-3bf5-46e2-af55-e7bf0ac608a1)

  
3. ***Analyze Unemployment Rates by Area:***
   - Use the dropdown menu labeled "Area Name" to select a specific area.
   - The bar chart will display the unemployment rates for the selected area over the available months and years.
  
    ![Screenshot 2024-05-27 062422](https://github.com/henrychan990805/Project_3/assets/151655013/15592ad3-31f8-4844-a615-247a901d64c7)


4. ***Explore Industry Employment Growth:***
   - Use the dropdown menu labeled "Industry Title/Type of Employment" to select an industry.
   - The line chart will display the employment growth rate for the selected industry over the years.
  
   ![Screenshot 2024-05-27 063638](https://github.com/henrychan990805/Project_3/assets/151655013/76adea14-380d-4b60-ad2f-713ed1d8017d)


5. ***View JSON Data:***
   - Links at the bottom of the page provide access to the raw JSON data used in the application.
  
    ![Screenshot 2024-05-27 063414](https://github.com/henrychan990805/Project_3/assets/151655013/64af7038-d0c2-4c3a-962e-a05d586ec86d)


### How to Run the Application Locally

### Prerequisites
Before you start, make sure you have the following installed on your local machine:
- [Python](https://www.python.org/downloads/): The programming language required to run the application.
- [pip](https://pip.pypa.io/en/stable/installation/): The Python package installer, used to install and manage Python packages. It's usually included with Python installations.
- [PostgreSQL](https://www.postgresql.org/download/): The database management system used by the application.


### Instructions

1. ***Clone the Repository:***
   Open your terminal and clone the repository using the following command:
   ```sh
   git clone https://github.com/henrychan990805/Project_3.git

2. ***Navigate to the project directory***
3. ***Install Dependencies***
4. ***Set Up the PostgreSQL Database:***

   - Ensure PostgreSQL is running on your local machine.
   - Create a new database.
   - Update the database credentials in the app.py file if necessary.
  
5. ***Reflect the Database Schema and Import Data:***

   - Make sure the database tables are set up correctly and the csv files are imported in the right table.
  
6. ***Run the Application:***

   - Start the Flask application using the following command:
     
     ```sh
     python app.py

7. ***Access the Application:***

   - Open a web browser and navigate to http://localhost:5000 to access the application.
  
## Additional Information

**JavaScript, CSS, and HTML Files:**
The JavaScript, CSS, and HTML files are already included in the repository. You can find them in the following locations:
   - static/js/: Contains the JavaScript files.
   - static/css/: Contains the CSS files.
   - The HTML template (project3.html) is located in the templates/ directory.

## Troubleshooting

- If you encounter issues with database connections, double-check your app.py file to ensure the database URI is correctly formatted.
- Ensure that all dependencies are correctly installed.
- Check for any error messages in the terminal where the Flask application is running and address any issues as needed.

By following these instructions, you should be able to run the application locally and explore the employment data for different industries and counties in California.

## Ethical Considerations
In developing this project, we prioritized ethical considerations to ensure responsible data use. We utilized publicly available datasets from trusted sources, ensuring data integrity and transparency. No personally identifiable information (PII) was collected or stored. Our visualizations were designed to present data clearly and accurately, avoiding any misleading representations. We documented our methodologies thoroughly to allow for reproducibility and verification. These efforts reflect our commitment to ethical standards in data and technology use.

## References
- Data Sources:
  - [Current Employment Statistics (CES)](https://data.ca.gov/dataset/current-employment-statistics-ces-2)
  - [Local Area Unemployment Statistics (LAUS)](https://data.ca.gov/dataset/local-area-unemployment-statistics-laus/resource/b4bc4656-7866-420f-8d87-4eda4c9996ed)

- Code References:
  - [Chart.js Documentation](https://www.chartjs.org/docs/latest/) — Used for understanding and implementing charts.
  - [D3.js Documentation](https://d3js.org/) — Used for understanding and implementing data manipulation techniques, such as d3.json for fetching data.
  - [Stack Overflow](https://stackoverflow.com/) — Utilized for troubleshooting and finding solutions to coding issues.
  - [Google](https://www.google.com/) — Used as a search tool to find relevant references.
  - [ChatGPT](https://www.openai.com/chatgpt) — Used for code assistance and guidance.
  - [BCS](https://bootcampspot.instructure.com/) — watching our cloud recordings, using instructor activity solutions, class activities, and past challenges as references.

> #### Team Members: Brent Beachtel, Alyssa Chand, Henry Chen, Darley Chen, and Karuna Kesavan Kothandath
