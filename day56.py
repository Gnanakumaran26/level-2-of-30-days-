import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# --------------------------------
# Website to scrape
# --------------------------------
URL = "https://news.ycombinator.com/"

def scrape_data():
    print("🌐 Fetching website data...")
    response = requests.get(URL)

    if response.status_code != 200:
        print("❌ Failed to fetch website")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.select(".titleline a")

    data = []
    for item in titles:
        title = item.text
        link = item["href"]
        data.append((title, link))

    return data


def save_to_excel(data):
    wb = Workbook()
    ws = wb.active
    ws.title = "Scraped Data"

    # Headers
    ws.append(["Title", "Link"])

    for row in data:
        ws.append(row)

    file_name = "day56_scraped_data.xlsx"
    wb.save(file_name)
    print(f"✅ Data saved to {file_name}")


# --------------------------------
# Main Program
# --------------------------------
if __name__ == "__main__":
    scraped_data = scrape_data()
    if scraped_data:
        save_to_excel(scraped_data)
