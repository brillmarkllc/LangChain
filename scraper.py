from bs4 import BeautifulSoup
import requests
import json

# Define pages to scrape
pages = {
    "main": "https://www.brillmark.com",
    "about_us": "https://www.brillmark.com/about-us/",
    "services": "https://www.brillmark.com/services/",
    "ab_test": "https://www.brillmark.com/hire-ab-test-developer/",
    "shopify": "https://www.brillmark.com/hire-shopify-developer/",
    "wordpress": "https://www.brillmark.com/wordpress-development-services/",
}

# Scrape page content
def scrape_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.get_text(separator="\n", strip=True)
    return content

# Save content to file
def save_content_to_file(pages, file_name="scraped_contents.json"):
    scraped_content = {name: {"url": url, "content": scrape_page(url)} for name, url in pages.items()}
    with open(file_name, "w") as f:
        json.dump(scraped_content, f, indent=4)

if __name__ == "__main__":
    save_content_to_file(pages)
    print(f"Scraped content saved to 'scraped_contents.json'.")
