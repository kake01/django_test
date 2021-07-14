from django.db import models

class Message(models.Model):
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    respond = models.CharField(max_length=300)
    pub_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return super().__str__()
    
    class Meta:
        ordering = ('pub_data',)