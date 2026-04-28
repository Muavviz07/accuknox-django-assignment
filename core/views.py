import time
import threading
from django.http import HttpResponse
from django.db import transaction
from .models import TestModel

def test_sync_view(request):
    print("starting sync test")
    start = time.time()
    
    TestModel.objects.create(name="sync")
    
    duration = time.time() - start
    print("saved, time:", round(duration, 2))
    
    return HttpResponse(f"took {duration:.2f}s")

def test_thread_view(request):
    print("starting thread test")
    print(f"view thread: {threading.current_thread().name}")
    
    TestModel.objects.create(name="thread")
    
    print("done")
    return HttpResponse("ok")

def test_transaction_view(request):
    print("starting txn test")
    count_before = TestModel.objects.count()
    print(f"count before: {count_before}")
    
    try:
        with transaction.atomic():
            TestModel.objects.create(name="txn")
            print("throwing error")
            raise Exception("oops")
    except Exception as e:
        print(f"error: {e}")
        
    print(f"count after: {TestModel.objects.count()}")
    return HttpResponse("ok")
