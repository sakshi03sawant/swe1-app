from django.apps import apps
from django.conf import settings
from django.test import SimpleTestCase


class ProjectSmokeTests(SimpleTestCase):
    def test_secret_key_exists(self):
        self.assertTrue(settings.SECRET_KEY)

    def test_apps_are_loaded(self):
        self.assertGreater(len(list(apps.get_app_configs())), 0)

    def test_debug_is_boolean(self):
        self.assertIsInstance(settings.DEBUG, bool)

    def test_polls_app_is_installed(self):
        self.assertTrue(apps.is_installed("polls"))

    def test_dummy(self):
        self.assertTrue(False)


# Create your tests here.
