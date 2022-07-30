from django.test import TestCase

# Create your tests here.

from django.test import TestCase

import my_blog.settings
import os


class AnimalTestCase(TestCase):
    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""

        print(my_blog.settings.STATIC_ROOT)
