# imdb-dead-actors-scraper
This script scrapes informations about dead actors from imdb. Actors or actresses that born in Mexico. 

# IMDb and Wikipedia Scraping Scripts
This repository contains two scripts for scraping data from IMDb and Wikipedia, focusing on Mexican actors. The scripts are intended to gather birth and death information from IMDb profiles and extract actor links from Wikipedia searches.

# 1. IMDb Scraping urls Script (imdb_urls.py)
# Description
This Python script uses undetected_chromedriver,and seleniumto scrape data from IMDb. It retrieves names,and IMDb URLs for Mexican actors listed on IMDb.

# Features
Automated Pagination: Automatically clicks the "Load more" button to load additional actor profiles.
Data Extraction: Scrapes IMDb profiles for birth and death details.
Error Handling: Logs any errors encountered during scraping in a separate errors_imdb.txt file.
Data Storage: Saves extracted data to a text file (imdb_mexico_deaths.txt) and allows exporting results to an Excel file.

The script will navigate to the specified IMDb page, load all profiles, and scrape the relevant data.

# Output
IMDb URLs and Names: Stored in imdb_mexico_deaths.txt.

# 1.2. Scraping more info about each actor individualy (imdb_actor_deaths.ipynb)

This script using requests and Bs4 and iterates the urls that found from the previous task and finds more informations about each actor such as Date of Birth, Location of Birth, Cause of Death, Date of Death.

# Output
An excel file with all the combined informations from the first task and this one.

# Additional

# 2. Wikipedia Scraping Script (wikipedia_scraper.ipynb)
# Description
This Jupyter Notebook script uses requests and BeautifulSoup to scrape Wikipedia search results for Mexican actors. It retrieves URLs and names of actors based on the search term "actor mexicano."

# Features
Batch Processing: Iterates over search results with pagination, fetching up to 10,000 results.
Data Extraction: Collects URLs and actor names from Wikipedia search results.
Data Storage: Saves the extracted URLs and names to a text file (wikipedia.txt).

Run the Notebook: Execute the cells in the Jupyter Notebook to start the scraping process. The script will automatically handle pagination and save results.

# Process Extracted Data:
The script saves the extracted Wikipedia URLs and names to wikipedia.txt for further processing or analysis.
Output
Wikipedia URLs and Names: Stored in wikipedia.txt.
Notes
Rate Limiting: Both scripts include delays (time.sleep()) to prevent overwhelming the target servers. Adjust these delays based on your scraping needs and ethical considerations.
Error Handling: Any URLs that cause errors during scraping are logged in errors_imdb.txt for later review.

# Requirements
- undetected_chromedriver
- selenium
- BeautifulSoup
- requests
- tqdm
- pandas
- xlsxwriter (for exporting to Excel)
