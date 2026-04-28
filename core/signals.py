import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel

@receiver(post_save, sender=TestModel)
def my_signal_handler(sender, instance, created, **kwargs):
    print("signal running")
    
    if instance.name == "sync":
        print("sleeping for 2 seconds")
        time.sleep(2)
        print("woke up")
        
    elif instance.name == "thread":
        print(f"signal thread: {threading.current_thread().name}")
        
    elif instance.name == "txn":
        print("saving from signal")
        
    print("finished signal")
