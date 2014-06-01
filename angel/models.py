from django.db import models
from django.utils import timezone


class LogModel(models.Model):
    """base model for tracking changes on a model"""
    ### Logging
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    ### Meta
    class Meta:
        abstract = True


class BaseModel(LogModel):
    """base model most other models inherit from"""
    name = models.CharField(max_length=256, blank=True, help_text='name for this object')

    ### Flags
    active = models.BooleanField(default=True, help_text='field to enable/disable object')

    ### Meta
    class Meta:
        abstract = True
        ordering = ('name', )

    ###
    ### Properties
    ###

    @property
    def NOW(self):
        """returns a properly timezoned value for right now"""
        return timezone.localtime(timezone.now())

    ###
    ### Functions
    ###

    def __unicode__(self):
        return self.name