from typing import Optional, Iterable
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


@dataclass
class TableResult:
    rows: Iterable[OverviewEntry]
