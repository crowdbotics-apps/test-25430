from django.contrib import admin
from .models import (
    Recording,
    Event,
    Subscription,
    Course,
    Group,
    Module,
    SubscriptionType,
    Enrollment,
    Category,
)

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Recording)
admin.site.register(Subscription)
admin.site.register(Group)
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Enrollment)
admin.site.register(SubscriptionType)

# Register your models here.
