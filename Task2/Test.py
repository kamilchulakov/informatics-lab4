import unittest
from parse import process


class MyTestCase(unittest.TestCase):
    def test_something(self):
        text = "Look at what we’d kill: Mosquitos and flies. 'Cuz they’re pests. Lions and tigers. " \
               "'Cuz it’s fun! Chickens and pigs. 'Cuz we’re hungry. Pheasants and quails. 'Cuz it’s fun. " \
               "And we’re hungry. And people. We kill people… 'Cuz they’re pests, And it’s fun!"
        wanted = ["Cuz they’re pests, And it’s fun!"]
        self.assertEqual(process(text), wanted)

    def test_nothing(self):
        text = None
        wanted = None
        self.assertEqual(process(text), wanted)

    def test_files(self):
        with open("test-files/wes-anderson.txt", "r") as file:
            text = file.read()
            wanted = ["I’m looking forward to checking it out with my kiddos, we are huge dog lovers!",
                      "In fact, we've been a bunch of mean jerks!"]
            self.assertEqual(process(text), wanted)
        with open("test-files/bashlachev.txt", "r") as file:
            text = file.read()
            wanted = ["Ты звени, звени, звени, сердце под рубашкою!", "Давай, заряжай — поехали!",
                      "Загремим, засвистим, защелкаем!", "Эй, Братва!"]
            self.assertEqual(process(text, "ru"), wanted)

    def test_russian(self):
        text = "Все сдали лабу, кроме меня! А тесты сами себя не пишут, почему? Получается, автотесты не настоящие!"
        wanted = "Все сдали лабу, кроме меня! Получается, автотесты не настоящие!"
        self.assertEqual(" ".join(process(text, "ru")), wanted)

    def test_spanish(self):
        text = "¡El español es bueno, vivir es lindo!¡Buena suerte y crédito en tu bolsillo!"
        wanted = "¡El español es bueno, vivir es lindo!"
        self.assertEqual("".join(process(text, "es")), wanted)

    def test_german(self):
        text = "Den ganzen Druck vorwärts, statt zu verteidigen!\n\n\n\n\nDas eine trieb das andere an; " \
               "so lächerlich es Ihnen vielleicht scheint, ich \n begann mich zu beschimpfen – 'schneller, schneller!"
        wanted = "Den ganzen Druck vorwärts, statt zu verteidigen! Das eine trieb das andere an; " \
                 "so lächerlich es Ihnen vielleicht scheint, ich \n begann mich zu beschimpfen – 'schneller, schneller!"
        self.assertEqual(" ".join(process(text, "de")), wanted)


if __name__ == '__main__':
    unittest.main()
