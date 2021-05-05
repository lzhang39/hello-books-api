def test_get_all_books_with_no_records(client):
    # ACT STAGE !!!
    response = client.get("/books")
    response_body = response.get_json()

    # ASSERT STAGE !!!
    assert response.status_code == 200
    assert response_body == []


# 1 !
def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        # 2 !!
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }
