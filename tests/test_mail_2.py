# Импортируем фреймворк
import pytest


# Фикстура
@pytest.fixture
def set_up():
    print("Вход в систему выполнен!")


# Псевдотесты на отправку писем без использования фикстуры

def test_sending_mail_1():
    print("Первое письмо отправлено")


def test_sending_mail_2():
    print("Второе письмо отправлено")
