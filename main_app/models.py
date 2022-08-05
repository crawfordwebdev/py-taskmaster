from django.db import models
from django.urls import reverse

PRIORITY = (
  ('0', 'None'),
  ('1', 'Low'),
  ('2', 'Medium'),
  ('3', 'High'),
  ('4', 'Emergency')
)

class Reward(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('reward_detail', kwargs={'pk': self.id})

class Penalty(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('penalty_detail', kwargs={'pk': self.id})

class Task(models.Model):
  date = models.DateField(blank=True),
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  reward = models.ManyToManyField(Reward, blank=True)
  penalty = models.ManyToManyField(Penalty, blank=True)
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

  def get_priority(self):
    return f"{self.get_priority_display()}"



