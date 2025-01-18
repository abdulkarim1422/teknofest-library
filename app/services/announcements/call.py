from app.services.announcements.links_service import api_parse_page
from app.services.announcements.page_service import parsing_announcement_page
from app.services.announcements.file_service import download_the_files, sanitize_filename

# list all links
# call a function for every link
# create a fold name {date}_{title}
# download all files to that folder

def main(year=2025, firstpage: int = 1, lastpage: int = 3, lang="tr"):
    url = "https://teknofest.org/tr/content/announcements/"

    for page in range(firstpage, lastpage):
        print(f"Start of page: {page}, {year}")

        announcements_data = api_parse_page(url, year, page)

        for title, date, link in announcements_data:
            announcement_page_url = link

            file_urls  = parsing_announcement_page(announcement_page_url)
            DOWNLOAD_FOLDER = str(str(year) + '/' + date + "_" + sanitize_filename(title))
            download_the_files(file_urls, DOWNLOAD_FOLDER)

        print(f"End of page: {page}, {year}")

if __name__ == "__main__":
    main(2024, 1, 3, "tr")