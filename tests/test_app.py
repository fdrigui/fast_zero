from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'email': 'test@test.com',
            'password': 'password',
        },
    )

    # Retornou Status Code Correto (201)?
    assert response.status_code == HTTPStatus.CREATED

    # Validar Schema de retorno UserPublic
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'email': 'test@test.com',
                'id': 1,
            }
        ]
    }


def test_read_user(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_user_id_greather_than_DB_len(client):
    response = client.get('/users/100')
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_read_user_id_negative(client):
    response = client.get('/users/-5')
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': '123',
            'username': 'testuusername2',
            'email': 'test2@test2.com',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'testuusername2',
        'email': 'test2@test2.com',
        'id': 1,
    }


def test_update_id_greather_than_DB_len(client):
    response = client.put(
        '/users/100',
        json={
            'password': '123',
            'username': 'testuusername2',
            'email': 'test2@test2.com',
            'id': 100,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_id_negative(client):
    response = client.put(
        '/users/-5',
        json={
            'password': '123',
            'username': 'testuusername2',
            'email': 'test2@test2.com',
            'id': -5,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_id_negative(client):
    response = client.delete(
        '/users/-5',
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_id_greather_than_DB_len(client):
    response = client.delete(
        '/users/100',
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}
