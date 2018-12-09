from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import MemberManager
import datetime
# Create your models here.


class Member(AbstractBaseUser, PermissionsMixin):
  TYPE = (
    ('T', 'Tech'),
    ('B', 'Builder'),
    ('O', 'Other'),
  )

  #'username', 'first_name', 'last_name',
  #'email', 'date_of_birth', 'graduation_year',
  #'specialized', 'password'
  username = models.CharField(_('username'), help_text="Your username", unique=True, max_length=20)
  email = models.CharField(_('email'), help_text="Your email", unique=True, max_length=40)
  first_name = models.CharField(_('first name'), help_text="Your first name", max_length=30)
  last_name = models.CharField(_('last name'), help_text="Your last name", max_length=30)
  date_of_birth = models.DateField(_('date of birth'), help_text="Your birth (MM/DD/YYYY)")
  date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
  is_staff = models.BooleanField(_('staff'), default=False)
  is_active = models.BooleanField(_('active'), default=True)
  graduation_year = models.PositiveIntegerField(_('graduation year'), help_text="Your expected graduation year", default=datetime.date.today().year)
  specialized = models.CharField(_('Type'), max_length=1, choices=TYPE, default="O")
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'password']

  objects = MemberManager()

  class Meta:
    verbose_name = _('user')
    verbose_name_plural = _('users')
  @property
  def age(self):
    today = datetime.datetime.utcnow()
    age = today - self.date_of_birth
    return age

  def get_full_name(self):
    '''
    Returns the first_name plus the last_name, with a space in between.
    '''
    full_name = '%s %s' % (self.first_name, self.last_name)
    return full_name.strip()

  def get_short_name(self):
    '''
    Returns the short name for the user.
    '''
    return self.first_name

  def email_user(self, subject, message, from_email=None, **kwargs):
    '''
    Sends an email to this User.
    '''
    send_mail(subject, message, from_email, [self.email], **kwargs)


class SuperAdmin(Member):
  pass
