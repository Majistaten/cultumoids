import requests
from bs4 import BeautifulSoup
from pathlib import Path


def get_page(url:str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def get_image_url(soup:BeautifulSoup, url: str) -> str:
    a_tag = soup.find('a', class_='link3')
    image_url = a_tag['href']

    if not image_url.startswith(('http:', 'https:')):
        image_url = f"{url.rstrip('/')}{image_url}"

    return image_url


def download_image(url: str, path:str) -> str:
    page = get_page(url)
    soup = BeautifulSoup(page, 'html.parser')
    image_url = get_image_url(soup, url)
    image_response = requests.get(image_url)
    image_response.raise_for_status()
    image_name = image_url.split('/')[-1]

    if not Path(path).exists():
        Path(path).mkdir()

    with open(f'{path}/{image_name}', 'wb') as file:
        file.write(image_response.content)

    return image_name


if __name__ == '__main__':
    page_url = 'https://restaurangcultum.se'
    download_image(page_url, './images')
