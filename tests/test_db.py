from fast_zero.models import User


def test_create_userr():
    user = User(
        username='AAA',
        email='AAA@ZZZ.com',
        password='123456'
        )
    assert user.username == 'AAA'
