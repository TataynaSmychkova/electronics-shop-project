from csv import DictReader
from sett import PATH_TO_FILE


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open(PATH_TO_FILE, 'r', newline='', encoding='windows-1251') as csvfile:
            data = DictReader(csvfile)
            for row in data:
                cls.all.append(Item(**row))

    @staticmethod
    def string_to_number(any_string: str) -> int:
        try:
            return int(float(any_string))
        except ValueError:
            return 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if len(value) <= 10:
            self.__name = value
        else:
            raise ValueError

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
