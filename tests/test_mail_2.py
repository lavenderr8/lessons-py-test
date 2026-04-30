# Импортируем фреймворк
import pytest


# Псевдотесты на отправку писем без использования фикстуры

def test_sending_mail_3(set_up, module_setup):
    print("Третье письмо отправлено")


def test_sending_mail_4(set_up, module_setup):
    print("Четвёртое письмо отправлено")
