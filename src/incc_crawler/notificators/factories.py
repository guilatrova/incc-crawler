from incc_crawler import dtos
from incc_crawler.crawler import PAGE_URL


class MessageFactory:
    def build_message(self, overview: dtos.TableResult, complete: dtos.TableResult):
        last_period: dtos.OverviewEntry = overview.rows[0]
        # TODO: what if there's only 1? e.g. January
        period_before: dtos.OverviewEntry = overview.rows[1]
        diff = self.calc_diff_prev_diff(last_period, period_before)

        cur_month_idx = len(overview.rows)
        last_year: dtos.YearlyEntry = complete.rows[1]
        prev_year: dtos.YearlyEntry = complete.rows[2]

        partial = (
            f"Período de *{last_period.period}*\n"

            # Overview last month
            f"INCC de: *{last_period.value}%* / "
            f"acumulado no ano: *{last_period.accumulated_year}%*\n"

            # Overview prev month
            f"Mês anterior: {period_before.value}% / Diferença: *{diff:.{1}f}%*\n"

            # Last year
            f"\nEm {last_year.year} foi *{last_year.get_month_value(cur_month_idx)}%*"

            f"\nEm {prev_year.year} foi *{prev_year.get_month_value(cur_month_idx)}%*"

            # Detalhes
            f"\n\n[Ver detalhes]({PAGE_URL})"
        )
        return partial.replace(".", "\.")

    def calc_diff_prev_diff(self, last: dtos.OverviewEntry, prev: dtos.OverviewEntry):
        print(last.value)
        diff = last.value - prev.value
        return diff
