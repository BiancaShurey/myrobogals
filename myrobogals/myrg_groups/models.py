"""
    myRobogals
    myrg_groups/models.py
    Custom LocatableEntity, Role, RoleClass model definition

    2014
    Robogals Software Team
"""

from django.db import models
from django.core import validators
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from myrg_users.models import RobogalsUser



# Based upon:
# * https://docs.djangoproject.com/en/dev/ref/models/fields/

class Group(models.Model):
    name = models.CharField(_('name'),
                            max_length=63,
                            blank=False)

    creator = models.ForeignKey(RobogalsUser)

    #administrators = models.ManyToManyField(RobogalsUser, limit_choices_to={'is_active': True})
    
    parent = models.ForeignKey('self',
                               null=True,
                               blank=True)

    description = models.TextField(_('description'),
                            blank=True,
                            help_text=_('Description, with HTML support'))
                            
    STATUS_CHOICES = (
        (0, 'Deleted'),
        (1, 'Active, Private, Non-joinable'),
        (2, 'Active, Private, Gated'),
        (3, 'Active, Private, Joinable'),
        (7, 'Active, Public, Non-joinable'),
        (8, 'Active, Public, Gated'),
        (9, 'Active, Public, Joinable'),
    )
    status = models.PositiveSmallIntegerField(_('status'),
                              choices=STATUS_CHOICES,
                              default=0,
                              blank=False)

    date_created = models.DateField(_('date created'),
                                    blank=False,
                                    default=timezone.now)
    
    # Fields that cannot be listed or filtered/sorted with
    PROTECTED_FIELDS = ()

    # Fields that cannot be listed (but can be filtered/sorted with)
    # NONVISIBLE_FIELDS = ()
    
    # Fields that cannot be written to
    READONLY_FIELDS = ("id","date_created",)
    
    
    def get_preferred_name(self):
        """Retrieves the preferred name of the group, for display purposes.
        
        Format:
            <preferred> (where available)
            <given> (otherwise)
        """
        return '{}'.format(self.preferred_name or self.name)
        
    def get_sortable_name(self):
        return self.get_preferred_name(self)
    
    def __str__(self):
        return self.get_preferred_name()
        
class LocatableEntity(Group):
    address = models.TextField(_('address'),
                               blank=False)
    city = models.CharField(_('city'),
                            max_length=63,
                            blank=True)
    state = models.CharField(_('state'),
                             max_length=63,
                             blank=True)
    postcode = models.CharField(_('postcode'),
                                blank=True,
                                max_length=15)
    country = models.CharField(_('country'),
                               max_length=63,
                               blank=False)
    latitude = models.FloatField(_('latitude'),
                                 blank=True,
                                 null=True)
    longitude = models.FloatField(_('longitude'),
                                  blank=True,
                                  null=True)

    timezone = models.CharField(_('timezone'),
                                max_length=63,
                                blank=False,
                                default='Etc/UTC')

    url = models.CharField(_('url'),
                           max_length=255,
                           blank=True)
    class Meta:
        abstract = True
        
class Chapter(LocatableEntity):
    university = models.CharField(_('university'),
                                  max_length=63,
                                  blank=True)

class School(LocatableEntity):
    pass

class Company(LocatableEntity):
    legal_name = models.CharField(_('legal name'),
                                  max_length=63,
                                  blank=True)

class RoleClass(models.Model):
    name = models.CharField(_('name'),
        max_length=63,
        unique=True)

    description = models.TextField(_('description'),
        blank=True,
        help_text=_('Short description of the role class.'))

    group_exclude = models.ManyToManyField(Group,
        related_name='roleclass_exclude',
        blank=True,
        null=True)

    group_include = models.ManyToManyField(Group,
        related_name='roleclass_include',
        blank=True,
        null=True)

    is_active = models.BooleanField(_('active'), default=True)
    
    # Fields that cannot be listed or filtered/sorted with
    PROTECTED_FIELDS = ()

    # Fields that cannot be listed (but can be filtered/sorted with)
    # NONVISIBLE_FIELDS = ()
    
    # Fields that cannot be written to
    READONLY_FIELDS = ("id","is_active")
    
    def __str__(self):
        return self.name

    def get_applicable_groups(self):
        if self.group_include.all():
            applicable_groups = self.group_include.exclude(pk__in = self.group_exclude.all())
        else:
            applicable_groups = Group.objects.exclude(pk__in = self.group_exclude.all())
        return applicable_groups

class Role(models.Model):
    user = models.ForeignKey(RobogalsUser)
    role_class = models.ForeignKey(RoleClass)
    group = models.ForeignKey(Group)

    date_start = models.DateTimeField(_('date start'),
        default=timezone.now)

    date_end = models.DateTimeField(_('date end'),
        blank=True,
        null=True)
    
    # Fields that cannot be listed or filtered/sorted with
    PROTECTED_FIELDS = ()

    # Fields that cannot be listed (but can be filtered/sorted with)
    # NONVISIBLE_FIELDS = ()
    
    # Fields that cannot be written to
    READONLY_FIELDS = ("id")




