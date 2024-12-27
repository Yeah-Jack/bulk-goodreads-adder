from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import os
import urllib.parse
import time

def save_cookies(driver, path):
    with open(path, 'wb') as file:
        pickle.dump(driver.get_cookies(), file)

def load_cookies(driver, path):
    with open(path, 'rb') as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)

def add_books_to_goodreads(file_path):
    driver = webdriver.Chrome()
    cookies_path = 'goodreads_cookies.pkl'
    
    # First, go to Goodreads domain (required for adding cookies)
    driver.get("https://www.goodreads.com")
    
    # Load cookies if they exist
    if os.path.exists(cookies_path):
        try:
            load_cookies(driver, cookies_path)
            driver.refresh()  # Refresh to apply cookies
        except Exception as e:
            print(f"Error loading cookies: {e}")
    
    # Check if we need to log in (you'll need to do this only once)
    if "Sign up with email" in driver.page_source:
        input("Please log in manually in the browser window and press Enter once done...")
        # Save cookies after manual login
        save_cookies(driver, cookies_path)
    
    # Read the books from the file
    with open(file_path, 'r') as file:
        books = [line.strip() for line in file if line.strip()]
    
    for book in books:
        try:
            # Create the search URL
            search_query = urllib.parse.quote(book)
            url = f"https://www.goodreads.com/search?q={search_query}"
            
            # Navigate to the search page
            driver.get(url)
            
            # Wait for and find the "Want to Read" button
            wait = WebDriverWait(driver, 10)
            button = wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, 'button.wtrToRead'
            )))
            
            # Click the button
            button.click()
            
            print(f"Added '{book}' to Want to Read list")
            
            # Ask user if they want to continue
            response = input(f"Continue to next book? (y/n): ")
            if response.lower() != 'y':
                break
                
        except Exception as e:
            print(f"Error processing '{book}': {str(e)}")
            continue
    
    # Save cookies before quitting
    save_cookies(driver, cookies_path)
    driver.quit()

if __name__ == "__main__":
    file_path = "books.txt"  # Replace with your text file path
    add_books_to_goodreads(file_path)