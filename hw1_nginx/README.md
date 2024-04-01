run a working nginx web server in docker

1. The image should be lightweight
2. Use basic lightweight images - alpine
3. It should be possible to configure nginx via a file
4. Static pages must be an outer volume
5. Create a docker-compose file to start and build
6. The container must be run as an unprivileged user
7. After installing all the necessary utilities, the cache should be cleared