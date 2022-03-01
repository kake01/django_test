from django.db import models
from django.contrib.auth.models import User
        
class Message(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    respond = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'owner='+ str(self.owner) + '(Message:id=' + str(self.id) + ' , '  + 'content=' + self.content + 'respond=' + self.respond + str(self.pub_date) + ' ) '
        
    class Meta:
        ordering = ('pub_date', )




