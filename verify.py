import os
import django
from django.test import Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'accuknox_assignment.settings')
django.setup()

c = Client()
print("\n--- /test-sync/ ---")
c.get('/test-sync/')
print("\n--- /test-thread/ ---")
c.get('/test-thread/')
print("\n--- /test-transaction/ ---")
c.get('/test-transaction/')
