from fastapi import FastAPI, HTTPException
from typing import List, Dict
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import nest_asyncio
import uvicorn

# Create the FastAPI app
app = FastAPI()

# Define the endpoint to extract links using a GET request
@app.get("/extract-menus/", response_model=Dict[str, List[Dict[str, str]]])
async def extract_menus(website: str) -> Dict[str, List[Dict[str, str]]]:
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        }
        response = requests.get(website, headers=headers)
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to retrieve the page.")
        
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        extracted_links = []
        unique_urls = set()

        # Find all <a> elements
        links = soup.find_all('a', href=True)

        for link in links:
            try:
                link_url = link.get('href')
                # Handle relative URLs
                full_url = urljoin(website, link_url) if not link_url.startswith(('http://', 'https://')) else link_url

                # Clean up link text and extract only the first line
                link_text = link.get_text(separator=' ', strip=True).split('\n', 1)[0].strip()
                # Replace specific special characters including '-&gt; amp'
                link_text = re.sub('<[^<]+?>', '', link_text).strip()
                link_text = link_text.replace("&amp;", " ").replace("-&gt;", "")

                # Check if link text contains only alphabets and symbols (excluding integers)
                if link_text.strip() and not any(char.isdigit() for char in link_text):
                    if full_url not in unique_urls:
                        extracted_links.append({
                            "Link Text": link_text,
                            "Link URL": full_url
                        })
                        unique_urls.add(full_url)
            except Exception as e:
                print(f"Error processing link: {e}")
        
        # If no links found, raise HTTPException
        if not extracted_links:
            raise HTTPException(status_code=404, detail="No menu links found on the page.")

        return {"menu_info": extracted_links}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Function to run the FastAPI app
def run_app():
    nest_asyncio.apply()
    uvicorn.run(app, host="127.0.0.1", port=8000)

# Run the app
run_app()
