from django_blakey_utils.test_utils.tastypie_test import ResourceTestCase as ResourceTestCaseCore
from django.contrib.auth.models import User

import os
import simplejson

class UserMixin:
    """
    Creates a user, saves it to its field.
    """
    user_name = 'dummy-user'
    user_email = 'dummy.user@email.com'
    user_password ='dummy-password'
    def init_user(self, username = user_name, email = user_email, password = user_password):
        if not User.objects.count():
            self.user = User.objects.create_user(username, email, password)
            self.user.save()
        else:
            self.user = User.objects.get_by_natural_key(username)
        return self.user


class ResourceTestCase(ResourceTestCaseCore, UserMixin):
    """
    Base test class for testing TastyPie resources through http requests.
    """
    user_name = 'dummy-user'
    user_password ='dummy-password'

    def setUp(self):
        super(ResourceTestCase, self).setUp()
        self.init_user(username=self.user_name, password=self.user_password)
        self.credentials = self.create_basic(username=self.user_name, password=self.user_password)


class ExternalResources:
    """
    Manages external resource files.
    """
    @classmethod
    def get_json(cls, parent, path):
        assert parent
        assert path
        return simplejson.load(open(os.path.join(parent, path)))

    @classmethod
    def get_content(cls, parent, path):
        assert parent
        assert path
        return open(os.path.join(parent, path)).read()