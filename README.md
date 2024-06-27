# django-apod

## Getting started

Create a new file `apod/settings/local.py` as a copy of `apod/settings/local.py.tmpl`. You will need to fill in two API keys

* [Nasa API key](https://api.nasa.gov/#signUp) - this is not required and if you do not provide one it will use the DEMO_KEY which has higher rate limits.
* [Hugging Face API key](https://huggingface.co/docs/api-inference/quicktour#get-your-api-token) - this is used for the text classification and getting tags from the explanation. This is needed for the Tags API. Grant your API key access to 
[X] Make calls to the serverless Inference API
[X] Make calls to Inference Endpoints

### Running the application locally

```
DJANGO_SETTINGS_MODULE=apod.settings.local python manage.py migrate
DJANGO_SETTINGS_MODULE=apod.settings.local python manage.py runserver
```

### Tests

To run the testsuite, run 
```
make test
```

## Endpoints

`/admin/` - django admin. You must create a superuser/ log in as superuser to view and/or edit this data.

`/images/` - images list. Initially this is empty

`/images/`random - get a random image

`/images/<date>/` - get the APOD image for a specific data

`/images/<data>/tags/` - get tags using a HuggingFace keyword search for this image. Note: this must happen after the image has already been retrieved 

## Outstanding issues/ time limitations

1. The endpoint to fill tags is separate from actually showing those tags. Would like to make sure that if the image doesn't exist when the tags endpoint is called 
Would like to either make that a proper hyperlinked field or automatically fetch tags immediately after the image is fetched/ based on a URL query parameter.


2. Testing: there are a few sample tests but the application is not well-tested overall. Ran out of time. If given more time, would have added tests for the rest of the endpoints.

3. The keyword model doesn't always give the best results, would be better to have a trained model specifically for this use case. 