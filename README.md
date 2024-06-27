# django-apod

## About

Django-apod is a 

## Getting started

Create a new file `apod/settings/local.py` as a copy of `apod/settings/local.py.tmpl`. You will need to fill in two API keys

* [Nasa API key](https://api.nasa.gov/#signUp) - this is not required and if you do not provide one it will use the DEMO_KEY which has higher rate limits.
* [Hugging Face API key](https://huggingface.co/docs/api-inference/quicktour#get-your-api-token) - this is used for the text classification and getting tags from the explanation. This is needed for the Tags API. Grant your API key access to 
[X] Make calls to the serverless Inference API
[X] Make calls to Inference Endpoints

### Running the aplication locally

```
DJANGO_SETTINGS_MODULE=apod.settings.local python manage.py migrate
DJANGO_SETTINGS_MODULE=apod.settings.local python manage.py runserver
```

### Tests

To run the testsuite, run 
```
make test
```
