    Django + Postgres + Docker + Nginx + Gunicorn

    python:3.8.3-slim
    django==3.1.3
    
    pipenv
        
    tests need fixes (was worked before i18n)
    
    
** .env
    
    .env.prod
    DEBUG=0
    SECRET_KEY='q^$vs7!h8grxxo!lv9b7+bzuw$*7+n*ia@ezt5g%^661%^b0gj'
    DJANGO_ALLOWED_HOSTS=localhost 0.0.0.0 127.0.0.1 [::1]
    SQL_ENGINE=django.db.backends.postgresql
    SQL_DATABASE=nasa_prod
    SQL_USER=nasa
    SQL_PASSWORD=nasa123
    SQL_HOST=db
    SQL_PORT=5432
    DATABASE=postgres

    .env.dev
    DEBUG=1
    SECRET_KEY=foo
    DJANGO_ALLOWED_HOSTS=localhost 0.0.0.0 127.0.0.1 [::1]
    SQL_ENGINE=django.db.backends.postgresql
    SQL_DATABASE=nasa_dev
    SQL_USER=nasa
    SQL_PASSWORD=nasa123
    SQL_HOST=db
    SQL_PORT=5432
    DATABASE=postgres

** urls

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('users/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('', include('pages.urls', namespace='pages')),


** dirs

    django apps:
        - pages - main, used for all pages in site
        - design - get design from admin for changing frontend
        - users - allauth, contct data and admin
    locale - translates
    media - for save/upload media data
    static - static
    static - all static for prod
    templates - all templates for all project 
    
** run in prod:
    
    $ docker-compose -f docker-compose.prod.yml down -v
    $ docker-compose -f docker-compose.prod.yml up --build

    $ docker-compose exec web python manage.py makemigrations    
    $ docker-compose exec web python manage.py migrate
    $ docker-compose exec web python managy.py makemessages --all
    $ docker-compose exec web python manage.py compilemessages
    $ docker-compose exec web python manage.py createsuperuser

    http://localhost:8000/

** check db

    $ docker-compose exec db psql --username=nasa --dbname=nasa_prod
    $ \dt


** run in dev:

    $ docker-compose down -v    
    $ docker-compose up --build

    $ docker-compose exec web python manage.py makemigrations    
    $ docker-compose exec web python manage.py migrate
    $ docker-compose exec web python managy.py makemessages --all
    $ docker-compose exec web python manage.py compilemessages
    $ docker-compose exec web python manage.py createsuperuser

    http://localhost:1337/

** check db

    $ docker-compose exec db psql --username=nasa --dbname=nasa_dev
    $ \dt

**

    git pull https://github.com/smaffy/nasa_project.git
    0.0.0.0:8000/en/design_elements/
