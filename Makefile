.PHONY: test
test:
	DJANGO_SETTINGS_MODULE=apod.settings.test python manage.py test -v 2