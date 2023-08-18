''' Inheritance Example '''


class User():
    def sign_in(self):
        print("Logged In")

    def attack(self):
        print("Nothing")


class Wizard(User):
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def attack(self):
        print(f'Attacking with the power of {self._power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self._name = name
        self._num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows number of {self._num_arrows}')


user1 = User()
wizard1 = Wizard("Wiz", 60)
archer1 = Archer("Robin", 5)

# user1.sign_in()
# wizard1.sign_in()
# archer1.sign_in()

user1.attack()
wizard1.attack()
archer1.attack()
