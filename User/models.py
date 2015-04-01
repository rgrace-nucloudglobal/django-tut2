from django.db import models
from django.contrib.auth.models import User, UserManager
from django.template.defaultfilters import default

class User2(User):
    #     teddy_bear = 't'
    #     doll = 'd'
    #     car = 'c'
    #     boat = 'b'
    # favorite_childhood_toy_choices = ((t: 'Teddy Bear'), (d: 'Doll'), (c:
    # 'Car'), (b: 'Boat'))
#     , choices=('t', 'Teddy Bear'), ('d', 'Doll'), ('c', 'Car'), ('b', 'Boat')
    favorite_childhood_toy = models.CharField(max_length=100, blank=True)
    do_you_love_your_mommy = models.BooleanField(default=False)
