from ..models import Person
from django.test import TestCase


class PersonModelTest(TestCase):
    def create_person(self, name: str, age: str, email: str):
        """ Create a person based on given data in database."""
        return Person.objects.create(name=name, age=age, email=email)

    def test_person_unicode(self):
        """Test to check if person unicode value."""
        person = self.create_person("saurabh", 24, "saurabh@rautela.dev")
        self.assertEqual(p.__unicode__(), person.name)
