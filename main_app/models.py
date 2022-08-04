from django.db import models

class Task(models.Model):
  PRIORITY_CHOICES = [
      (1, 'Low'),
      (2, 'Medium'),
      (3, 'High'),
      (4, 'Emergency'),
  ]

  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  reward = models.CharField(max_length=100)
  penalty = models.CharField(max_length=100)

  priority = models.CharField(
    max_length=1,
    choices=PRIORITY_CHOICES,
    default=3,
)

  def __str__(self):
    return self.name