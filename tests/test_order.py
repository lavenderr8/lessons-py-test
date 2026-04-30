# Импортируем фреймворк
import pytest


# Используем библиотеку ORDERING для определения
# очерёдности исполнения функций

@pytest.mark.run(order=6)
def test_method_1(set_up):
    print("Метод 1, который должен выполниться 6-ым")


@pytest.mark.run(order=3)
def test_method_2(set_up):
    print("Метод 2, который должен выполниться 3-им")


@pytest.mark.run(order=5)
def test_method_3(set_up):
    print("Метод 3, который должен выполниться 5-ым")


@pytest.mark.run(order=2)
def test_method_4(set_up):
    print("Метод 4, который должен выполниться 2-ым")


@pytest.mark.run(order=4)
def test_method_5(set_up):
    print("Метод 5, который должен выполниться 4-ым")


@pytest.mark.run(order=1)
def test_method_6(set_up):
    print("Метод 6, который должен выполниться 1-ым")
