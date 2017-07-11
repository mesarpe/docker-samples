export EXTERNAL_PORT_WWW=4000;
export EXTERNAL_PORT_DB=5001;
export EXTERNAL_PORT_VISUALIZER=8080;
for i in {1..2}; do
  export EXTERNAL_PORT_WWW=$(($EXTERNAL_PORT_WWW+1));
  export EXTERNAL_PORT_DB=$(($EXTERNAL_PORT_DB+1));
  export EXTERNAL_PORT_VISUALIZER=$(($EXTERNAL_PORT_VISUALIZER+1));
  docker stack deploy -c docker-compose.yml exercise1_user$i;
done;
