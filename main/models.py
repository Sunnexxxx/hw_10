from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# class Genre(models.Model):
#     genre = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.genre


class Band(models.Model):
    GENRE_CHOICES = [('Rock', 'Rock'),
                     ('Metal', 'Metal'),
                     ('Jazz', 'Jazz'),
                     ('Classical', 'Classical'),
                     ('Blues', 'Blues'),
                     ('Country', 'Country'),
                     ('Hip-Hop', 'Hip-Hop'),
                     ('Pop', 'Pop'),
                     ('R&B', 'R&B'),
                     ('Rap', 'Rap'),
                     ('Reggae', 'Reggae'),
                     ]
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True, max_length=255)

    def __str__(self):
        return f'{self.name} - {self.genre}'

    class Meta:
        ordering = ['genre']

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.genre}')
        super(Band, self).save(force_insert, force_update, using, update_fields)

    def get_absolute_url(self):
        return reverse('band', kwargs={"genre": self.genre, "slug": self.slug})
