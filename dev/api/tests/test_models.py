import datetime
from ..models import Person
from django.test import TestCase
from typing import List


class PersonModelTest(TestCase):
    """Tests for api.models.Person."""

    def setUp(self) -> None:
        self.test_data: List[dict] = [
            {
                "name": "sanjeev",
                "dob": datetime.date(2001, 9, 16),
                "email": "sanjeev@mail.com",
                "hobby": "singing",
            },
            {
                "name": "rohan",
                "dob": datetime.date(1992, 10, 3),
                "email": "rohan@mail.com",
                "hobby": "trekking",
            },
        ]

    def test_person(self) -> None:
        """Test to check if person unicode value."""
        for person_data in self.test_data:
            person: Person = PersonModelTest._create_person(person_data)

            assert person.name == person_data.get("name")
            assert person.dob == person_data.get("dob")
            assert person.email == person_data.get("email")
            assert person.hobby == person_data.get("hobby")

            assert str(person) == person_data.get("name")
            assert person.get_hobby() == person_data.get("hobby")
            assert person.get_dob() == person_data.get("dob")

    @staticmethod
    def _create_person(person_data: dict) -> Person:
        """ Create a person based on given data in database."""
        name: str = person_data.get("name")
        dob: datetime.date = person_data.get("dob")
        email: str = person_data.get("email")
        hobby: str = person_data.get("hobby")

        return Person.objects.create(name=name, dob=dob, email=email, hobby=hobby)
