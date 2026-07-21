from django.db import models



class Blog(models.Model):
    # заголовок,
    # содержимое,
    # превью(изображение),
    # дата
    # создания,
    # признак
    # публикации(булевое
    # поле),
    # количество
    # просмотров.

    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",

    )
    content = models.TextField( blank=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="media/media", blank=True, null=True, verbose_name="Изображение"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    is_published = models.BooleanField(
        "Признак публикации",
        default=False,
    )
    views_count = models.PositiveIntegerField(
        "Количество просмотров",
        default=0,
    )

    class Meta:
        verbose_name = "посты"
        verbose_name_plural = "посты"
        ordering = ["-created_at"]  # сортировка по дате создания (новые сверху)

    def __str__(self):
        return self.title

