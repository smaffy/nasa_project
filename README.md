docker-compose down
sudo docker volume ls
sudo docker volume rm nasa_project_postgres_data
git pull https://github.com/smaffy/nasa_project.git
docker-compose up --build




docker-compose exec web python managy.py makemigrations

docker-compose exec web python managy.py migrate

docker-compose exec web python managy.py createsuperuser

docker-compose exec web python managy.py makemessages --all

docker-compose exec web python managy.py compilemessages



docker-compose down

docker-compose up --build


0.0.0.0:8000/en/design_elements/