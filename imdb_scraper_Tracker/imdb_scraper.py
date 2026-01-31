from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def scrape_imdb_top_250(headless=True):
    print("🔄 Opening browser...")

    # Chrome options
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Launch WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    print("🌐 Loading IMDb Top 250 page...")
    url = "https://www.imdb.com/chart/top/"
    driver.get(url)
    time.sleep(3)

    print("📊 Collecting data...")
    movies = driver.find_elements(By.XPATH, '//li[contains(@class, "ipc-metadata-list-summary-item")]')

    movie_data = []

    for movie in movies:
        try:
            title = movie.find_element(By.XPATH, './/h3').text
            year = movie.find_element(By.XPATH, './/span[contains(@class,"cli-title-metadata-item")][1]').text
            rating = movie.find_element(By.XPATH, './/span[contains(@class,"ipc-rating-star")]/span[1]').text
            movie_data.append({
                "Title": title,
                "Year": year,
                "IMDb Rating": rating
            })
        except Exception as e:
            print("⚠️ Skipping one entry due to error:", e)
            continue

    driver.quit()

    print("💾 Saving data to 'imdb_top_250.csv'...")
    df = pd.DataFrame(movie_data)
    df.index += 1
    df.to_csv("imdb_top_250.csv", index_label="Rank")

    print("✅ Done! Data saved successfully.")
    print(df.head(10))

if __name__ == "__main__":
    scrape_imdb_top_250(headless=False)  # Change to True for headless mode

