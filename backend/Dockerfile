# FROM openjdk:11
# ADD target/backend-0.0.1-SNAPSHOT.jar backend.jar
# ENTRYPOINT ["java", "-jar", "backend.jar"]


# Stage 1: Build the JAR
FROM maven:3.8.1-openjdk-11 AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package -DskipTests

# Stage 2: Run the JAR
FROM openjdk:11
WORKDIR /app
COPY --from=build /app/target/backend-0.0.1-SNAPSHOT.jar backend.jar
ENTRYPOINT ["java", "-jar", "backend.jar"]

