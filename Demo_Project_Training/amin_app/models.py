from django.db import models

class amin_app(models.Model):
    amin_icon = models.CharField(max_length=100)
    amin_title = models.CharField(max_length=100)
    amin_discription = models.TextField(max_length=100)

    def __str__(self):
        return self.amin_title
