import unittest
from main import Planet, Exoplanet, DwarfPlanet, ObjectFactory

class TestObjectFactory(unittest.TestCase):

    def test_create_planet(self):
        """Тест: создание обычной планеты."""
        obj = ObjectFactory.create_object('Планеты "Марс" 1659.12.28 3389.5')
        self.assertIsInstance(obj, Planet)
        self.assertEqual(obj.name, "Марс")
        self.assertEqual(obj.radius, 3389.5)

    def test_create_exoplanet(self):
        """Тест: создание экзопланеты."""
        obj = ObjectFactory.create_object(
            'Экзопланета "Проксима Центавра b" 2016.08.24 1.1 "Проксима Центавра"'
        )
        self.assertIsInstance(obj, Exoplanet)
        self.assertEqual(obj.name, "Проксима Центавра b")
        self.assertEqual(obj.star_system, "Проксима Центавра")

    def test_create_dwarf_planet(self):
        """Тест: создание карликовой планеты."""
        obj = ObjectFactory.create_object(
            'КарликоваяПланета "Плутон" 1930.02.18 1188.3 да'
        )
        self.assertIsInstance(obj, DwarfPlanet)
        self.assertEqual(obj.name, "Плутон")
        self.assertEqual(obj.is_trans_neptunian, "да")

    def test_error_unknown_type(self):
        """Тест: неизвестный тип объекта -> None."""
        obj = ObjectFactory.create_object('Кометa "Галлея" 1758.03.13 11.0')
        self.assertIsNone(obj)

    def test_error_bad_date(self):
        """Тест: неправильная дата -> None."""
        obj = ObjectFactory.create_object('Планеты "Марс" 1659.абв 3389.5')
        self.assertIsNone(obj)

    def test_error_missing_fields(self):
        """Тест: не хватает полей -> None."""
        obj = ObjectFactory.create_object('Планеты "Марс"')
        self.assertIsNone(obj)

if __name__ == '__main__':
    unittest.main()
