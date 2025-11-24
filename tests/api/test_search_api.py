import requests
import pytest

API_ENDPOINT = "https://vod.film/search-defaults"

def test_api_search_the_pickup():

    payload = {
        "host": "vod.film",
        "locale": "pl", 
        "searchTerm": "the pickup"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(
        API_ENDPOINT, 
        json=payload,  
        headers=headers,
        timeout=10
    )

    assert response.status_code == 200, \
        f"Niepoprawny status code: {response.status_code}. Response: {response.text}"


    try:
        data = response.json()
    except ValueError:
        pytest.fail("Odpowiedź nie jest poprawnym JSON-em")


    assert isinstance(data, list), "Odpowiedź API nie jest listą"
    

    titles = [item.get("title", "").lower() for item in data if isinstance(item, dict)]
    
    expected_titles = ["the pickup cały film", "the pickup"]
    found = any(any(expected in title for expected in expected_titles) for title in titles)
    
    assert found, \
        f"API nie zwróciło filmu 'The Pickup' w wynikach. Znalezione tytuły: {titles}"

    pickup_movie = None
    for movie in data:
        if isinstance(movie, dict) and "the pickup" in movie.get("title", "").lower():
            pickup_movie = movie
            break

    assert pickup_movie is not None, "Nie znaleziono szczegółów filmu 'The Pickup'"

    expected_fields = ["title", "type", "tmdb_id", "release_date", "vote_average"]
    for field in expected_fields:
        assert field in pickup_movie, f"Brak wymaganego pola '{field}' w danych filmu"
    

    assert pickup_movie["title"] == "The Pickup Cały Film", \
        f"Nieprawidłowy tytuł: {pickup_movie['title']}"
    
    assert pickup_movie["type"] == "movie", \
        f"Nieprawidłowy typ: {pickup_movie['type']}"
    
    assert pickup_movie["tmdb_id"] == 1106289, \
        f"Nieprawidłowe TMDB ID: {pickup_movie['tmdb_id']}"


    assert len(data) >= 1, \
        "Lista wyników jest pusta — oczekiwano co najmniej 1 pozycji."

    print(f"✓ Test passed! Found {len(data)} results, including '{pickup_movie['title']}'")


def test_api_search_empty():

    payload = {
        "host": "vod.film", 
        "locale": "pl",
        "searchTerm": ""
    }
    
    response = requests.post(API_ENDPOINT, json=payload, timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

if __name__ == "__main__":

    test_api_search_the_pickup()