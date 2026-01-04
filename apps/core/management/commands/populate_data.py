
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.blog.models import Post, Category, Tag, Comment
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write("Creating sample data...")
        
        # Create user
        user, created = User.objects.get_or_create(username="admin", email="admin@example.com")
        if created:
            user.set_password("admin")
            user.save()
            self.stdout.write("Created superuser: admin/admin")
        
        # Categories
        categories = ["Technology", "Design", "Life", "Travel"]
        cats = [Category.objects.get_or_create(name=c)[0] for c in categories]
        
        # Tags
        tags = ["django", "unpoly", "python", "webdev", "ui/ux"]
        ts = [Tag.objects.get_or_create(name=t)[0] for t in tags]
        
        # Posts
        for i in range(15):
            post = Post.objects.create(
                title=f"Sample Post {i+1}",
                content=f"This is the content for sample post {i+1}. It is very interesting and demonstrates Unpoly capabilities. " * 5,
                author=user,
                category=random.choice(cats)
            )
            post.tags.set(random.sample(ts, 2))
            
            # Comments
            Comment.objects.create(post=post, author=user, content=f"Great post {i+1}!")
        
        self.stdout.write(self.style.SUCCESS("Successfully populated data"))
