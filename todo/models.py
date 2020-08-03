from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)#عشان لو عايزها بلانك فاضيه
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)#عشان لو مش عايز تكتب فيه حاجه ميجيش وارننج
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): #لازم str  كلها سمال 
        return self.title #عشان تبين اسم الاوبجيت فالادمن
