# ID: BUG-PT-002;

**Tytuł:** Przycisk "Wyczyść" nie resetuje ustawień sortowania na stronie Filmy.

**Środowisko:**
• Przeglądarka: Chrome 143
• OS: Windows 11
• Adres aplikacji: https://vod.film
• Wersja aplikacji: Nieznana

**Kroki do reprodukcji:**

1. Wejdź na stronę główną Vod.Film
2. Wybierz dowolny film
3. Na stronie filmu spróbuj ocenić daną produkcję za pomocą gwiazdek w sekcji „Oceń film”
4. Sprawdź, czy wszystko działa poprawnie.

**Rezultat oczekiwany(Expected Result):**
• Bez zalogowania się do platformy nie będzie to możliwe
• Powinna pojawić się informacja, że trzeba być zalogowanym, aby móc ocenić daną produkcję.
• Mimo braku możliwości oceniania, powinna wyświetlić się animacja przyznawania oceny.

**Rezultat aktualny(Actual Result):**
• Aplikacja pokazuje, że film został oceniony.
• Brak animacji gwiazdek.
• Informacje w popupie wyświetlają się niepoprawnie: za pierwszym razem „Twoja ocena została przesłana”, a następnie ciągle „Już oceniłeś tę produkcję” przy każdym kliknięciu gwiazdek.
• Błędne wyświetlanie popupu (problem UI)

• Ważność: średni;
• Priorytet: (P3)- średni.
