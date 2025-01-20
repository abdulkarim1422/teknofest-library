from app.services.teams import scrape 
import time

def scrape_all_links(first_page=1, last_page=200):
    count = 0
    for i in range(first_page, last_page):
        print(f"Processing page: {i}")
        scrape.scrape_page(i)
        
        # Wait for 300 seconds (5 minutes) after every 10 pages
        count += 1
        if (count) % 10 == 0:
            print("Waiting for 5 minutes...")
            time.sleep(300)


if __name__ == "__main__":
    link0 = "https://teknofest.org/tr/competitions/competition_report/"

    scrape.scrape_page(link0)