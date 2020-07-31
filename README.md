<!-- ----------------------------------------DVP CONFIG-------------------------------------------- -->
  $ pip freeze | grep -v "pkg-resources" > requirements.txt
  		pkg-resources causes an error on heroku: Ubuntu Bug (19.10) providing incorrect metadata to pip

<!-- ----------------------------------------GIT CONFIG-------------------------------------------- -->
#SPECIFICATIONS
python version: 3.6.9
django version: 3.0.4

#GITIGNORE
git -rm -r --cached .
git add .
git push

	$ python3 manage.py check --deploy
<!-- ----------------------------------------PRODUCTION CONFIG-------------------------------------------- -->
#HEROKU
import django_heroku
	$ pip install django_heroku
		whitenoise | dj-database-url | django-heroku
##Fetch Data
Procfile | requirements.txt | runtime.txt

##DB
import dj_database_url

#Static
##Whitenoise
Installed with django_heroku
Configure Middleware & STATIC
	# whitenoise
	https://devcenter.heroku.com/articles/django-assets
##Gunicorn
	$ pip3 install gunicorn


<!-- ----------------------------------------HEROKU SITE CONFIG------------------------------------------- -->
##APP
	$ heroku login
	$ heroku create app_name
##Push into HEROKU
	$ git push heroku master

##Configure Heroku App
	$ heroku config

Secret_Key
	$ heroku config:set DJANGO_SECRET_KEY=
DEBUG
	$ heroku config:set DJANGO_DEBUG=
BRAINTREE
	$ heroku config:set BRAINTREE_MERCHANT_ID=
	$ heroku config:set BRAINTREE_PUBLIC_KEY=
	$ heroku config:set BRAINTREE_PRIVATE_KEY=
STATIC
Debugging
	$ heroku config:set DEBUG_COLLECTSTATIC=1
Disable Collectstatic: LET Heroku run collectstatic
	$ heroku config:set DISABLE_COLLECTSTATIC=1

	$ heroku ps:scale web=1

##Heroku DB
	$ heroku addons:create heroku-postgresql:hobby-dev
													||
	$ heroku addons:create heroku-postgresql

	$ heroku run python manage.py migrate
	$ heroku run python manage.py createsuperuser

<!-- ------------------------------------------TROUBLE SHOOT--------------------------------------------- -->
heroku logs -t -a <heroku-app>

https://hashcode.co.kr/questions/9391/heroku%EC%97%90-django%EB%A5%BC-%EC%98%AC%EB%A6%B0-%ED%9B%84%EC%97%90-server-error-500%EC%9D%B4-%EB%B0%9C%EC%83%9D%ED%95%A9%EB%8B%88%EB%8B%A4
<!-- ------------------------------------------CELERY--------------------------------------------- -->
celery -A buro_shop worker -l info

celery -A buro_shop flower