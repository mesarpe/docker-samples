This is my instalation script:

cd www
docker build -t www_server .
cd ..

cd db
docker build -t mysql_server .
cd ..

# Check that both images appear here
docker images

#Login in docker cloud
docker login


docker tag image mesarpe/www_server:v1
docker tag image mesarpe/mysql_server:v1

#### NOW WE START THE EXECUTION OF THE MULTIPLE INSTANCES
docker swarm init
docker stack deploy -c docker-compose.yml exercise1

# Now the web app should be available at the browser on port 80
