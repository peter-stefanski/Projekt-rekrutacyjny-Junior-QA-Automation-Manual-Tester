"""
SearchResultsPage – strona wyników wyszukiwania.

Metody:
- get_all_titles()
- phrase_in_results()
- open_first_result()
"""

from .base_page import BasePage


class SearchResultsPage(BasePage):

    # Stabilne selektory wyników
    RESULTS_LIST = (
        "ul.results, "
        ".results-list, "
        ".search-results"
    )

    RESULT_TITLE = (
        "ul.results li .title, "
        ".search-results .title, "
        "li .movie-title"
    )

    FIRST_RESULT_LINK = (
        "ul.results li:first-child a, "
        ".search-results a:first-child, "
        ".results-list a:first-of-type"
    )

    def get_all_titles(self):

        self.wait_for(self.RESULTS_LIST)
        elements = self.page.query_selector_all(self.RESULT_TITLE)
        return [el.inner_text().strip() for el in elements]

    def phrase_in_results(self, phrase: str) -> bool:

        titles = [t.lower() for t in self.get_all_titles()]
        return any(phrase.lower() in t for t in titles)

    def open_first_result(self):

        self.click(self.FIRST_RESULT_LINK)
