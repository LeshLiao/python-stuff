# Python Code for factory method

class FrenchLocalizer:

    def __init__(self):
        print('French __init__')
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle": "cyclette"}

    def localize(self, msg):
        return self.translations.get(msg, msg)


class SpanishLocalizer:

    def __init__(self):
        print('Spanish __init__')
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle": "ciclo"}

    def localize(self, msg):

        return self.translations.get(msg, msg)


class EnglishLocalizer:

    def __init__(self):
        print('English __init__')

    def localize(self, msg):
        return msg


class LocalizerFactory:

    @staticmethod
    def get_localizer(language='English'):
        localizer_list = {
            "French": FrenchLocalizer,
            "English": EnglishLocalizer,
            "Spanish": SpanishLocalizer,
        }
        return localizer_list[language]()


if __name__ == "__main__":
    e = LocalizerFactory.get_localizer("English")
    f = LocalizerFactory.get_localizer("French")
    s = LocalizerFactory.get_localizer("Spanish")

    message = ["car", "bike", "cycle"]

    for msg in message:
        print(e.localize(msg))
        print(f.localize(msg))
        print(s.localize(msg))
