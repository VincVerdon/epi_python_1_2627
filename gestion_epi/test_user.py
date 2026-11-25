'''!
@author: N.Carree
@version: 20261119
'''

import unittest
from model.User import User


class TestUser(unittest.TestCase):
    '''!
    Tests unitaires de la classe métier User
    '''

    def test_init_and_getters(self):
        user = User("Jean", "Dupont", "jdupont", "secret123", 1)
        self.assertEqual(user.getId(), 1)
        self.assertEqual(user.getFirstName(), "Jean")
        self.assertEqual(user.getLastName(), "Dupont")
        self.assertEqual(user.getLogin(), "jdupont")
        self.assertEqual(user.getPassword(), "secret123")

    def test_setters(self):
        user = User()
        user.setId(42)
        user.setFirstName("Alice")
        user.setLastName("Martin")
        user.setLogin("amartin")
        user.setPassword("motdepasse")

        self.assertEqual(user.getId(), 42)
        self.assertEqual(user.getFirstName(), "Alice")
        self.assertEqual(user.getLastName(), "Martin")
        self.assertEqual(user.getLogin(), "amartin")
        self.assertEqual(user.getPassword(), "motdepasse")


if __name__ == "__main__":
    unittest.main()