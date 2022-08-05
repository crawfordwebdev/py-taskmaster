from django.db import models
from django.urls import reverse

PRIORITY = (
  ('0', 'None'),
  ('1', 'Low'),
  ('2', 'Medium'),
  ('3', 'High'),
  ('4', 'Emergency')
)

class Task(models.Model):
  date = models.DateField(blank=True),
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  reward = models.CharField(max_length=100)
  penalty = models.CharField(max_length=100)
  priority = models.CharField(
    max_length=1,
    choices=PRIORITY,
    # set the default value for priority to 0 or None
    default=PRIORITY[0][0]
  )

  def __str__(self):
    return self.name 

  def get_absolute_url(self):
    return reverse('tasks_detail', kwargs={'task_id': self.id})