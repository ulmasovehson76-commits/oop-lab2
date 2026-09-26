from datetime import datetime
import shlex


class Planet:
    def __init__(self, name, discovery_date, radius):
        self.name = name
        self.discovery_date = discovery_date
        self.radius = radius

    def __str__(self):
        return (
            f"Планета:\n"
            f"  Название: {self.name}\n"
            f"  Дата открытия: {self.discovery_date.strftime('%Y.%m.%d')}\n"
            f"  Радиус: {self.radius} км"
        )

 class Exoplanet(Planet):
    """Экзопланета: добавляет звездную систему."""
    def __init__(self, name, discovery_date, radius, star_system):
        super().__init__(name, discovery_date, radius)
        self.star_system = star_system

    def __str__(self):
        return (f"Экзопланета: {self.name}\n"
                f"  Звездная система: {self.star_system}\n"
                f"  Дата открытия: {self.discovery_date.strftime('%Y.%m.%d')}\n"
                f"  Радиус: {self.radius} км")

class DwarfPlanet(Planet):
    """Карликовая планета: добавляет признак пояса Койпера."""
    def __init__(self, name, discovery_date, radius, is_trans_neptunian):
        super().__init__(name, discovery_date, radius)
        self.is_trans_neptunian = is_trans_neptunian

    def __str__(self):
        return (f"Карликовая планета: {self.name}\n"
                f"  Пояс Койпера: {self.is_trans_neptunian}\n"
                f"  Дата открытия: {self.discovery_date.strftime('%Y.%m.%d')}\n"
                f"  Радиус: {self.radius} км")
class ObjectFactory:
    @staticmethod
    def create_object(text):
        # Разбиваем строку с учетом кавычек
        parts = shlex.split(text)

        obj_type = parts[0]

        if obj_type.lower() == "планета":
            name = parts[1]
            discovery_date = datetime.strptime(parts[2], "%Y.%m.%d").date()
            radius = float(parts[3])

            return Planet(name, discovery_date, radius)

        raise ValueError("Неизвестный тип объекта")


def main():
    print("Введите описание объекта:")
    print('Пример: Планета "Марс" 1659.11.28 3389.5')
    print('Пример: Планета "нептун')
    text = input("> ")

    obj = ObjectFactory.create_object(text)

    print("\nСоздан объект:")
    print(obj)


if __name__ == "__main__":
    main()
