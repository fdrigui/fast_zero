from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='AAA', email='AAA@ZZZ.com', password='123456')
    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'AAA@ZZZ.com'))
    assert result.username == 'AAA'
