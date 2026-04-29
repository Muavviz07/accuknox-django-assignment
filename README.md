# Django Signals Assignment

This project demonstrates how Django signals behave with respect to execution flow, threading, and database transactions.

## Setup

pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

## Endpoints

http://127.0.0.1:8000/test-sync/
http://127.0.0.1:8000/test-thread/
http://127.0.0.1:8000/test-transaction/

## Notes

- Check console output while hitting endpoints
- Sync test shows blocking behavior
- Thread test prints current thread
- Transaction test shows rollback

## Rectangle

{'length': value}  
{'width': value}
