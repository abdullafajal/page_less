
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, Category, Tag, Comment

User = get_user_model()

class BlogModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.category = Category.objects.create(name="Tech")
        self.tag = Tag.objects.create(name="Django")
        self.post = Post.objects.create(
            title="Hello World",
            author=self.user,
            content="This is a test post.",
            category=self.category
        )
        self.post.tags.add(self.tag)

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Hello World")
        self.assertEqual(self.post.slug, "hello-world")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.category.name, "Tech")
        self.assertEqual(self.post.tags.first().name, "Django")

    def test_comment_creation(self):
        comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content="Great post!"
        )
        self.assertEqual(comment.content, "Great post!")
        self.assertEqual(self.post.comments.count(), 1)
