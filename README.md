# Textstrip


A Student Project for Text-Classification and Summarization.

---

## Table of Contents
1. [What is Textstrip?](#what-is-textstrip)
2. [How to access Textstrip?](#how-to-access-textstrip)
    1. [How to install Textstrip as a Docker container?](#how-to-install-textstrip-as-a-docker-container)
        1. [Use the Docker image from Docker Hub](#use-the-docker-image-from-docker-hub)
        2. [Build it from the source code](#build-it-from-the-source-code)
3. [How to use Textstrip?](#how-to-use-textstrip)
4. [Additional information](#additional-information)

## What is Textstrip?


---
## How to access Textstrip?
In order to Use Textstrip you have the following options:

1. Run it as a Docker container
2. Open it in your browser (Chrome, Firefox, Safari, etc.) (Coming soon)

### How to install Textstrip as a Docker container?

#### Use the Docker image from Docker Hub

1. Install Docker on your machine
2. Pull the Docker image from Docker Hub using the following command:
```bash
docker pull textstrip/textstrip
```
3. Run the Docker image using the following command:
```bash
docker run -p 8080:8080 textstrip/textstrip
```
4. Open your browser and go to http://localhost:8080
5. Enjoy!
6. (Optional) If you want to stop the Docker container, run the following command:
```bash
docker stop <container-id>
```

#### Build it from the source code

1. Install Docker on your machine
2. Clone the repository
3. Build the Docker image using the following command:
```bash
docker compose build
```
4. Run the Docker image using the following command:
```bash
docker compose up
```
5. Open your browser and go to http://localhost:8080
6. Enjoy!
7. (Optional) If you want to stop the Docker container, run the following command:
```bash
docker compose down
```
---
## How to use Textstrip?


---
## Additional information
For each Component of this Project more information can be found in the corresponding README.md file.
It is also possible to find more information about the Project in the Documentation (Info: Only available in German Language).