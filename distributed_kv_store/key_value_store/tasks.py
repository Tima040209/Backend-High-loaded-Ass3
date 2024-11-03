from celery import shared_task
from django.core.cache import cache

@shared_task
def store_data_task(key, value):
    # Store data in Redis cache
    cache.set(key, value, timeout=300)
    return f"Data stored successfully for key: {key}"