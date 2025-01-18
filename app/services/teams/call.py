from app.services.teams import scrape 

def scrape_all_links(first_page=1, last_page=200):   
    for i in range(first_page, last_page):
        print(f"Processing page: {i}")
        scrape.scrape_page(i)

if __name__ == "__main__":
    link0 = "https://teknofest.org/tr/competitions/competition_report/"

    scrape.scrape_page(link0)