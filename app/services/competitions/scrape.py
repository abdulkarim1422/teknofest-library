import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote
import os
from app.services import download
from app.services.competitions import links

def scrape_link(link):
    response = requests.get(link)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    the_list = soup.find_all('div', class_="tab-pane tab-pane-navigation")

    if the_list:
        for x in the_list:
            if x:
                for li in x.find_all("li"):
                    file_url = unquote(li.find('a').get('href').strip())
                    folder_name = li.find('a').find('p', class_="m-0 p-0 font-weight-bold").get_text().strip().replace('/', '-')
                    
                    file_name = os.path.basename(urlparse(file_url).path)
                    
                    comp_name = links.get_name_from_link(link)
                    folder_path = os.path.join(os.getcwd(), comp_name, folder_name)
                    os.makedirs(folder_path, exist_ok=True)
                    
                    download.download_file(file_url, os.path.join(folder_path, file_name))
            else:
                print("No x-subElement")
    else:
        print("The specified element was not found.")