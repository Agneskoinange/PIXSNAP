from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.save()


# iterable tuple to use as choices of category field


ORDER_CHOICES = (
    ('11', 'Vegetation'),
    ('12', 'Trees'),
    ('13', 'Nature'),
    ('14', 'Abstract'),
    ('15', 'IT & Computers'),
    ('16', 'Animals'),
    ('17', 'Illustrations'),
    ('18', 'Arts'),
    ('19', 'Business'),
    ('20', 'Industries'),
    ('21', 'Objects'),
    ('22', 'Technology'),
    ('23', 'People'),
    ('24', 'Travel'),
)


class Category(models.Model):
    name = models.CharField(max_length=30)
    category_choices = models.CharField(max_length=10, choices=ORDER_CHOICES)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_catgory(self):
        self.save()


class Image(models.Model):
    image_name = models.CharField(max_length=20)
    image_description = models.CharField(max_length=30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/', null="True", blank="True")

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls, search_term):
        app = cls.objects.filter(category__name__icontains=search_term)
        return app

  
    @classmethod
    def filter_by_location(cls):
        app = cls.objects.filter(
            location__name__icontains='Silicon Valley')
        return app

    class Meta:
        ordering = ['image_name']