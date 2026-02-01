# Imdb_Scraper_Tracker
IMDB_Scraper_Tracker

## 🎬 IMDB Movie Scraper & Rating Analysis System

A Python-based web scraping application that extracts real-time movie data from IMDb, including movie titles, ratings, release year, and popularity metrics. The system automates data collection, stores it in CSV format, and enables easy analysis of movie trends.

## I. Overview

The IMDB Scraper Tracker is designed to collect and analyze movie-related data from IMDb.
Using Selenium automation, the application scrapes dynamically loaded IMDb pages, processes the extracted information using Pandas, and stores structured data for further analysis.
This project demonstrates practical skills in web scraping, automation, and data handling.

## II. Project Modules

This project is divided into 6 major modules:

#### 1. Browser Automation Module

Launches a headless Chrome browser
Opens IMDb pages dynamically
Handles page load and timeout scenarios

#### 2. Data Scraping Module

Extracts movie details such as:
Movie Title
IMDb Rating
Release Year
Genre
Vote Count

#### 3. Data Cleaning Module

Removes unwanted symbols and whitespace
Structures raw scraped text into clean columns

#### 4. Timestamping Module

Adds date and time of data extraction
Supports trend and historical analysis

#### 5. Data Storage Module

Saves movie data into CSV format
Appends new records without overwriting old data

#### 6. Reporting Module

Displays scraped movie data in tabular format
Enables quick inspection and validation

## III. Technologies Used
#### Backend & Core
Python 🐍
Pandas
Selenium
WebDriver Manager

##### Web Scraping
Chrome WebDriver
Headless browser automation

#### Data Storage
CSV file handling

## IV. Features
1️⃣ Automated IMDb Scraping

Extracts real-time movie data from IMDb
Handles JavaScript-rendered pages

2️⃣ Movie Rating Tracking

Collects IMDb ratings and vote counts
Helps analyze popularity trends

3️⃣ Structured Data Storage

Saves data in CSV format
Enables further analysis or visualization

4️⃣ Scalable Design

Can be extended to scrape:
Top 250 Movies
Trending Movies
TV Shows

5️⃣ Reliable Automation

Headless execution for fast scraping
Error handling for dynamic content

## V. How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/IMDB_Scraper_Tracker.git
cd IMDB_Scraper_Tracker

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Program
python imdb_scraper.py

## VI. Output

Displays scraped IMDb movie data in the terminal
Saves data automatically to:
data/imdb_movies.csv

## VII. Testing

Verified scraping accuracy across multiple runs
Tested dynamic content loading
Validated CSV data consistency

## VIII. Future Enhancements

Scrape IMDb Top 250 Movies
Add movie trend visualization using Matplotlib / Seaborn
Deploy as a Streamlit dashboard
Schedule automated scraping
Store data in a database (MySQL / MongoDB)

### 📜 License

This project is licensed under the MIT License — free for academic and personal use.

### 🤝 Contributing

Contributions, issues, and feature requests are welcome.
Feel free to fork the repository and submit a pull request.

### ⭐ Acknowledgements

IMDb for movie data

Selenium & WebDriver Manager

Python open-source community
