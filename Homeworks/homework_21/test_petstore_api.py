import requests
import json

base_url = 'https://petstore.swagger.io/v2'


def test_get_pet():
    pet_id = 13
    url = f'{base_url}/pet/{pet_id}'
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()
    print(data)

    with open('pet_data.json', 'w') as file:
        json.dump(data, file)


def test_add_pet():
    pet_data = {
        'id': 22,
        'name': 'Shanty',
        'category': {
            'id': 1,
            'name': 'Dogs'
        },
        'status': 'available'
    }

    url = f'{base_url}/pet'
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=json.dumps(pet_data))

    assert response.status_code == 200
    data = response.json()
    assert data is not None
    print(data)

    with open('added_pet_data.json', 'w') as file:
        json.dump(data, file)


def test_petstore_parametrized():
    url = f'{base_url}/pet'
    body = {
        "id": 1,
        "category": {"id": 1, "name": "dogs"},
        "name": "Rex",
        "photoUrls": ["https://example.com/dog.jpg"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "available"
    }

    response = requests.post(url, json=body)
    response.raise_for_status()

    data = response.json()
    with open('pet_result.txt', 'w') as file:
        json.dump(data, file)

    assert 'Rex' in response.text



