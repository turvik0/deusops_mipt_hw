creating a lightweight image by building the application on one image and running it on another.
1. The image should be lightweight
2. Use basic lightweight images - alpine
3. The application must be built in the first image
4. The application is launched in the second image, by copying the artifact
5. All configuration is done through environment variables
6. Building and launching the application must be done in one Dockerfile
7. When building an application, each build step should only be performed when dependent files change
8. Create a docker-compose file to start and build
9. The container must be run as an unprivileged user
10. After installing all the necessary utilities, the cache should be cleared