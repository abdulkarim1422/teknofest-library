import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote
import os
from app.services import download
from app.services.scrape.competitions import links_service
from app.services.unify.function import find_original_sentence
from datetime import datetime
from app.services.repo_additional import competition_crud_services

def scrape_link(link, update_database: bool = False, year=None, session_id=None):
    # set session_id if year is specified and session_id is not provided
    if session_id:
        response = requests.get(link, cookies={'sessionid': session_id})
    elif year:
        session_id = get_session_id_for_specific_year(year)
        response = requests.get(link, cookies={'sessionid': session_id})
    else:
        response = requests.get(link)
        year = datetime.now().year
    
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
                    
                    comp_name = links_service.get_name_from_link(link)
                    unified_comp_name = find_original_sentence(comp_name)
                    folder_path = os.path.join(os.getcwd(), unified_comp_name, "reports", folder_name)
                    os.makedirs(folder_path, exist_ok=True)
                    
                    download.download_file(file_url, os.path.join(folder_path, file_name))
            else:
                print("No x-subElement")
    else:
        print("The specified element was not found.")
    
    # update database with competition data
    if update_database:
        image_link = get_competition_image_link(soup)
        comp_description = get_competition_description(soup)
        application_link = get_competition_application_link(soup)

        competition_crud_services.update_or_create_competition(
            link=link,
            image_link=image_link,
            application_link=application_link,
            comp_name=comp_name,
            comp_description=comp_description,
            comp_link=link,
            year=year,
        )

def scrape_all_links(lang="tr", update_database: bool = False, year=None):
    # set session_id if year is specified
    if year:
        session_id = get_session_id_for_specific_year(year)
    else:
        session_id = None

    all_links = links_service.get_all_links(lang)
    for link in all_links:
        scrape_link(link=link, update_database=update_database, year=year, session_id=session_id)



# elements
def get_competition_image_link(soup):
    try:
        image_link = soup.find('div', id='tabsNavigation1').find('p').find('img')['src']
        image_link = unquote(image_link)
        return image_link
    except:
        return None

def get_competition_description(soup):
    try:
        description = soup.find('div', id='tabsNavigation1').text
        return description
    except:
        return None

def get_competition_application_link(soup):
    try:
        application_link = soup.find('div', id='tabsNavigation1').find('a')['href']
        return application_link
    except:
        return None

def get_page_lang(response):
    try:
        content_language = response.headers.get('Content-Language', 'Not Found')
        return content_language
    except:
        return None

# options
def get_session_id_for_specific_year(year):
    try:
        response = requests.get(f"https://teknofest.org/tr/season/{year}")
        print(response.cookies)
        session_id = response.cookies.get('sessionid')
        return session_id
    except:
        return None