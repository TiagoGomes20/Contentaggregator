import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def gather_social_media_content():
    social_media_urls = [
        'https://www.twitter.com',
        'https://www.facebook.com',
        'https://www.instagram.com'
    ]

    aggregated_content = []

    for url in social_media_urls:
        soup = scrape_website(url)
        
        # Example: Extracting and adding titles from the website
        titles = soup.find_all('h1')  # Modify this to match the specific elements you want
        for title in titles:
            aggregated_content.append(title.text.strip())
        
        # Example: Extracting and adding paragraphs from the website
        paragraphs = soup.find_all('p')  # Modify this to match the specific elements you want
        for paragraph in paragraphs:
            aggregated_content.append(paragraph.text.strip())

    return aggregated_content

def display_content(content):
    for item in content:
        print(item)
        print('-' * 50)

if __name__ == '__main__':
    aggregated_content = gather_social_media_content()
    display_content(aggregated_content)
