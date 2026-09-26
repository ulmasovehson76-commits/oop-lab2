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
        parts = shlex.split(text)
        obj_type = parts[0].lower()

        if obj_type == "экзопланета":
            return ObjectFactory._create_exoplanet(parts)
        elif obj_type == "карликоваяпланета":
            return ObjectFactory._create_dwarf_planet(parts)
        elif obj_type in ("планета", "планеты"):
            return ObjectFactory._create_planet(parts)
        else:
            raise ValueError(f"Неизвестный тип: {obj_type}")

    @staticmethod
    def _create_planet(parts):
        name = parts[1]
        discovery_date = datetime.strptime(parts[2], "%Y.%m.%d").date()
        radius = float(parts[3])
        return Planet(name, discovery_date, radius)

    @staticmethod
    def _create_exoplanet(parts):
        name = parts[1]
        discovery_date = datetime.strptime(parts[2], "%Y.%m.%d").date()
        radius = float(parts[3])
        star_system = parts[4]
        return Exoplanet(name, discovery_date, radius, star_system)

    @staticmethod
    def _create_dwarf_planet(parts):
        name = parts[1]
        discovery_date = datetime.strptime(parts[2], "%Y.%m.%d").date()
        radius = float(parts[3])
        is_trans_neptunian = parts[4]
        return DwarfPlanet(name, discovery_date, radius, is_trans_neptunian)

        raise ValueError("Неизвестный тип объекта")


def main():
    print("Введите описание объекта:")
    print('Пример: Планета "Марс" 1659.11.28 3389.5')
    print('Пример: Планета "нептун')
    text = input("> ")

    obj = ObjectFactory.create_object(text)

    print("\nСоздан объект:")
    print(obj)


def process_data(lines):
    """Обрабатывает список строк, возвращает список объектов."""
    objects = []
    for line in lines:
        if line.strip():  # пропускаем пустые строки
            obj = ObjectFactory.create_object(line.strip())
            objects.append(obj)
    return objects

if __name__ == "__main__":
    data_lines = [
        'Планеты "Марс" 1659.12.28 3389.5',
        'Экзопланета "Проксима Центавра b" 2016.08.24 1.1 "Проксима Центавра"',
        'КарликоваяПланета "Плутон" 1930.02.18 1188.3 да',
        'Планеты "Нептун" 1846.09.23 24622.0'
    ]

    print("--- Обработка набора объектов ---")
    results = process_data(data_lines)
    
    for obj in results:
        print(obj)
        print("-" * 30)
    main()
