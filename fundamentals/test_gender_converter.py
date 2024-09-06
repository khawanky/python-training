from unittest import TestCase
from gender_converter import convert_gender

class Test(TestCase):
    def test_convert_gender_male(self):
        male_gender = convert_gender('m')
        self.assertEqual(male_gender,'MALE')

    def test_convert_gender_female(self):

        female_gender = convert_gender('f')
        self.assertEqual(female_gender,'FEMALE')

    def test_convert_gender_unknown(self):
        unknown_gender = convert_gender('else')
        self.assertEqual(unknown_gender,'UNKNOWN')
