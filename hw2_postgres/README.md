The goal of the laboratory: to assemble from the source and launch a working application with a database in Docker (any open source - Java, python/django/flask, golang).

1. The image should be lightweight
2. Use basic lightweight images
3. All application configuration must be through environment variables
4. Static (dependencies) must be an outer volume `volume`
5. Create a `docker-compose` file to start and build
6. In `docker-compose` you need to use a database (postgresql, mysql, mongodb etc.)
7. When starting the application, automatic migrations should be taken into account
8. The container must be run as an unprivileged user
9. After installing all the necessary utilities, the cache should be cleared