# Zadanie rekrutacyjne - Junior QA Automation

## Opis projektu

Celem projektu jest automatyczne przetestowanie kluczowych funkcjonalności serwisu **Vod.Film**, w tym:

- działania wyszukiwarki filmów (pozytywny i negatywny scenariusz),
- poprawności wyświetlania strony szczegółów filmu,
- widoczności i działania odtwarzacza,
- pojawienia się popupu (w zakresie 1–60 sekund),
- poprawności działania backendowego API „live search”.

Projekt wykorzystuje architekturę **Page Object Model (POM)**, dzięki czemu logika stron jest oddzielona od warstwy testowej.

## Podstawowe technologie

- **Język programowania**: Python 3.10+
- **Testy UI**: Playwright
- **Testy API**: requests
- **Framework testowy**: pytest

## Architektura i narzędzia

- **Wzorzec projektowy**: Page Object Model (POM)
- **Kontrola wersji**: Git + GitHub
- **CI/CD**: GitHub Actions
- **Konteneryzacja**: Docker + docker-compose

## Instalacja

### 1. Sklonuj repozytorium

- git clone https://github.com/peter-stefanski/Projekt-rekrutacyjny-Junior-QA-Automation-Manual-Tester.git
- cd vodfilm-qa

### 2.Utwórz i aktywuj środowisko wirtualne

- **Windows:**
  python -m venv venv
  venv\Scripts\activate

- **Linux / macOS:**
  python3 -m venv venv
  source venv/bin/activate

- **Zainstaluj zależności:**

pip install -r requirements.txt

- **Zainstaluj przeglądarki Playwright:**

pip playwright install

## Komendy do uruchamiania testów:

**Wszystkie testy (UI + API)**
pytest -v

**Tylko testy UI**
pytest tests/ui -v

**Tylko testy API**
pytest tests/api -v

## Wybrana biblioteka: Playwright

W projekcie użyto: Playwright

Uzasadnienie:

- jest szybszy i stabilniejszy niż Selenium,
- posiada automatyczne oczekiwania (auto-waiting),
- idealnie nadaje się do testowania elementów dynamicznych (np. popup pojawiający się po 1–60 sekundach),
- ma prosty, czytelny API idealny dla początkujących,
- wspiera testy równoległe i działa szybciej od Selenium.

# Analiza SQL: Weryfikacja powiązań filmu "The Pickup"

## Cel zapytania

Potwierdzenie, że film "The Pickup" jest poprawnie powiązany z kategorią za pomocą zapytania SQL z użyciem JOIN.

## Struktura tabel

- movies - tabela filmów
  - movie_id (PK) - identyfikator filmu
  - title - tytuł filmu
  - release_year - rok produkcji
- categories - tabela kategorii
  - category_id (PK) - identyfikator kategorii
  - name - nazwa kategorii
- movie_categories - tabela łącząca (many-to-many)
  - movie_id (FK) - identyfikator filmu
  - category_id (FK) - identyfikator kategorii

## Zapytanie SQL

- SELECT
- m.movie_id,
- m.title AS movie_title,
- c.category_id,
- c.name AS category_name
- FROM movies m
- INNER JOIN movie_categories mc ON m.movie_id = mc.movie_id
- INNER JOIN categories c ON mc.category_id = c.category_id
- WHERE m.title = 'The Pickup';
