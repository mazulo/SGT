from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
from django.core import validators

from sgt.core.models import Unidade


class UserDbvManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Usuários devem ter um endereço de email')
        if not username:
            raise ValueError('Usuários devem ter um nome de usuário')

        user = self.model(username=username, email=self.normalize_email(email))
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user


CARGO_CHOICES = (
    ('CSO', 'Conselheiro(a)'),
    ('CPT', 'Capit(ã)o'),
    ('SCT', 'Secretário(a)'),
    ('TSR', 'Tesoureiro(a)'),
    ('INS', 'Instrutor(a)'),
    ('DRT', 'Diretor(a)'),
    ('DRT_AS', 'Diretor(a) Associado(a)'),
    ('CPL', 'Capel(ã)o'),
)


class UserDbv(AbstractBaseUser, PermissionsMixin):

    # The basic fields of the user
    username = models.CharField(
        'Nome de Usuário',
        max_length=30,
        unique=True,
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                (
                    'Enter a valid username. This value may contain only ',
                    'letters, numbers ' 'and @/./+/-/_ characters.'
                )
            ),
        ],
    )
    email = models.EmailField('E-mail', unique=True)
    first_name = models.CharField(
        'Primeiro Nome',
        null=True,
        blank=True,
        max_length=50
    )
    last_name = models.CharField(
        'Segundo Nome',
        null=True,
        blank=True,
        max_length=50
    )
    date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)
    is_active = models.BooleanField('Está ativo?', null=False, default=True)
    is_staff = models.BooleanField('É da equipe?', null=False, default=False)
    is_admin = models.BooleanField('É admin?', default=False)

    # My own fields
    age = models.IntegerField(default=10)
    profile_image = models.ImageField(
        upload_to='dbv_profile_images', blank=True
    )
    group = models.ForeignKey(Unidade, related_name='desbravadores', null=True)
    position = models.CharField(max_length=100, choices=CARGO_CHOICES)

    objects = UserDbvManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
