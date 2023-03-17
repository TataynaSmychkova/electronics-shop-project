import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item('Смартфон', 10000, 20)


def test_item_init(item1):
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 20


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    item1.apply_discount()
    assert item1.price == 10000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('text') == 0


def test_name():
    item = Item(name='Смартфон', price=10000, quantity=20)
    assert item.name == 'Смартфон'
    item.name = 'текст'
    assert item.name == 'текст'
    with pytest.raises(Exception):
        item.name = 'СуперСмартфон'


def test__repr__():
    item1 = Item(name='Смартфон', price=10000, quantity=20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test__str__():
    item1 = Item(name='Смартфон', price=10000, quantity=20)
    assert str(item1) == 'Смартфон'

