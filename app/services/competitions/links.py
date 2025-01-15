import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_all_links(lang="tr"):
    link0 = f"https://teknofest.org/{lang}/yarismalar/"
    response0 = requests.get(link0)
    content0 = response0.content
    soup0 = BeautifulSoup(content0, 'html.parser')
    the_list0 = soup0.find('div', class_="tab-content mt-5 mobile-container", id="program")

    items0 = the_list0.find_all('a', class_='btn')

    list_of_links = []
    for i in items0:
        x = "https://teknofest.org" + i.get('href')
        if x not in list_of_links:
            list_of_links.append(x)

    # with open("links.txt", 'w') as f: 
    #     for item in list_of_links:
    #         x = item + "\n"
    #         f.write(x)

    return list_of_links

def get_name_from_link(link):
    x =  (urlparse(link)).path.strip('/').split('/')[-1]
    return x

def get_all_names(lang="tr"):
    links = get_all_links(lang)
    names = []
    for link in links:
        names.append(get_name_from_link(link))
    return names