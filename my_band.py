class Band:

    all = []

    def __init__(self, role , members=[]):
        self.name = name
        self,role = role
        self.members = members
        self.__class__.all.append(self)

    def __repr__(self):
        return f'{self.members} - {self.members}'

    def __str__(self):
        return f'The pack is led by {self.leader}, the members are {self.members}'

    @staticmethod
    def get_band_oath():
        return 'Rocking in the free world'

    @classmethod
    def create_from_data(cls, data):
        """
        Arguments:
            data {[type]} -- [description]
        """


class Musician:

    # class attribute
    musician_list = []

    def __init__(self, name, role):
        self.name = name
        self. role = role
        self.__class__.musician_list.append(self)

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'I am a {self.__class__.__name__} my role is {self.name} in the band'

    @classmethod
    def get_musicians(cls):
        return cls.musician_list


class Guitarist(Musician):

    def __init__(self, name):
        super().__init__(name, 'Guitarist')

    def play_solos(self):
        return 'Cool guitar solo makes you high'


class Bassist(Musician):

    def __init__(self, name):
        super().__init__(name, 'Bassist')

    def play_solos(self):
        return 'Bass solo is a bumbblebee that nails you to the wall'


class Drummer(Musician):

    def __init__(self, name):
        super().__init__(name, 'Drummer')

    def play_solos(self):
        return 'Drum solo is stormy stompy catasphere hurricane catagoria#9 '
