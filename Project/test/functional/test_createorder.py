# test/functional/test_createorder.py
def test_creating_order(client):
    response = client.post('/order/new', data={
        'user_id': 1,
        'book_id': 1,
        'quantity': 2
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b"Orders" in response.data

def test_invalid_user_in_order(client):
    response = client.post('/order/new', data={
        'user_id': 9999,
        'book_id': 1,
        'quantity': 2
    })
    assert response.status_code == 404
    assert b"User or Book not found" in response.data

def test_invalid_book_in_order(client):
    response = client.post('/order/new', data={
        'user_id': 1,
        'book_id': 9999,
        'quantity': 2
    })
    assert response.status_code == 404
    assert b"User or Book not found" in response.data

def test_invalid_quantity_in_order(client):
    response = client.post('/order/new', data={
        'user_id': 1,
        'book_id': 1,
        'quantity': -1
    }, follow_redirects=True) 
    
    
    assert response.status_code == 200
  