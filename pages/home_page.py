"""
HomePage – strona główna Vod.Film.

Metody:
- open_home()
- open_search()
- type_search_phrase()
- confirm_search()
"""

from .base_page import BasePage


class HomePage(BasePage):

    # Stabilne selektory (multi–alternatywy)
    SEARCH_ICON = (
        "button[aria-label='Szukaj'], "
        "button[title='Szukaj'], "
        "[class*='search'], "
        "svg[aria-label='search']"
    )

    SEARCH_INPUT = (
        "input[name='q'], "
        "input[type='search'], "
        "input[placeholder*='szuk'], "
        "input[class*='search']"
    )

    SEARCH_CONFIRM = (
        "button[type='submit'], "
        "button.search-submit, "
        "form.search button"
    )

    def open_home(self):
        self.goto("")  # https://vod.film/

    def open_search(self):
        self.click(self.SEARCH_ICON)

    def type_search_phrase(self, phrase: str):
        self.type(self.SEARCH_INPUT, phrase)

    def confirm_search(self):

        try:
            self.click(self.SEARCH_CONFIRM)
        except AssertionError:
            pass 