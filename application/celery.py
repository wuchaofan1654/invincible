# -*- coding: utf-8 -*-
"""
Create by sandy at 17:07 14/03/2022
Description: ToDo
"""

# schedule_task/schedule_task/celery.py
from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

import logging


logger = logging.getLogger(__name__)


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')
app = Celery('apps')

# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
