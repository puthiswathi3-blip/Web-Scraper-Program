##### **Web Scraping Program Using Python**



###### **Description**

This project is a simple web scraper developed using Python. It extracts publicly available headings and their associated links from a permitted webpage and saves the collected information into a CSV file.



###### **Objective**

To learn the basics of HTML parsing, HTTP requests, web data extraction, and CSV file handling using Python.

###### 

###### **Technologies Used**

\- Python

\- Requests

\- BeautifulSoup

\- CSV module



###### **Features**

\- Fetches webpage content using HTTP requests.

\- Extracts H1, H2, and H3 headings.

\- Collects associated links when available.

\- Checks robots.txt permissions before scraping.

\- Saves extracted information into a CSV file.

\- Handles request and file errors.



###### **Installation**

Install the required libraries using:

pip install requests beautifulsoup4



###### **How to Run**

1\. Save the program as `web\_scraper.py`.

2\. Open a terminal in the project folder.

3\. Run the following command: python web\_scraper.py

4\. Enter the URL of a permitted webpage.

5\. View the extracted information in the terminal.

6\. Find the generated `scraped\_data.csv` file in the project folder.



###### **Output**

The CSV file contains two columns:



\- Heading: The extracted webpage heading.

\- Link: The associated link, if available.



###### **Learning Outcomes**

\- Understanding HTTP requests.

\- Learning HTML parsing with BeautifulSoup.

\- Extracting structured information from webpages.

\- Writing data into CSV files.

\- Handling errors in Python.



###### **Note**

Only scrape websites that permit automated access. Respect website terms, robots.txt instructions, and reasonable request rates.





