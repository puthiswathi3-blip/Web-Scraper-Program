
import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

def check_robots_permission(url):
    """Check whether robots.txt permits scraping."""
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"

    parser = RobotFileParser()
    parser.set_url(robots_url)

    try:
        parser.read()
        return parser.can_fetch("*", url)
    except Exception:
        print("Could not verify robots.txt permission.")
        return False


def scrape_website(url):
    """Extract titles and links from a permitted webpage."""
    if not url.startswith(("http://", "https://")):
        print("Please enter a valid HTTP or HTTPS URL.")
        return []

    if not check_robots_permission(url):
        print("Scraping is not permitted or permission could not be verified.")
        return []

    headers = {
        "User-Agent": "EducationalWebScraper/1.0"
    }

    try:
        # Send an HTTP request to the webpage
        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        dataset = []

        # Extract headings and links
        for heading in soup.find_all(["h1", "h2", "h3"]):
            title = heading.get_text(" ", strip=True)

            if title:
                link_tag = heading.find("a")

                link = ""
                if link_tag and link_tag.get("href"):
                    link = requests.compat.urljoin(
                        url, link_tag["href"]
                    )

                dataset.append({
                    "Heading": title,
                    "Link": link
                })

        return dataset

    except requests.exceptions.RequestException as error:
        print(f"Error fetching webpage: {error}")
        return []


def save_to_csv(dataset, filename="scraped_data.csv"):
    """Save the extracted dataset into a CSV file."""
    if not dataset:
        print("No data found to save.")
        return

    try:
        with open(
            filename, "w", newline="", encoding="utf-8"
        ) as csvfile:
            fieldnames = ["Heading", "Link"]
            writer = csv.DictWriter(
                csvfile, fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(dataset)

        print(f"Data saved successfully to {filename}")

    except OSError as error:
        print(f"Error saving CSV file: {error}")


def main():
    print("===== Web Scraping Program =====")

    url = input("Enter a permitted webpage URL: ").strip()

    # Use a reasonable delay before making the request
    time.sleep(1)

    dataset = scrape_website(url)

    if dataset:
        print("\nExtracted Data:")
        for index, item in enumerate(dataset, start=1):
            print(f"{index}. Heading: {item['Heading']}")
            print(f"   Link: {item['Link']}")

        save_to_csv(dataset)
        print(f"\nTotal headings extracted: {len(dataset)}")
    else:
        print("No data was extracted.")


if __name__ == "__main__":
    main()
