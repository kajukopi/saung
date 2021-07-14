from django.db import models

# declare a new model with a name "GeeksModel"


class Blog(models.Model):

    # fields of the model
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        db_table = 'blog'
    # renames the instances of the model
    # with their title name

    def __str__(self):
        return self.title
