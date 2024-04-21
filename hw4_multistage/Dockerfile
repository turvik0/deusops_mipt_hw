#stage 1: system
FROM openjdk:11-jdk-slim as system
WORKDIR /app
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk && \
    rm -rf /var/lib/apt/lists/*
RUN apt update && \
    apt install -y maven

#stage 2: build
FROM system as build
WORKDIR /app
COPY ./javahelloworld/pom.xml .
RUN mvn dependency:go-offline
COPY ./javahelloworld/src ./src
RUN mvn clean package

#stage 3: run
FROM debian:bullseye-slim as run
RUN apt-get update && \
    apt-get install -y openjdk-17-jre && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY --from=build /app/target .
RUN chown -R 1001 .
USER 1001
# ENTRYPOINT ["tail","-f","/dev/null"]
CMD ["java", "-jar", "gs-maven-0.1.0.jar"]