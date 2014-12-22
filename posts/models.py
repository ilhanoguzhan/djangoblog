from django.db import models
from django_fsm import FSMField, transition

# Create your models here.

class Post(models.Model):

    state = FSMField(default='new')

    post_text = models.TextField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

    @transition(field=state, source='*', target='published')
    def publish(self):
        self.state = 'published'
        self.save()

    @transition(field=state, source='published', target='unpublished')
    def unpublish(self):
        self.state = 'unpublished'
        self.save()



