from incc_crawler import dtos
from incc_crawler.crawler import PAGE_URL

from abc import ABC, abstractmethod

class BaseBuilder(ABC):
    _next_handler: "BaseBuilder" = None

    def then(self, handler: "BaseBuilder") -> "BaseBuilder":
        self._next_handler = handler
        return self._next_handler

    def build(self, overview: dtos.TableResult, complete: dtos.TableResult, msg: str) -> str:
        msg = self._build(overview, complete, msg)

        if self._next_handler:
            return self._next_handler.build(overview, complete, msg)

        return msg

    @abstractmethod
    def _build(self, overview: dtos.TableResult, complete: dtos.TableResult, msg: str) -> str:
        pass


class HeadlineBuilder(BaseBuilder):
    def _build(self, overview: dtos.TableResult, complete: dtos.TableResult, msg: str) -> str:
        last_period: dtos.OverviewEntry = overview.rows[0]
        return msg + f"Período de *{last_period.period}*\n"


class CurPeriodBuilder(BaseBuilder):
    def _build(self, overview: dtos.TableResult, complete: dtos.TableResult, msg: str) -> str:
        last_period: dtos.OverviewEntry = overview.rows[0]

        return (
            f"{msg}"
            f"INCC de: *{last_period.value}%* / "
            f"acumulado no ano: *{last_period.accumulated_year}%*\n"
        )

class PrevPeriodDiffBuilder(BaseBuilder):
    def _build(self, overview: dtos.TableResult, complete: dtos.TableResult, msg: str) -> str:
        if len(overview.rows) < 2:
            return msg

        last_period: dtos.OverviewEntry = overview.rows[0]
        period_before: dtos.OverviewEntry = overview.rows[1]
        diff = self.calc_diff(last_period, period_before)
        sign = "📉" if diff > 0 else "📈"

        return (
            f"{msg}"
            f"Diferença: *{sign}{diff:.{1}f}%* / Mês anterior: {period_before.value}%\n"
        )

    def calc_diff(self, last: dtos.OverviewEntry, prev: dtos.OverviewEntry):
        diff = last.value - prev.value
        return diff


class PrevYearSamePeriodBuilder(BaseBuilder):
    def __init__(self, year_offset: int = 1):
        self.offset = year_offset

    def _build(self, overview: dtos.TableResult, complete: dtos.TableResult, msg: str) -> str:
        cur_month_idx = len(overview.rows)
        last_year: dtos.YearlyEntry = complete.rows[self.offset]

        return (
            f"{msg}\n"
            f"Em {last_year.year} foi *{last_year.get_month_value(cur_month_idx)}%*"
        )

class FooterDetailsBuilder(BaseBuilder):
    def _build(self, overview: dtos.TableResult, complete: dtos.TableResult, msg: str) -> str:
        return msg + f"\n\n[Ver detalhes]({PAGE_URL})"


class TrimmerBuilder(BaseBuilder):
    def _build(self, overview: dtos.TableResult, complete: dtos.TableResult, msg: str) -> str:
        return msg.replace(".", "\.").replace("-", "\-")


class MessageFactory:
    def build_message(self, overview: dtos.TableResult, complete: dtos.TableResult):
        builder = HeadlineBuilder()
        next_builder = builder.then(CurPeriodBuilder())
        next_builder = next_builder.then(PrevPeriodDiffBuilder())

        for prev_year in range(1, 5):
            next_builder = next_builder.then(PrevYearSamePeriodBuilder(prev_year))

        next_builder = next_builder.then(FooterDetailsBuilder())
        next_builder = next_builder.then(TrimmerBuilder())

        return builder.build(overview, complete, "")
