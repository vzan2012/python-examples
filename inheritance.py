''' Inheritance Example '''


class User():
    # def __init__(self, email):
    #     self.email = email

    def sign_in(self):
        print("Logged In")

    def attack(self):
        print("Nothing")


class Wizard(User):
    # def __init__(self, name, power, email):
    # super().__init__(email)
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def attack(self):
        # User.attack(self)
        print(f'Attacking with the power of {self._power}')


class Archer(User):
    # def __init__(self, name, num_arrows, email):
    #     super().__init__(email)
    def __init__(self, name, num_arrows):
        self._name = name
        self._num_arrows = num_arrows

    def check_arrows(self):
        print(f"{self._num_arrows} remaining")

    def attack(self):
        print(f'Attacking with arrows number of {self._num_arrows}')

    def run(self):
        print("Archer running fast")


# user1 = User("email")
user1 = User()
# wizard1 = Wizard("Wiz", 60, "wiz_email")
wizard1 = Wizard("Wiz", 60)
# archer1 = Archer("Robin", 5, "arc_email")
archer1 = Archer("Robin", 5)

# user1.sign_in()
# wizard1.sign_in()
# archer1.sign_in()

# user1.attack()
# wizard1.attack()
# archer1.attack()


def player_attack(char):
    char.attack()


# player_attack(user1)
# player_attack(wizard1)
# player_attack(archer1)


def users_attack(chars):
    for char in chars:
        char.attack()

# Example for Multiple Inheritance


class Robot(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


users_attack([user1, archer1, wizard1])

# print(wizard1.email)
# print(archer1.email)

print(isinstance(wizard1, User))
print(isinstance(wizard1, object))
print(isinstance(archer1, User))

print(dir(User))
print("---")
print(dir(wizard1))
print("---")
print(dir(archer1))


r1 = Robot("GRobot", 99, 150)

r1.run()
r1.check_arrows()
r1.attack()
r1.sign_in()
