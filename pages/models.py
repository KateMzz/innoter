from django.db import models


class Tag(models.Model):
    """
    Model for representing tags.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    user_id = models.UUIDField(editable=False)
    image_url = models.URLField()
    tags = models.ManyToManyField("Tag", related_name="pages")
    followers = models.ManyToManyField("Followers", related_name="following_pages")
    is_blocked = models.BooleanField(default=False)
    unblock_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Followers(models.Model):
    page_id = models.ForeignKey(Page, on_delete=models.CASCADE)
    user_id = models.UUIDField(editable=False)
