from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class About(models.Model):
    full_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='about/')
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    rezume = models.FileField(upload_to='cv/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"About - {self.full_name}"


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('soft', 'Soft Skill'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(default=0)
    icon = models.ImageField(upload_to='skill_icons/', blank=True, null=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='soft')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    DEGREE_CHOICES = [
        ('bachelor', 'Bakalavr'),
        ('master', 'Magistr'),
        ('course', 'Kurs'),
        ('bootcamp', 'Bootcamp'),
        ('certificate', 'Sertifikat'),
        ('other', 'Boshqa'),
    ]

    degree = models.CharField(max_length=20, choices=DEGREE_CHOICES)
    institution = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    diploma_file = models.FileField(upload_to='education/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.institution} - {self.get_degree_display()}"


class Experience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.position} at {self.company}"


class Work(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='work_images/', blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)
    source_code = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class BlogArticle(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    content = CKEditor5Field('Content')

    class Meta:
        ordering = ['-published_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    telegram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.email


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.email}"
