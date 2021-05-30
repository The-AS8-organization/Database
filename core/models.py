# Importing necessary modules & libraries
import uuid
from django.db import models
from django.contrib.auth.models import User


# Creating Django Models. Each represent a table.
class UserAdditionalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    github_profile = models.URLField(null=True, blank=True)
    discord_username = models.CharField(max_length=100, null=True, blank=True)
    social_link = models.URLField(null=True, blank=True)
    org_task = models.CharField(max_length=100, null=False, blank=False)


    def __str__(self):
        return self.user.username


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    value = models.CharField(max_length=50, null=False, blank=False, unique=True)

    def __str__(self):
        return f"{self.value}"
    
    def save(self, *args, **kwargs):
        self.value = self.value.lower()
        return super(Tag, self).save(*args, **kwargs)


class Organization(models.Model):
    ORGANIZATION_POPULARITY = [
        ('High','High'),
        ('Mid','Mid'),
        ('Low','Low')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    site = models.URLField(unique=True, null=True, blank=True)
    location = models.CharField(max_length=200, null=False, blank=False)
    is_club = models.BooleanField(null=False, blank=False)
    institution = models.CharField(max_length=100, null=True, blank=True)
    popularity = models.CharField(max_length=4, choices=ORGANIZATION_POPULARITY, default='Mid', null=False, blank=False)
    is_active = models.BooleanField(null=False, blank=False)
    related_tag = models.ManyToManyField(Tag, related_name="org_tag", blank=True)

    def __str__(self):
        return f"{self.name} • {self.category}"

    def save(self, *args, **kwargs):
        self.location = self.location.title()
        self.institution = self.institution.title()
        return super(Organization, self).save(*args, **kwargs)


class Initiative(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    date = models.DateField(null=True, blank=True)
    site = models.URLField(null=True, blank=True)
    parent_org = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name="initiative_org", null=True, blank=True)
    related_tag = models.ManyToManyField(Tag, related_name="initiative_tag", blank=True)

    def __str__(self):
        return f"{self.name}"


class Resource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    date = models.DateField(null=True, blank=True)
    link = models.URLField(null=False, blank=False)
    parent_org = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name="post_org", null=True, blank=True)
    followed_initiative = models.ManyToManyField(Initiative, related_name="resource_initiative", blank=True)
    can_display = models.BooleanField(null=False, blank=False)
    related_tag = models.ManyToManyField(Tag, related_name="resource_tag", blank=True)

    def __str__(self):
        return f"{self.platform} • {self.parent_org.name}"


class Consumer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, null=True, blank=True)
    age = models.IntegerField(null=False, blank=False)
    location = models.CharField(max_length=200, null=False, blank=False)
    profession = models.CharField(max_length=200, null=False, blank=False)
    institution = models.CharField(max_length=200, null=False, blank=False)
    social_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.location = self.location.title()
        self.profession = self.profession.lower()
        self.institution = self.institution.title()
        return super(Consumer, self).save(*args, **kwargs)
