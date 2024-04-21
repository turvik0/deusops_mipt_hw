#stage 1: build the java application
FROM openjdk:11-jdk-slim AS builder
WORKDIR /app
COPY HelloWorld.java .
RUN javac HelloWorld.java

#stage 2: create the final lightweight image
FROM openjdk:11-jre-slim
WORKDIR /app
#copy the built java application from the builder stage
COPY --from=builder /app /app
RUN whoami
#run app
CMD ["java", "HelloWorld"]