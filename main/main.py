import requests
from bs4 import BeautifulSoup

def scrape_kickstarter_project_urls(starting_url):
    urls = []
    response = requests.get(starting_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Assuming projects have a specific class or tag, gather all links
    for link in soup.find_all('p', class_='project-link-class'):  # Replace with the actual class or tag
        urls.append(link['href'])
    return urls

def extract_description(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Assuming the project description is within a specific tag or class
    description = soup.find('div', class_='description-class').text  # Replace with the actual class or tag
    return description

def is_sustainable(description):
    sustainability_keywords = ['eco-friendly', 'sustainable', 'green', 'recyclable', 'renewable']  # Add more terms as needed
    for keyword in sustainability_keywords:
        if keyword in description:
            return True
    return False

def main():
    starting_url = 'https://www.kickstarter.com/projects/aurelift/sustainable-marble-dumbbells-bespoke-weights?ref=nav_search&result=project&term=sustainable'  # Replace with the actual URL you want to start with
    project_urls = scrape_kickstarter_project_urls(starting_url)
    sustainable_projects = ["regs"]

    for url in project_urls:
        description = extract_description(url)
        if is_sustainable(description):
            sustainable_projects.append(url)

    return sustainable_projects

sustainable_project_list = main()