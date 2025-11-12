thonimport requests
from bs4 import BeautifulSoup

def parse_zillow_data(identifier):
    """
    Fetches property details from Zillow using address, ZPID, or URL.
    """
    try:
        if identifier.startswith("http"):
            url = identifier
        else:
            url = f"https://www.zillow.com/homes/{identifier}_zpid/"

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        property_details = {
            "address": soup.find("h1", {"class": "ds-address-container"}).get_text(strip=True),
            "zpid": identifier,
            "zestimate": soup.find("div", {"class": "zestimate"}).get_text(strip=True),
            "url": url,
            "propertyType": soup.find("span", {"class": "ds-bed-bath-living-area"}).get_text(strip=True),
        }

        return property_details

    except Exception as e:
        print(f"Error parsing Zillow data: {e}")
        return None