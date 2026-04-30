# Импортируем фреймворк
import pytest


# Псевдотесты на отправку писем с использованием фикстуры

def test_sending_mail_1(set_up, module_setup):
    print("Первое письмо отправлено")


def test_sending_mail_2(set_up, module_setup):
    print("Второе письмо отправлено")
