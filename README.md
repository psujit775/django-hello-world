# django-hello-world

You can Run this application On your local or in docker.

# Run Command
```python manage.py runserver```

Above will start Django server on http://localhost:8000.

# Run in Docker
First build Docker.

```docker build -t django-hello-world .```

Run Docker.
```docker run --name django-hello-world --rm -it -p 8000:8000 django-hello-world```
