IP_ADDR = $(shell ip -o -4 addr list wlan0 | awk '{print $$4}' | cut -d/ -f1)

migrations:
	python manage.py makemigrations
	python manage.py migrate

build:
	pip install -r requirements.txt
	make migrations

run-specific:
	python manage.py runserver $(IP_ADDR):8001

run:
	python manage.py runserver 0:8000