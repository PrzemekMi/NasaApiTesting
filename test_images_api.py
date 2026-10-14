import requests


IMAGES_API_URL = "https://images-api.nasa.gov/search"


def test_images_api_search_returns_results():
    response = requests.get(
        IMAGES_API_URL,
        params={"q": "Apollo 11"},
        timeout=10,
    )

    assert response.status_code == 200
    collection = response.json()["collection"]
    assert isinstance(collection["items"], list)
    assert collection["metadata"]["total_hits"] > 0
