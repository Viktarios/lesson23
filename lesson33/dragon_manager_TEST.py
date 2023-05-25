import unittest
from dragonmanager import DragonManager


class DragonManagerTest(unittest.TestCase):
    def test_negative_age(self):
        age = -1
        expected = 0

        actual = DragonManager.calculate_total_heads(age)

        self.assertEqual(expected, actual)

    def test_zero_age(self):
        age = 0
        expected = 0

        actual = DragonManager.calculate_total_heads(age)

        self.assertEqual(expected, actual)

    def test_string_age(self):
        age = "100"
        expected = 0

        actual = DragonManager.calculate_total_heads(age)

        self.assertEqual(expected, actual)

    # positive
    def test_age_between_1_and_200(self):
        age = 100
        expected = 303

        actual = DragonManager.calculate_total_heads(age)

        self.assertEqual(expected, actual)

    def test_age_between_201_and_300(self):
        age = 250
        expected = 703

        actual = DragonManager.calculate_total_heads(age)

        self.assertEqual(expected, actual)

    def test_age_more_than_300(self):
        age = 350
        expected = 853

        actual = DragonManager.calculate_total_heads(age)

        self.assertEqual(expected, actual)

    def test_age_with_1(self):
        age = 1
        expected = 6

        actual = DragonManager.calculate_total_heads(age)

        self.assertEqual(expected, actual)

    def test_age_with_200(self):
        age = 200
        expected = 603

        actual = DragonManager.calculate_total_heads(age)

        self.assertEqual(expected, actual)

    def test_age_with_201(self):
        age = 201
        expected = 605

        actual = DragonManager.calculate_total_heads(age)

        self.assertEqual(expected, actual)

    def test_age_with_300(self):
        age = 300
        expected = 803

        actual = DragonManager.calculate_total_heads(age)

        self.assertEqual(expected, actual)

    def test_age_with_301(self):
        age = 301
        expected = 804

        actual = DragonManager.calculate_total_heads(age)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
