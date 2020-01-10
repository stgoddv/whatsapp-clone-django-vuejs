import os
from django.core.cache import cache
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.urls import reverse
from django.test import TestCase

from friends.exceptions import AlreadyExistsError, AlreadyFriendsError
from friends.models import Friend, Follow, FriendshipRequest, Block


User = get_user_model()


class login(object):
    def __init__(self, testcase, user, password):
        self.testcase = testcase
        success = testcase.client.login(username=user, password=password)
        self.testcase.assertTrue(
            success, "login with username=%r, password=%r failed" % (
                user, password)
        )

    def __enter__(self):
        pass

    def __exit__(self, *args):
        self.testcase.client.logout()


class BaseTestCase(TestCase):
    def setUp(self):
        """
        Setup some initial users
        """
        self.user_pw = "test"
        self.user_bob = self.create_user("bob", "bob@bob.com", self.user_pw)
        self.user_steve = self.create_user(
            "steve", "steve@steve.com", self.user_pw)
        self.user_susan = self.create_user(
            "susan", "susan@susan.com", self.user_pw)
        self.user_amy = self.create_user(
            "amy", "amy@amy.amy.com", self.user_pw)
        cache.clear()

    def tearDown(self):
        cache.clear()
        self.client.logout()

    def login(self, user, password):
        return login(self, user, password)

    def create_user(self, username, email_address, password):
        user = User.objects.create_user(username, email_address, password)
        return user

    def assertResponse200(self, response):
        self.assertEqual(response.status_code, 200)

    def assertResponse302(self, response):
        self.assertEqual(response.status_code, 302)

    def assertResponse403(self, response):
        self.assertEqual(response.status_code, 403)

    def assertResponse404(self, response):
        self.assertEqual(response.status_code, 404)


class FriendshipModelTests(BaseTestCase):
    def test_friendship_request(self):
        # Bob wants to be friends with Steve
        req1 = Friend.objects.add_friend(self.user_bob, self.user_steve)

        # Ensure that the request can be sent
        self.assertFalse(Friend.objects.can_request_send(
            self.user_bob, self.user_bob))
        self.assertTrue(Friend.objects.can_request_send(
            self.user_bob, self.user_steve))

        # Ensure neither have friends already
        self.assertEqual(Friend.objects.friends(self.user_bob), [])
        self.assertEqual(Friend.objects.friends(self.user_steve), [])

        # Ensure FriendshipRequest is created
        self.assertEqual(
            FriendshipRequest.objects.filter(
                from_user=self.user_bob).count(), 1
        )
        self.assertEqual(
            FriendshipRequest.objects.filter(
                to_user=self.user_steve).count(), 1
        )
        self.assertEqual(
            Friend.objects.unread_request_count(self.user_steve), 1)

        # Ensure the proper sides have requests or not
        self.assertEqual(len(Friend.objects.requests(self.user_bob)), 0)
        self.assertEqual(len(Friend.objects.requests(self.user_steve)), 1)
        self.assertEqual(len(Friend.objects.sent_requests(self.user_bob)), 1)
        self.assertEqual(len(Friend.objects.sent_requests(self.user_steve)), 0)

        self.assertEqual(
            len(Friend.objects.unread_requests(self.user_steve)), 1)
        self.assertEqual(
            Friend.objects.unread_request_count(self.user_steve), 1)

        self.assertEqual(
            len(Friend.objects.rejected_requests(self.user_steve)), 0)

        self.assertEqual(
            len(Friend.objects.unrejected_requests(self.user_steve)), 1)
        self.assertEqual(
            Friend.objects.unrejected_request_count(self.user_steve), 1)

        # Ensure they aren't friends at this point
        self.assertFalse(Friend.objects.are_friends(
            self.user_bob, self.user_steve))

        # Accept the request
        req1.accept()

        # Ensure neither have pending requests
        self.assertEqual(
            FriendshipRequest.objects.filter(
                from_user=self.user_bob).count(), 0
        )
        self.assertEqual(
            FriendshipRequest.objects.filter(
                to_user=self.user_steve).count(), 0
        )

        # Ensure both are in each other's friend lists
        self.assertEqual(Friend.objects.friends(
            self.user_bob), [self.user_steve])
        self.assertEqual(Friend.objects.friends(
            self.user_steve), [self.user_bob])
        self.assertTrue(Friend.objects.are_friends(
            self.user_bob, self.user_steve))

        # Make sure we can remove friendship
        self.assertTrue(Friend.objects.remove_friend(
            self.user_bob, self.user_steve))
        self.assertFalse(Friend.objects.are_friends(
            self.user_bob, self.user_steve))
        self.assertFalse(Friend.objects.remove_friend(
            self.user_bob, self.user_steve))

        # Susan wants to be friends with Amy, but cancels it
        req2 = Friend.objects.add_friend(self.user_susan, self.user_amy)
        self.assertEqual(Friend.objects.friends(self.user_susan), [])
        self.assertEqual(Friend.objects.friends(self.user_amy), [])
        req2.cancel()
        self.assertEqual(Friend.objects.requests(self.user_susan), [])
        self.assertEqual(Friend.objects.requests(self.user_amy), [])

        # Susan wants to be friends with Amy, but Amy rejects it
        req3 = Friend.objects.add_friend(self.user_susan, self.user_amy)
        self.assertEqual(Friend.objects.friends(self.user_susan), [])
        self.assertEqual(Friend.objects.friends(self.user_amy), [])
        req3.reject()

        # Duplicated requests raise a more specific subclass of IntegrityError.
        with self.assertRaises(AlreadyExistsError):
            Friend.objects.add_friend(self.user_susan, self.user_amy)

        self.assertFalse(Friend.objects.are_friends(
            self.user_susan, self.user_amy))
        self.assertEqual(
            len(Friend.objects.rejected_requests(self.user_amy)), 1)
        self.assertEqual(
            len(Friend.objects.rejected_requests(self.user_amy)), 1)

        # let's try that again..
        req3.delete()

        # Susan wants to be friends with Amy, and Amy reads it
        req4 = Friend.objects.add_friend(self.user_susan, self.user_amy)
        req4.mark_viewed()

        self.assertFalse(Friend.objects.are_friends(
            self.user_susan, self.user_amy))
        self.assertEqual(len(Friend.objects.read_requests(self.user_amy)), 1)

        # Ensure we can't be friends with ourselves
        with self.assertRaises(ValidationError):
            Friend.objects.add_friend(self.user_bob, self.user_bob)

        # Ensure we can't do it manually either
        with self.assertRaises(ValidationError):
            Friend.objects.create(to_user=self.user_bob,
                                  from_user=self.user_bob)

    def test_already_friends_with_request(self):
        # Make Bob and Steve friends
        req = Friend.objects.add_friend(self.user_bob, self.user_steve)
        req.accept()

        with self.assertRaises(AlreadyFriendsError):
            req2 = Friend.objects.add_friend(self.user_bob, self.user_steve)

    def test_multiple_friendship_requests(self):
        """ Ensure multiple friendship requests are handled properly """
        # Bob wants to be friends with Steve
        req1 = Friend.objects.add_friend(self.user_bob, self.user_steve)

        # Ensure neither have friends already
        self.assertEqual(Friend.objects.friends(self.user_bob), [])
        self.assertEqual(Friend.objects.friends(self.user_steve), [])

        # Ensure FriendshipRequest is created
        self.assertEqual(
            FriendshipRequest.objects.filter(
                from_user=self.user_bob).count(), 1
        )
        self.assertEqual(
            FriendshipRequest.objects.filter(
                to_user=self.user_steve).count(), 1
        )
        self.assertEqual(
            Friend.objects.unread_request_count(self.user_steve), 1)

        # Steve also wants to be friends with Bob before Bob replies
        req2 = Friend.objects.add_friend(self.user_steve, self.user_bob)

        # Ensure they aren't friends at this point
        self.assertFalse(Friend.objects.are_friends(
            self.user_bob, self.user_steve))

        # Accept the request
        req1.accept()

        # Ensure neither have pending requests
        self.assertEqual(
            FriendshipRequest.objects.filter(
                from_user=self.user_bob).count(), 0
        )
        self.assertEqual(
            FriendshipRequest.objects.filter(
                to_user=self.user_steve).count(), 0
        )
        self.assertEqual(
            FriendshipRequest.objects.filter(
                from_user=self.user_steve).count(), 0
        )
        self.assertEqual(
            FriendshipRequest.objects.filter(to_user=self.user_bob).count(), 0
        )

    def test_multiple_calls_add_friend(self):
        """ Ensure multiple calls with same friends, but different message works as expected """
        req1 = Friend.objects.add_friend(
            self.user_bob, self.user_steve, message="Testing"
        )

        with self.assertRaises(AlreadyExistsError):
            req2 = Friend.objects.add_friend(
                self.user_bob, self.user_steve, message="Foo Bar"
            )
