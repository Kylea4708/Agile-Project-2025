def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Books" in response.data or b"Readers" in response.data

def test_order_delete(client):
    response = client.post("/orders/1/delete", follow_redirects=True)
    assert response.status_code == 200
    assert b"Orders" in response.data

def test_manage_books_page(client):
    response = client.get("/manage-books")
    assert response.status_code == 200
    assert b"Manage Books" in response.data or b"Create Book" in response.data

def test_manage_books_create(client):
    response = client.post("/manage-books", data={
        "create": "Create",
        "title": "Test Book",
        "author": "Test Author",
        "genre_name": "Test Genre",
        "quantity": 5,
        "physical": "on"
    }, follow_redirects=True)
    assert response.status_code == 200