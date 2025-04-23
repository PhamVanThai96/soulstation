import asyncio
import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Function to wrap synchronous translation
async def translate_text_async(text, src='en', dest='vi'):
    async with Translator() as translator:
        result = await translator.translate(text, src=src, dest=dest)
        return result

## web fetch html content
def fetch_html(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

# Translate only divs with data-type="problem"
def translate_problem_divs(soup):
    divs = soup.find_all('div', {'data-type': 'problem'})
    results = []

    tasks = []
    for div in divs:
        original = div.get_text(separator=' ', strip=True)
        if original:
            print("\nOrigin: ", original)
            output = asyncio.run(translate_text_async(original))
            print("\nOutput: ", output.text)

    # translated_texts = await asyncio.gather(*tasks)

    # for idx, (div, translated) in enumerate(zip(divs, translated_texts), 1):
    #     results.append((idx, div.get_text(separator=' ', strip=True), translated.text))comment
    # return results

# === Main entry point ===
if __name__ == '__main__':
    print(" --- Start translator ---\n")
    URL = "https://openstax.org/books/college-physics-ap-courses-2e/pages/34-problems-exercises"
    url_content = fetch_html(URL)
    translate_problem_divs(url_content)
