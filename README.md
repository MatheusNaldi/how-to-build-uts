# Setting up the development environment

Execute the following commands after cloning the repository:

```
cp .env.template .env
docker-compose up
```

After that the project should be running on (http://localhost:3000/)[http://localhost:3000/].

# Run Tests

Execute the following command after the repository is up & running:

```
docker exec -it how-to-build-uts-api sh -c "./manage.py test"
```
