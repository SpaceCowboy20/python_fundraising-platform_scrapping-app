import requests
from bs4 import BeautifulSoup
import tkinter as tk 

def scrape_kickstarter_project_urls(starting_url):
    urls = []
    response = requests.get(starting_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(response)
    # for link in soup.find_all('a', class_='fund_tile_card_link'):  
    # for link in soup.find_all('a', class_='baseDiscoverableCard'):  
    for link in soup.find_all('a', class_='activeEvent MuiBox-root css-mkokko'):  
        urls.append(link['href'])
    return urls

def extract_description(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # description = soup.find('div', class_='o-campaign-story hrt-mt-3').text
    # description = soup.find('div', class_='routerContentStory-storyBody').text
    description = soup.find('div', class_='routerContentStory-storyBody').text
    return description

def is_sustainable(description):
    sustainability_keywords = [
        'eco-friendly', 'sustainable', 'green', 'recyclable', 'renewable','shipping'
                               ]
    sustainability = [word in description for word in sustainability_keywords]

    return sustainability
def main():
    # starting_url = 'https://www.gofundme.com/en-gb/discover'
    # starting_url = 'https://www.indiegogo.com/explore/all?project_timing=all&sort=trending'
    starting_url = 'https://www.startengine.com/explore'

    project_urls = scrape_kickstarter_project_urls(starting_url)
    sustainable_projects = []

    for url in project_urls:
        description = extract_description(url)
        sus=is_sustainable(description)
        if any(sus):
            sustainable_projects.append(url)
  
    return sustainable_projects

sustainable_project_list2 = main()
sustainable_project_list = list(set(sustainable_project_list2))

def run_code() :
    output_list = sustainable_project_list

    for output in output_list:
        output_text.insert(tk.END, output + "\n")
root= tk.Tk()
root.title("Sustainable Projects")

run_button = tk.Button(root, text="run code",command=run_code)
run_button.pack()

output_text= tk.Text(root, height=10, width=40)
output_text.pack()

root.mainloop()
