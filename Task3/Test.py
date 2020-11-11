import unittest
from Parse import *


class MyTestCase(unittest.TestCase):
    def test_nothing(self):
        self.assertEqual(parse_all(None), None)

    def test_fio(self):
        groups = ["P3115", "M666", "YES", "Chess"]
        data = {"Университет ИТМО\nИванов И.И. P3115\nИванов И. P3115": "Университет ИТМО\nИванов И. P3115",
                "Александров А.А. M777": "Александров А.А. M777",
                "Ben Brode NO\nВасильев В.В. YES": "Ben Brode NO\n",
                "Magnus S.C ChessGM Chulakov C.C. Chess": "Magnus S.C ChessGM "}
        group = 0
        for key, value in data.items():
            self.assertEqual(parse_fio(key, groups[group]), value)
            group += 1

    def test_fi(self):
        text = "Студентов С.С. P3115\n" \
               "Student S. P3115"
        wanted = "Студентов С.С. P3115"
        self.assertNotEqual(parse_fi(text, "P3115"), wanted, "It is OK! Not a Bug!")

    def test_nice_group(self):
        groups = ["", "\n\n"]
        text = "Fun F.F. \nText T.T. \n\n\n .. "
        results = ["\n\n .. ", "Fun F.F. \n .. "]
        for i in range(len(results)):
            self.assertEqual(parse_all(text, groups[i]), results[i])


if __name__ == '__main__':
    unittest.main()
