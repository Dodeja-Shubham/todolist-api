from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoItem(models.Model):
    # home = 'Home'
    # personal = 'Personal'
    # work = 'Work'
    # fitness = 'Fitness'
    # medication = 'Medication'
    # categories = [
    #     (home, 'Home'),
    #     (personal, 'Personal'),
    #     (work, 'Work'),
    #     (fitness, 'Fitness'),
    #     (medication, 'Medication'),
    # ]
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="todolist", null=True)
    category = models.CharField(max_length=100, default=1)
    title = models.CharField(max_length=150, null=True)
    due_date = models.DateField(null=True, blank=True)
    desc = models.TextField(null= True)
    colour = models.CharField(max_length=7, null= True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return (self.title)

    class Meta:
        ordering = ('id',)