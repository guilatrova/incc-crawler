from typing import Optional, Iterable, Union
from dataclasses import dataclass


@dataclass
class OverviewEntry:
    period: str
    value: float
    accumulated_year: float
    accumulated_last_12_months: float


@dataclass
class YearlyEntry:
    year: int
    jan: Optional[float]
    feb: Optional[float]
    mar: Optional[float]
    apr: Optional[float]
    may: Optional[float]
    jun: Optional[float]
    jul: Optional[float]
    aug: Optional[float]
    sep: Optional[float]
    oct: Optional[float]
    nov: Optional[float]
    dec: Optional[float]
    accumulated_year: float

    def get_month_value(self, idx) -> float:
        value_idx = {
            1: "jan",
            2: "feb",
            3: "mar",
            4: "apr",
            5: "may",
            6: "jun",
            7: "jul",
            8: "aug",
            9: "sep",
            10: "oct",
            11: "nov",
            12: "dec",
        }

        prop = value_idx.get(idx)
        return getattr(self, prop)


@dataclass
class TableResult:
    rows: Iterable[Union[OverviewEntry, YearlyEntry]]
