from abc import ABC, abstractmethod

class GermanLanguage(ABC):
    @abstractmethod
    def greet(self):
        pass

class Bavarian(GermanLanguage):
    def greet(self):
        return "Grüß Gott"

class Swabian(GermanLanguage):
    def greet(self):
        return "Hallo zusammen"

class GenericGerman:
    @staticmethod
    def common_phrase():
        return "Wie geht's?"

class Tourist(GermanLanguage, GenericGerman):
    def greet(self):
        return "Hello!"

class GermanDialogue:
    def __init__(self, language):
        self.language = language

    def formal_greeting(self):
        return self.language.greet() + ", " + self.common_phrase()

class DynamicLanguageChanger:
    def __init__(self, language):
        self.language = language

    def change_language(self, new_language):
        self.language = new_language

    def perform_greeting(self):
        return self.language.greet()

def main():
    german = GermanLanguage()
    bavarian = Bavarian()
    swabian = Swabian()
    tourist = Tourist()
    dialogue = GermanDialogue(bavarian)
    changer = DynamicLanguageChanger(swabian)

    print(german.greet())
    print(bavarian.greet())
    print(swabian.greet())
    print(tourist.greet())
    print(dialogue.formal_greeting())
    print(changer.perform_greeting())
    changer.change_language(tourist)
    print(changer.perform_greeting())

if __name__ == "__main__":
    main()
