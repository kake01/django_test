from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=300)
    progress = models.PositiveSmallIntegerField()
    pub_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'owner='+ str(self.owner) + \
        '(title=' + str(self.title) + \
        ' , '  + 'contents=' + self.contents + 'progress=' + self.progress + \
            ' pub_date: ' + str(self.pub_date) + ' ) '

    class Meta:
        ordering = ('pub_data',)