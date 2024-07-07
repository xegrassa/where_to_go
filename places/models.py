from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField("Название", max_length=255)
    short_description = models.TextField("Короткое описание", blank=True)
    long_description = HTMLField("Длинное описание", blank=True)
    longitude = models.FloatField("Долгота")
    latitude = models.FloatField("Широта")

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField("Файл картинки")
    _order = models.PositiveSmallIntegerField("Позиция", default=0, blank=True, db_index=True)

    def save(self, *args, **kwargs):

        if not self.id:
            max_order = Image.objects.filter(place_id=self.place.id).aggregate(max_order=models.Max("_order"))[
                "max_order"
            ]
            if max_order is not None:
                self._order = max_order + 1
            else:
                self._order = 1

        super().save(*args, **kwargs)

    class Meta(object):
        ordering = ["_order"]

    def __str__(self):
        return f"{self._order} {self.place}"
