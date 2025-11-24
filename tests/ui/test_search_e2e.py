import pytest
import time
from urllib.parse import urlparse

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.movie_details_page import MovieDetailsPage
from pages.popup_redirect_page import PopupRedirectPage 

@pytest.mark.parametrize(
    "phrase, expected_in_results",
    [
        ("the pickup", True),   
        ("abcxyz123", False),     
    ],
)
def test_search_and_play_popup(page, phrase, expected_in_results):
    home = HomePage(page)
    results = SearchResultsPage(page)
    movie = MovieDetailsPage(page)
    popup = PopupRedirectPage(page) 

    home.open_home()
    home.open_search()
    home.type_search_phrase(phrase)
    home.confirm_search()

    if not expected_in_results:
        found = results.phrase_in_results(phrase)
        assert not found, f"Negatywny scenariusz: fraza '{phrase}' powinna nie być w wynikach, ale została znaleziona."
        return

    found = results.phrase_in_results(phrase)
    assert found, f"Fraza '{phrase}' nie pojawiła się w wynikach wyszukiwania (oczekiwano przynajmniej jednego wyniku)."

    results.open_first_result()

    h1_text = movie.get_h1()
    assert (
        phrase.lower() in h1_text.lower()
    ), f"H1 nie zawiera frazy. Oczekiwano: '{phrase}', znaleziono H1: '{h1_text}'"

    assert movie.is_player_visible(), "Player wideo nie jest widoczny na stronie szczegółów filmu."

    movie.click_play()

    start = time.perf_counter()

    try:
        movie.wait_for_popup(timeout_seconds=60)
    except AssertionError as e:
        page.screenshot(path=f"screenshots/popup_not_found_{phrase}.png")
        raise AssertionError("Popup nie pojawił się w ciągu 60 sekund po kliknięciu Play.") from e
    elapsed = time.perf_counter() - start

    assert (
        elapsed >= 1.0
    ), f"Popup pojawił się za szybko (w czasie {elapsed:.2f}s) — oczekiwany minimalny czas 1s."
    assert (
        elapsed <= 60.0
    ), f"Popup pojawił się po {elapsed:.2f}s, co przekracza dozwolony limit 60s."

    popup_link = movie.get_popup_link()
    assert popup_link, "Popup nie zawiera linku (href pusty lub element nie znaleziony)."

    parsed = urlparse(popup_link)
    assert parsed.scheme in ("http", "https"), f"Link z popupu nie ma schematu http/https: {popup_link}"

    host = parsed.netloc
    assert host, f"Nie udało się wyodrębnić hosta z linku popupu: {popup_link}"

    print(f"[INFO] Fraza: '{phrase}' — popup pojawił się po {elapsed:.2f}s, link: {popup_link}")