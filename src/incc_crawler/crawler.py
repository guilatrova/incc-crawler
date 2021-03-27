from typing import Tuple
import requests
from bs4 import BeautifulSoup
from incc_crawler import factories, dtos

PAGE_URL = "https://calculador.com.br/tabela/indice/INCC"


def build_results() -> Tuple[dtos.TableResult, dtos.TableResult]:
    page = requests.get(PAGE_URL)
    soup = BeautifulSoup(page.text, "html.parser")

    overview, general = soup.find_all("table")
    overview_result = factories.build_overview(overview)
    general_result = factories.build_general(general)

    return overview_result, general_result
