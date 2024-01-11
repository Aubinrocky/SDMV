from django.db import models
from django.conf import settings

# Create your models here.


class Sport(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        verbose_name = "sport"
        verbose_name_plural = "3. Sports"

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        verbose_name = "city"
        verbose_name_plural = "4. Cities"

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        verbose_name = "level"
        verbose_name_plural = "5. Levels"

    def __str__(self):
        return self.name


class Tournament(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField(max_length=10000, null=True)
    featured_image = models.ImageField(upload_to="tournoi/featured_images/%Y/%m/%d/")
    is_published = models.BooleanField(default=False)
    date = models.DateField(auto_now=False, null=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    locationLon = models.FloatField(null=True)
    locationLat = models.FloatField(null=True)
    level = models.ManyToManyField(Level)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tournament",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "tournament"
        verbose_name_plural = "6. Tournaments"

    def __str__(self):
        return self.title

    def get_number_of_likes(self):
        return self.likes.count()
