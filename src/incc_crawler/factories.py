from typing import Generator, Iterable
from . import dtos


def parse_cells(cells):
    for cell in cells:
        content = cell.text.strip()

        if content == "-":
            yield None
        else:
            stripped = content.replace(",", ".")
            try:
                if stripped.isdigit():
                    yield int(stripped)
                else:
                    yield float(stripped)
            except ValueError:
                yield stripped


def build_overview(payload) -> dtos.TableResult:
    rows = list(build_overview_rows(payload))
    return dtos.TableResult(rows)


def build_general(payload) -> dtos.TableResult:
    rows = list(build_general_rows(payload))
    return dtos.TableResult(rows)


def build_overview_rows(payload) -> Iterable[dtos.OverviewEntry]:
    rows = payload.find('tbody').find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        values = parse_cells(cells)

        yield dtos.OverviewEntry(*values)


def build_general_rows(payload) -> Iterable[dtos.YearlyEntry]:
    rows = payload.find('tbody').find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        values = list(parse_cells(cells))

        yield dtos.YearlyEntry(*values)
