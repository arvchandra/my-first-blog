from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.utils import timezone

from blog.forms import PostForm
from blog.models import Post


class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="admin", password="password")

        self.client = Client()
        self.client.login(username="admin", password="password")

        self.client.post('/post/new/', data={"title": "First post", "text": "Test first post"})
        self.client.post('/post/new/', data={"title": "Second post", "text": "Test second post"})
        
    def test_title(self):
        posts = Post.objects.all()
        for post in posts:
            self.assertTrue(len(post.title) < 200)

    def test_created_date(self):
        posts = Post.objects.all()
        for post in posts:
            self.assertTrue(post.published_date is None)