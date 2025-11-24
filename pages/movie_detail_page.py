from .base_page import BasePage


class MovieDetailsPage(BasePage):

    H1 = "h1, .movie-title, .title"
    VIDEO_PLAYER = (
        "video, "
        "iframe.video-player, "
        ".video-player-container, "
        "[class*='player']"
    )
    PLAY_BUTTON = (
        "button.play, "
        ".player-btn-play, "
        "[aria-label='play']"
    )
    POPUP = (
        ".popup, "
        ".modal, "
        "div[class*='redirect'], "
        "div[role='dialog']"
    )
    POPUP_LINK = ".popup a, .modal a, div[class*='redirect'] a"

    def get_h1(self) -> str:

        return self.get_text(self.H1)

    def is_player_visible(self) -> bool:

        try:
            self.wait_for(self.VIDEO_PLAYER, timeout=5000)
            return True
        except AssertionError:
            return False

    def click_play(self):

        self.click(self.PLAY_BUTTON)

    def wait_for_popup(self, timeout_seconds: int = 60):

        timeout_ms = timeout_seconds * 1000
        self.wait_for(self.POPUP, timeout=timeout_ms)

    def get_popup_link(self) -> str:

        return self.get_attribute(self.POPUP_LINK, "href")
