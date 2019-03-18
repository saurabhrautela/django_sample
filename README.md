# django_docker_boilerplate

Steps to launch swarm and deploy application:
1. Start VM
vagrant up

2. Start registry
docker-compose -f tools/registry.yml up -d

3. Build docker image and push to registry
pipenv lock -r >> requirements.txt
docker build -t localhost:5555/django_swarm .
docker push localhost:5555/django_swarm

4. Create secrets
cat tools/secrets/username_sample.txt | docker secret create pdb_username -
cat tools/secrets/password_sample.txt | docker secret create pdb_password -

5. Start swarm
docker swarm init

Note: If system has multiple addresses: docker swarm init --advertise-addr 192.168.21.150

6. Start another node
vagrant up
vagrant ssh app
docker swarm join --token SWMTKN-1-4q4vpjdoz220s1d8rlz29i53xfswa8qbsuhssx2k0fqy9jarvs-bbqfrcpwhbratn7j20bvi68ck 192.168.21.150:2377

7. Deploy application


