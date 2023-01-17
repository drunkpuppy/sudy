from django.db import models
from django.contrib.auth.models import User

article = 'AR'
news = 'NE'

POST_TYPE = [
    (article, 'Статья'),
    (news, 'Новость')
]

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        self.rating = 0
        for comment in Comment.objects.filter(user=self.user):
            self.rating += comment.comment_rating

        for post in Post.objects.filter(author=Author.objects.get(user=self.user)):
            self.rating += post.post_rating * 3
            for comments_to_post in Comment.objects.filter(post=post):
                self.rating += comments_to_post.comment_rating
        self.save()

    def __str__(self):
        return f'Name: {self.user}, Rating: {self.rating}'

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=POST_TYPE)
    data = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64, default='Unnamed')
    text = models.TextField()
    post_rating = models.IntegerField(default=0, db_column='rating')

    category = models.ManyToManyField(Category, through='PostCategory')

    @property
    def rating(self):
        return self.post_rating

    @rating.setter
    def rating(self, value):
        if value >= 0 and isinstance(value, int):
            self.post_rating = value
        else:
            self.post_rating = 0
        self.save()

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[0:124]}...'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0, db_column='rating')

    @property
    def rating(self):
        return self.comment_rating

    @rating.setter
    def rating(self, value):
        if value >= 0 and isinstance(value, int):
            self.comment_rating = value
        else:
            self.comment_rating = 0
        self.save()

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

