from datetime import datetime

from mongoengine.connection import connect
from mongoengine.document import Document
from mongoengine.fields import (
    DateTimeField,
    DictField,
    ListField,
    StringField,
    URLField,
)

connect("ptt-give", host="localhost", port=27007)


class Articles(Document):
    article_id = StringField(primary_key=True)
    article_title = StringField(required=True)
    author = StringField()
    board = StringField()
    content = StringField(required=True)
    date = StringField()
    ip = StringField()
    message_count = DictField()
    messages = ListField(DictField())
    url = URLField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    meta = {"allow_inheritance": True}


# class BlogPost(Document):
#     title = StringField(required=True, max_length=200)
#     posted = DateTimeField(default=datetime.utcnow)
#     tags = ListField(StringField(max_length=50))
#     meta = {'allow_inheritance': True}


# class TextPost(BlogPost):
#     content = StringField(required=True)


# class LinkPost(BlogPost):
#     url = StringField(required=True)


# post1 = TextPost(title='Using MongoEngine', content='See the tutorial')
# post1.tags = ['mongodb', 'mongoengine']
# post1.save()

# post2 = LinkPost(title='MongoEngine Docs', url='hmarr.com/mongoengine')
# post2.tags = ['mongoengine', 'documentation']
# post2.save()

# for post in BlogPost.objects:
#     print('===', post.title, '===')
#     if isinstance(post, TextPost):
#         print(post.content)
#     elif isinstance(post, LinkPost):
#         print('Link:', post.url)

# print(BlogPost.objects.count())
# print(TextPost.objects.count())
# print(LinkPost.objects.count())

# print(BlogPost.objects(tags='mongoengine').count())
# print(BlogPost.objects(tags='mongodb').count())
