from sqlalchemy import create_engine

from fast_zero.models import User, table_registry


def test_create_user():
    engine = create_engine('sqlite:///database.db')

    table_registry.metadata.create_all(engine)

    user = User(username='AAA', email='AAA@ZZZ.com', password='123456')
    assert user.username == 'AAA'
