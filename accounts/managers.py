from django.contrib.auth.base_user import BaseUserManager

# Create your managers here


class MemberManager(BaseUserManager):
    use_in_migrations = True

    def _create_member(self, email, password, **extra_fields):
        """
        Creates and saves a Member with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        member = self.model(email=email, **extra_fields)
        member.set_password(password)
        member.save(using=self._db)
        return member

    def create_member(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_member(email, password, **extra_fields)

    def create_supermember(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_member(email, password, **extra_fields)
