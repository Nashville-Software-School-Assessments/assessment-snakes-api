import requests

def test_get_all_owners():
    """
    Ensure we can get (GET) all owners.
    """
    response = requests.get('http://localhost:8088/owners')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
def test_get_single_owner():
    """
    Ensure we can get (GET) a single owner.
    """
    response = requests.get('http://localhost:8088/owners/1')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
def test_get_all_snakes():
    """
    Ensure we can get (GET) all snakes.
    """
    response = requests.get('http://localhost:8088/snakes')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
def test_create_snakes():
    """
    Ensure we can create (POST) a new snake.
    """
    snake = {
	"name":"adminsnake",
	"owner_id": 1,
	"species_id": 1,
	"gender": "female",
	"color": "blue"
    }
    response = requests.post('http://localhost:8088/snakes', json=snake)
    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    assert response.json()['name'] == 'adminsnake'

def test_get_single_snake():
    """
    Ensure we can get (GET) a single snake.
    """
    response = requests.get('http://localhost:8088/snakes/2')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
def test_get_snakes_by_species():
    """'
    Ensure we can get (GET) all snakes my their fk species id
    """
    species_id = 1
    response = requests.get(f'http://localhost:8088/snakes?species={species_id}')
    assert response.status_code == 200
    assert response.json()[0]['species_id'] == species_id
    assert isinstance(response.json(), list)
def test_post_incomplete_snake():
    """
    Ensure when sending an incomplete snake object, we get a 400 error
    """
    snake = {    
    "name":"adminsnake",
    "owner_id": 1}
    response = requests.post('http://localhost:8088/snakes', json=snake)
    assert response.status_code == 400
    assert 'color' in response.json()['message']
def test_no_alone_snakes():
    """_ make sure the aonyxx cinerea is not got alone :( _
    """
    response = requests.get('http://localhost:8088/snakes/1')
    assert response.status_code == 405
def test_get_all_species():
    """
    Ensure we can get (GET) all species.
    """
    response = requests.get('http://localhost:8088/species')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
def test_get_single_species():
    """
    Ensure we can get (GET) a single species.
    """
    response = requests.get('http://localhost:8088/species/1')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
def test_unsupported_get():
    """
    Ensure an unsupported endpoint returns a blank request body and status code 404.
    """
    response = requests.get('http://localhost:8088/unsupported')
    assert response.status_code == 404
    assert response.json() == ""
def test_unsupported_post():
    """
    Ensure an unsupported endpoint returns a blank request body and status code 404.
    """
    snake = {
	"name":"adminsnake",
	"owner_id": 1,
	"species_id": 1,
	"gender": "female",
	"color": "blue"
    }
    response = requests.post('http://localhost:8088/unsupported', json='snake')
    assert response.status_code == 404
    assert response.json() == ""
def test_unsupported_put():
    """
    Ensure an unsupported endpoint returns a blank request body and status code 404.
    """
    response = requests.put('http://localhost:8088/unsupported/1')
    assert response.status_code == 404
    assert isinstance(response.json(), str)
    assert response.json() == ""
    
def test_unsupported_delete():
    """
    Ensure an unsupported endpoint returns a blank request body and status code 404.
    """
    response = requests.delete('http://localhost:8088/unsupported/1')
    assert response.status_code == 404
    assert isinstance(response.json(), str)
    assert response.json() == ""