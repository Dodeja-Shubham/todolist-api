from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    home = 'Home'
    personal = 'Personal'
    work = 'Work'
    fitness = 'Fitness'
    medication = 'Medication'
    categories = [
        (home, 'Home'),
        (personal, 'Personal'),
        (work, 'Work'),
        (fitness, 'Fitness'),
        (medication, 'Medication'),
    ]
    category = models.CharField(max_length=10, choices=categories, default=1)
    title = models.CharField(max_length=150)
    due_date = models.DateField(null=True, blank=True)
    desc = models.TextField(null= True)
    colour = models.CharField(max_length=7)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return (self.title)

    class Meta:
        ordering = ('id',)