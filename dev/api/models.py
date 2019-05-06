import datetime
from django.db import models


class Person(models.Model):
    """Represents a person in the game.

    Attributes:
        name (str): Name of the person.
        dob (date): Date of birth of the person
        email (str): Email of the person
        hobby (str): Hobby of the person
        created_at (date): Time at which this model was created
        updated_at (date): Time at which this model was last updated
    """

    name = models.CharField(max_length=12)
    dob = models.DateTimeField()
    email = models.EmailField()
    hobby = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_hobby(self) -> str:
        """Fetches the hobby of the person.

        Returns:
            Hobby of the person.
        """
        return str(self.hobby)

    def get_dob(self) -> datetime.date:
        """Fetches the date of birth of the person.

        Returns:
            Date of birth of the person.
        """
        return self.dob

    def __str__(self) -> str:
        """Returns the name of the person.

        Returns:
            Name of the person.
        """
        return str(self.name)
