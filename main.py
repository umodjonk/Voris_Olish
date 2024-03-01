class User:
    _name='Bekzod'
    _tel=234567
    card=23545

class Odam(User):
    def __init__(self):
        print(self._name)
        print(self._tel)
        print(self.card)
Odam()