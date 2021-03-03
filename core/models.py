from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    """ Time Stamped Model Definition"""

    created = models.DateTimeField(auto_now_add=True) #auto_now_add => django knows when 
    # it is created
    updated = models.DateTimeField(auto_now=True)
    #everytime I save my model, I get a new datetime.

    #abstract model = model but not seen in the DB.
    #used to extend other model using itself
    class Meta:
        abstract = True