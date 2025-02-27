import os
import requests
from urllib.parse import urlparse, unquote, urljoin
from bs4 import BeautifulSoup
from app.services import download
from app.services.unify.function import find_original_sentence

def scrape_page(page):
    try:
        link = f"https://teknofest.org/tr/competitions/competition_report/?search=&page={page}"
        response0 = requests.get(link)
        response0.raise_for_status()
        content0 = response0.content
        soup0 = BeautifulSoup(content0, 'html.parser')
        the_table0 = soup0.find('tbody', id="myTable")

        if the_table0:
            for tr in the_table0.find_all('tr'):
                try:
                    comp_name = tr.find('th').find('a').text.strip()
                    comp_name = find_original_sentence(comp_name)
                    team_name = tr.find_all('td')[0].find('a').text.strip()
                    year = tr.find_all('td')[1].text.strip()

                    folder_path = os.path.join(os.getcwd(), "teams", comp_name, year)
                    os.makedirs(folder_path, exist_ok=True)

                    try:
                        report_link = tr.find_all('td')[2].find('a')['href']
                        base_file_name = unquote(os.path.basename(urlparse(report_link).path))
                        prefixed_file_name = f"{team_name}_{base_file_name}"
                        full_file_pah = os.path.join(folder_path, prefixed_file_name)
                        download.download_file(report_link, full_file_pah)
                    except:
                        print(f"report failed for {team_name}")
                    try:
                        team_link_relative = tr.find_all('td')[3].find('a')['href']
                        team_link = urljoin("https://teknofest.org", team_link_relative)
                        full_file_pah = os.path.join(folder_path, f"{team_name}_intro.html")
                        download.download_file(team_link, full_file_pah)
                    except:
                        print(f"team file failed for {team_name}")
                    
                except (AttributeError, IndexError, KeyError) as e:
                    print(f"Skipping a row due to missing data: {e}")
                    continue
        else:
            print("The specified element was not found.")
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching the page: {e}")