FROM alpine:3.19 as builder

RUN apk update && apk add --no-cache openjdk17 maven

WORKDIR /app

COPY /mvnw /mvnw.cmd /pom.xml ./

COPY /src ./src
RUN mvn dependency:resolve

RUN mvn package

FROM alpine:3.19

RUN apk update && apk add --no-cache openjdk17-jre

WORKDIR /app

COPY --from=builder /app/target/*.jar ./app.jar

RUN chown -R 1001:1001 .

USER 1001

EXPOSE 8080

CMD ["java", "-jar", "app.jar"]
# ENTRYPOINT ["tail","-f","/dev/null"]