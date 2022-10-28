# cards/models.py

from pyexpat import model
from django.db import models


NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

class Card(models.Model):

    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0]
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    def move(self, solved):
        next_box = self.box+1 if solved else BOXES[0]
        if next_box in BOXES:
            self.box = next_box
            self.save()
        return self