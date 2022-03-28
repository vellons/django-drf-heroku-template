# Django Rest Framework template for Heroku
A basic template with: Django Rest Framework, Django filters, Pagination, Swagger, WhiteNoise.

Ready to be deployed with Heroku for free.

## Project setup

#### Create a virtual environment (python>=3.8)
```shell
python3 --version
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


#### Run
```shell
cd src
python manage.py runserver
```

#### Other command
```shell
python manage.py makemigrations  // To collect edits in your models.py files
python manage.py migrate  // To apply edits to your database 
python manage.py collectstatic  // To collect static files
```

## Heroku deploy
In order to deploy your application to Heroku make sure to edit TODOs in src/myapp/settings.py

You need to enable GitHub Action in your repository. 
Then you need to set 3 secrets: HEROKU_APP_NAME, HEROKU_API_KEY, HEROKU_EMAIL.
The CI will automatically push to the main branch of your heroku project.

See runtime.txt and Procfile to edit Heroku settings.