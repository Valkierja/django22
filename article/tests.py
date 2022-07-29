from django.test import TestCase

# Create your tests here.

from django.test import TestCase

import my_blog.settings
import os


class AnimalTestCase(TestCase):
    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        self.assertEqual(my_blog.settings.SECRET_KEY, os.environ["SECRET_KEY"])
        print("BASE_DIR is: " + my_blog.settings.BASE_DIR)
