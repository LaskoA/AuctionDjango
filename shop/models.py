from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=63)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class Lot(models.Model):
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=255)
    category = models.ManyToManyField(Category, related_name="lots")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
