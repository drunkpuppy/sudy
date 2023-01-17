from news.models import *

#1
User.objects.create(username='User1', password='qwerty', first_name='Biba', last_name='Boba', email='biba@somedomain.com')
User.objects.create(username='User2', password='qwerty', first_name='Pupa', last_name='Lupa', email='pupa@otherdomain.ru')

#2
Author.objects.create(user=User.objects.get(username='User1'))
Author.objects.create(user=User.objects.get(username='User2'))

#3
Category.objects.create(name='Checkpoint')
Category.objects.create(name='Forcepoint')
Category.objects.create(name='ASA')
Category.objects.create(name='Firepower')

#4
Post.objects.create(author=Author(pk=1), type='AR', title='Checkpoint is to complex', text='Checkpoint is too complex')
Post.objects.create(author=Author(pk=1), type='AR', title='Firepower or ASA', text='Firepower or ASA')
Post.objects.create(author=Author(pk=2), type='NE', title='Forcepoint', text='Legacy of Stonegate')

#5
PostCategory.objects.create(post = Post.objects.get(pk=1), category = Category.objects.get(name='Checkpoint'))
PostCategory.objects.create(post = Post.objects.get(pk=2), category = Category.objects.get(name='ASA'))
PostCategory.objects.create(post = Post.objects.get(pk=2), category = Category.objects.get(name='Firepower'))
PostCategory.objects.create(post = Post.objects.get(pk=3), category = Category.objects.get(name='Forcepoint'))

#6
Comment.objects.create(post=Post.objects.get(pk=1), user=User.objects.get(username='User1'), text='Beep')
Comment.objects.create(post=Post.objects.get(pk=2), user=User.objects.get(username='User2'), text='Bop')
Comment.objects.create(post=Post.objects.get(pk=3), user=User.objects.get(username='User1'), text='Boop')
Comment.objects.create(post=Post.objects.get(pk=3), user=User.objects.get(username='User2'), text=')))')

#7
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=2).dislike()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=4).dislike()
Post.objects.get(pk=1).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=1).dislike()
Post.objects.get(pk=2).dislike()
Post.objects.get(pk=3).dislike()
Post.objects.get(pk=3).dislike()

#8
Author.objects.get(pk=1).update_rating()
Author.objects.get(pk=2).update_rating()

#9
Author.objects.all().order_by('-rating').values('user', 'rating')[0]

#10
Post.objects.all().order_by('-post_rating').values('data', 'author', 'post_rating', 'title')[0]
best_post = Post.objects.all().order_by('-post_rating')[0]
best_post.preview()

#11
Comment.objects.filter(post=best_post).values('date', 'user', 'comment_rating', 'text')