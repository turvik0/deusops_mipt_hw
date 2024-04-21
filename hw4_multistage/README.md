master methods for creating images with different levels of dependencies

1. Create a Dockerfile called system. All dependencies for building the project will be installed into it. As an example, a bare node of the required version.
2. Create a Dockerfile for the build and call it build. The project will be built in it, it must use the system image. You cannot install any additional dependencies in build, i.e. apk add, apt install, etc. are prohibited. In it you can only download dependencies and build the project.
3. Create a Dockerfile that will run the code that was compiled in build. It should only contain a tool for launching your project, as an example for a node project - npm run start, etc. If you have a python project, you can combine steps 2 and 3. If you are building a project on GO, then there should only be a binary to run.
4. All configuration is done through environment variables
5. Use basic lightweight images - alpine
6. The container must be run as an unprivileged user
7. After installing all the necessary utilities, the cache should be cleared