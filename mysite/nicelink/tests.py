from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import IntegrityError


from .models.Link import Link
from .models.User import UserModel

def user_login(self):
    response = self.client.post(reverse('nicelink:register_view'), {
        'username': 'Polak', 'password': 'Warszawa', 'confirm_password': 'Warszawa', 'email': 'pl@wp.pl',
        'first_name': 'Polak P'
    })
    response = self.client.post(reverse('nicelink:login_view'), {'username': 'Polak', 'password': 'Warszawa'})
    self.assertEqual(response.status_code, 200)


class LinkViewModelTest(TestCase):

    def test_add_link_form_view(self):
        user_login(self)
        link_count = Link.objects.count()
        response = self.client.post(reverse('nicelink:index'), {
            'oryginal_link':'https://docs.djangoproject.com/en/1.11/topics/testing/tools/'
        })
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Link.objects.count(), link_count +1)
        # self.assertTrue('localhost:8000/nicelink' in response.content)
        #assert 'Link generated' in str(response.context)

    def test_add_multiple_nice_links_to_db(self):
        for i in range(0,10):
            link_count = Link.objects.count()
            response = self.client.post(reverse('nicelink:index'), {
                'oryginal_link': 'https://docs.djangoproject.com/en/1.11/topics/testing/tools/'
            })
            # print(response.content)
            self.assertEqual(response.status_code, 200)
            # self.assertEqual(Link.objects.count(), link_count + 1)


class NiceLinkListTest(TestCase):

    def test_link_list(self):
        user_login(self)
        for i in range(0,10):
            link_count = Link.objects.count()
            response = self.client.post(reverse('nicelink:index'), {
                'oryginal_link': 'https://docs.djangoproject.com/en/1.11/topics/testing/tools/'
            })
            # print(response.content)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(Link.objects.count(), link_count + 1)
        response = self.client.get(reverse('nicelink:link_list'))
        self.assertEqual(response.status_code, 200)


class UserTest(TestCase):

    def test_add_user(self):
        user_count = User.objects.count()
        response = self.client.post(reverse('nicelink:register_view'), {
            'username':'Polak', 'password':'Warszawa','confirm_password':'Warszawa','email':'pl@wp.pl','first_name':'Polak P'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), user_count + 1)

    def test_add_equal_user(self):
        user_count = User.objects.count()
        response = self.client.post(reverse('nicelink:register_view'), {
            'username':'Polak', 'password':'Warszawa','confirm_password':'Warszawa','email':'pl@wp.pl','first_name':'Polak P'
        })
        response = self.client.post(reverse('nicelink:register_view'), {
            'username': 'Polak', 'password': 'Warszawa', 'confirm_password': 'Warszawa', 'email': 'pl@wp.pl',
            'first_name': 'Polak P'
        })
        self.assertRaises(IntegrityError)

    def test_user_login(self):
        user_login(self)
























