# test/functional/test_search.py
def test_booksearch_correct_title(client):
    response = client.get('/books?q=Python 101')
    assert response.status_code == 200
    assert b"Python 101" in response.data

def test_user_correct_name(client):
    response = client.get('/users?q=John Doe')
    assert response.status_code == 200
    assert b"John Doe" in response.data

def test_invalid_booksearch_title(client):
    response = client.get('/books?q=Nonexistent Book')
    assert response.status_code == 200
    assert b"Nonexistent Book" in response.data

def test_invalid_usersearch(client):
    response = client.get('/users?q=Nonexistent User')
    assert response.status_code == 200
    assert b"Nonexistent User" in response.data