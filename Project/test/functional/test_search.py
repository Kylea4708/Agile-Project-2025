# test/functional/test_search.py
def test_booksearch_correct_title(client):
    response = client.get('/books?q=Python 101')
    assert response.status_code == 200
    assert b"Python 101" in response.data
    assert b"Test 101" not in response.data

def test_user_correct_name(client):
    response = client.get('/users?q=John Doe')
    assert response.status_code == 200
    assert b"John Doe" in response.data

def test_invalid_booksearch_title(client):
    response = client.get('/books?q=Nonexistent Book')
    assert response.status_code == 200
    assert b"Python 101" not in response.data
    assert b"Test 101" not in response.data

def test_invalid_usersearch(client):
    response = client.get('/users?q=Nonexistent User')
    assert response.status_code == 200
    assert b"Nonexistent User" in response.data

def test_booksearch_author(client):
    response = client.get('/books?q=Whoisthis')
    assert response.status_code == 200
    assert b"Luke Skywalker" not in response.data
    assert b"Python 101" not in response.data

def test_usersearch_phone(client):
    response = client.get('/users?q=1234567890')
    assert response.status_code == 200
    assert b"1234567890" in response.data or b"(123) 456-7890" in response.data

def test_booksearch_invalid_author(client):
    response = client.get('/books?q=NoAuthorMatch')
    assert response.status_code == 200
    assert b"Luke Skywalker" not in response.data or b"No results found" in response.data

def test_usersearch_invalid_phone(client):
    response = client.get('/users?q=0000000000')
    assert response.status_code == 200
    assert b"1234567890" not in response.data or b"No results found" in response.data