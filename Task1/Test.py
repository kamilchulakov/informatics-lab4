import unittest
import random
from Parse import process


class MyTestCase(unittest.TestCase):
    def test_main(self):
        processed = "Уважаемые студенты! В эту субботу в 15:00 планируется доп. занятие на 2 часа. То есть в " \
                    "17:00:01 оно уже точно кончится. "
        wanted = "Уважаемые студенты! В эту субботу в (TBD) планируется доп. занятие на 2 часа. То есть в (" \
                 "TBD) оно уже точно кончится. "
        self.assertEqual(process(processed), wanted)

    def test_nothing(self):
        processed = ""
        wanted = ""
        self.assertEqual(process(processed), wanted)

    def test_none(self):
        self.assertIsNone(process(None))
        self.assertIsNone(process())

    def test_overflow(self):
        self.assertEqual(process("21:88"), "21:88")

    def test_not_a_number(self):
        self.assertEqual(process("0:0:00"), "0:0:00")

    def test_dict(self):
        data = {"10:00": "(TBD)",
                "24:00": "24:00",
                "24:00:00": "24:(TBD)",
                "222:00 is 2 x 21:00": "2(TBD) is 2 x (TBD)",
                "ENGLISH 12:00 INFORMATICS 18:00 OPD 1:00 JAVA 1-00": "ENGLISH (TBD) INFORMATICS (TBD) OPD 1:00 JAVA "
                                                                      "1-00"}
        for key, value in data.items():
            self.assertEqual(process(key), value)

#   def test_randomized(self):
#        for i in range(10):
#            data = get_tests(random.randint(1, 10), random.randint(1, 15))
#            for key, value in data.items():
#                self.assertEqual(process(key), value)

    def test_by_pvbalakshin(self):
        pass


if __name__ == '__main__':
    unittest.main()
