from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()  # Защита от переопределения модели пользователя


class Publications(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)

    description = models.TextField(verbose_name="Описание")

    create_date = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор объявления"
    )

    amount_of_upvotes = models.IntegerField(
        verbose_name="Количество голосов", default=0
    )


class Comments(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор объявления"
    )

    comment = models.TextField(verbose_name="Комментарий")

    create_date = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)

    publication = models.ForeignKey(
        Publications, on_delete=models.CASCADE, verbose_name="Публикация"
    )
