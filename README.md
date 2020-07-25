## Installation

To run the application, enter the following commands into the console, while you must have Python 3+ installed on your computer

```bash
pip install docker-compose
```

```bash
docker-compose run web python manage.py migrate --noinput

docker-compose run web python manage.py createsuperuser

docker-compose up -d --build
```

## Usage
To stop the application, enter the following commands
```bash
docker ps

docker stop [CONTAINER ID]
```