from django.db import models

class Task(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  reward = models.CharField(max_length=100)
  penalty = models.CharField(max_length=100)

  def __str__(self):
    return self.name