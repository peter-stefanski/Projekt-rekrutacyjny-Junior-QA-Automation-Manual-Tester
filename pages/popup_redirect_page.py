"""
PopupRedirectPage – osobny POM do obsługi popupu redirect.

Metody:
- is_visible()
- get_link()
"""

from .base_page import BasePage


class PopupRedirectPage(BasePage):

    POPUP = ".popup, .modal, div[class*='redirect'], div[role='dialog']"
    POPUP_LINK = ".popup a, .modal a, div[class*='redirect'] a"

    def is_visible(self) -> bool:
        try:
            self.wait_for(self.POPUP, timeout=5000)
            return True
        except AssertionError:
            return False

    def get_link(self) -> str:
        return self.get_attribute(self.POPUP_LINK, "href")
