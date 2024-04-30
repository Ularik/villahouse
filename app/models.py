from django.db import models
from django.contrib.auth import get_user_model
import uuid
User = get_user_model()


class Category(models.Model):
    title = models.CharField(
        max_length=123
    )

    def __str__(self):
        return self.title


class House(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    address = models.CharField(
        max_length=123
    )
    region = models.CharField(
        max_length=123
    )
    post_code = models.CharField(
        max_length=55
    )
    image = models.ImageField(
        upload_to='villa/'
    )
    area = models.CharField(
        max_length=17
    )
    floor = models.PositiveSmallIntegerField()
    bedrooms = models.PositiveSmallIntegerField()
    bathrooms = models.PositiveSmallIntegerField()
    parking_lot = models.PositiveSmallIntegerField()
    description = models.TextField()
    is_security = models.BooleanField(
        default=True
    )
    authorization_type = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Красная книга'),
            (2, 'Зелёная книга'),
            (3, 'Белая книга'),
            (4, 'В аренду')
        )
    )
    payment = models.ForeignKey(
        'MethodPayment',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00
    )
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    updated_date = models.DateTimeField(
        auto_now=True
    )
    is_active = models.BooleanField(
        default=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = str(uuid.uuid4())[:6]
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.address}, {self.region}, {self.post_code}'


class MethodPayment(models.Model):
    title = models.CharField(
        max_length=123
    )

    def __str__(self):
        return self.title


class Storage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'В процессе'),
            (2, 'Одобрено'),
        ),
        default=1
    )

    def save(self, *args, **kwargs):
        house = self.house
        if house.is_active == True:
            house.is_active = False
            house.save()
        return super().save(*args, **kwargs)

