makemigrations
migrate
createsuperuser

please create user 'company' and add all static data for site


1. git
sudo apt-get install git

2. git clone
//zajdi v papku dja raboty

git clone https://github.com/smaffy/nasa_project.git

3. docker
sudo apt-get remove docker docker-engine docker.io containerd runc

sudo apt-get update

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common


curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io

apt-cache madison docker-ce

sudo docker run hello-world

sudo groupadd docker

sudo usermod -aG docker $USER
//u menja $smafy vrode

newgrp docker

docker run hello-world

// WARNING: Error loading config file: /home/user/.docker/config.json -
// stat /home/user/.docker/config.json: permission denied
//
// sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
// sudo chmod g+rwx "$HOME/.docker" -R

sudo systemctl enable docker


4. zapusk, idem v papku proekta gde estj manage.py
docker-compose up --build

5. otkryvaem tuze papku v sosednem okne
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

6. v pervom okne ctrl+c i
docker-compose down
docker-compose up --build

7. otkryvaem v browsere
0.0.0.0:8000

