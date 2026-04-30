# Импортируем фреймворк
import pytest


# Фикстура
@pytest.fixture
def set_up():
    print("Вход в систему выполнен!")


# Псевдотесты на отправку писем с использованием фикстуры

def test_sending_mail_1(set_up):
    print("Первое письмо отправлено")


def test_sending_mail_2(set_up):
    print("Второе письмо отправлено")
