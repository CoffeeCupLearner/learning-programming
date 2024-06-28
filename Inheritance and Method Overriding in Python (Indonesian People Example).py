class Human:
    """
    Represents a human with basic actions like eating and sleeping.
    """

    def __init__(self, name, origin):
        """
        Initialize a Human object with a name and origin.
        """
        self.name = name
        self.origin = origin

    def eat(self):
        """
        Simulates the action of eating.
        """
        print(f"{self.name} is enjoying a meal.")

    def sleep(self):
        """
        Simulates the action of sleeping.
        """
        print(f"{self.name} is getting some rest.")


class Javanese(Human):
    """
    Represents a Javanese person, inheriting from Human.
    - Inheritance: Inherits from Human class.
    - Method Override: Overrides eat() method from Human.
    """

    def __init__(self, name, origin, favorite_batik):
        """
        Initialize a Javanese object with a name, origin, and favorite batik pattern.
        """
        super().__init__(name, origin)
        self.favorite_batik = favorite_batik

    def eat(self):
        """
        Simulates the action of eating Gudeg, a Javanese favorite food.
        - Method Override: Overrides eat() method from Human.
        """
        print(f"{self.name} is enjoying a delicious Gudeg, their favorite food.")

    def dance(self):
        """
        Simulates the action of performing a Javanese dance.
        """
        print(f"{self.name} is performing a graceful Javanese dance.")


class Chinese(Human):
    """
    Represents a Chinese person, inheriting from Human.
    - Inheritance: Inherits from Human class.
    - Method Override: Overrides eat() method from Human.
    """

    def __init__(self, name, origin, dialect):
        """
        Initialize a Chinese object with a name, origin, and dialect.
        """
        super().__init__(name, origin)
        self.dialect = dialect

    def celebrate_imlek(self):
        """
        Simulates the action of celebrating Imlek (Chinese New Year).
        """
        print(f"{self.name} is celebrating Imlek with family and friends.")

    def eat(self):
        """
        Simulates the action of having dim sum for lunch, a Chinese favorite dish.
        - Method Override: Overrides eat() method from Human.
        """
        print(f"{self.name} is having dim sum for lunch.")


class Hakka(Chinese):
    """
    Represents a Hakka Chinese person, inheriting from Chinese.
    - Inheritance: Inherits from Chinese class.
    - Method Override: Overrides eat() method from Chinese.
    """

    def __init__(self, name, origin, dialect):
        """
        Initialize a Hakka object with a name, origin, and dialect.
        """
        super().__init__(name, origin, dialect)

    def celebrate_Hakka_cuisine(self):
        """
        Simulates the action of enjoying Hakka cuisine, known for its distinctive flavors and techniques.
        """
        print(f"{self.name} is savoring authentic Hakka cuisine.")

    def eat(self):
        """
        Overrides the eat method from the parent class to reflect Hakka's dining preferences.
        - Method Override: Overrides eat() method from Chinese.
        """
        print(f"{self.name} is having Hakka-style dishes for dinner.")


class Banyumasan(Javanese):
    """
    Represents a Banyumasan Javanese person, inheriting from Javanese.
    - Inheritance: Inherits from Javanese class.
    """

    def __init__(self, name, origin, favorite_batik, ngapak_skill):
        """
        Initialize a Banyumasan object with a name, origin, favorite batik, and Ngapak speaking skill.
        """
        super().__init__(name, origin, favorite_batik)
        self.ngapak_skill = ngapak_skill

    def speak_ngapak(self):
        """
        Simulates the action of speaking with a Banyumasan accent (Ngapak).
        """
        print(f"{self.name} is speaking with a Banyumasan accent (Ngapak).")


class Surabayan(Javanese):
    """
    Represents a Surabayan Javanese person, inheriting from Javanese.
    - Inheritance: Inherits from Javanese class.
    - Method Override: Overrides eat() method from Javanese.
    """

    def __init__(self, name, origin, favorite_batik, favorite_dish):
        """
        Initialize a Surabayan object with a name, origin, favorite batik, and favorite dish.
        """
        super().__init__(name, origin, favorite_batik)
        self.favorite_dish = favorite_dish

    def eat(self):
        """
        Simulates the action of enjoying their favorite Surabaya delicacy.
        - Method Override: Overrides eat() method from Javanese.
        """
        print(f"{self.name} is enjoying a plate of {self.favorite_dish}, their favorite Surabaya delicacy.")


# Example usage with updated names and values
a_person = Human("Adam","Earth") # main class
print(a_person.name) # Output: Adam
print(a_person.origin) # Output: Earth
java_person = Javanese("Adi", "Indonesia", "Batik Solo")
java_person.eat()  # Output: Adi is enjoying a delicious Gudeg, their favorite food.
java_person.dance()  # Output: Adi is performing a graceful Javanese dance.

banyumas_person = Banyumasan("Budi", "Indonesia", "Batik Banyumas", "Intermediate")
banyumas_person.speak_ngapak()  # Output: Budi is speaking with a Banyumasan accent (Ngapak).
banyumas_person.eat()  # Output: Budi is enjoying a delicious Nasi Liwet, their favorite food.

surabaya_person = Surabayan("Citra", "Indonesia", "Batik Surabaya", "Rujak Cingur")
surabaya_person.eat()  # Output: Citra is enjoying a plate of Rujak Cingur, their favorite Surabaya delicacy.
surabaya_person.dance()  # Output: Citra is performing a graceful Javanese dance.

hakka_person = Hakka("Lin", "Indonesia", "Hakka")
hakka_person.celebrate_imlek()  # Output: Lin is celebrating Imlek with family and friends.
hakka_person.celebrate_Hakka_cuisine()  # Output: Lin is savoring authentic Hakka cuisine.
hakka_person.eat()  # Output: Lin is having Hakka-style dishes for dinner.
