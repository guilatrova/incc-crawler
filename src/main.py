import requests
from bs4 import BeautifulSoup
from incc_crawler import factories


def main():
    page = requests.get("https://calculador.com.br/tabela/indice/INCC")
    soup = BeautifulSoup(page.text, 'html.parser')
    overview, general = soup.find_all('table')

    overview_result = factories.build_overview(overview)
    general_result = factories.build_general(general)


if __name__ == "__main__":
    main()
