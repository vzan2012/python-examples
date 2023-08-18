class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name="anonmy", age=0):
        # if age > 18:
        self.name = name
        self.age = age

    def run(self):
        print(f"{self.name} runs at the age of {str(self.age)}")

    @classmethod
    def adding_things(cls, num1, num2):
        return cls("Addition", num1+num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1+num2


player1 = PlayerCharacter("ABC", 20)
player2 = PlayerCharacter("pl2", 30)
player3 = PlayerCharacter("pl3", 40)
# player4 = PlayerCharacter()

player1.run()
player2.run()
player3.run()

print(player1.name)
print(player2.name)
print(player3.name)
print(type(player3))


print(player1.membership)

player4 = PlayerCharacter.adding_things(6, 5)

print(player4.age)
print(player4.name)
print(player4.adding_things2(7, 8))


# player4.run()
