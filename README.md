# Textstrip

---

## Table of Contents

This README.md file contains the following information:

<!-- TOC -->

* [Textstrip](#textstrip)
    * [Table of Contents](#table-of-contents)
    * [Aim of the project](#aim-of-the-project)
    * [Creator of the project](#creator-of-the-project)
    * [Setting up and Using the Project](#setting-up-and-using-the-project)
        * [Cloning the Project](#cloning-the-project)
        * [Setting Up the Project](#setting-up-the-project)
        * [Installing the Project Dependencies](#installing-the-project-dependencies)
            * [Installation with pip](#installation-with-pip)
            * [Installation with conda](#installation-with-conda)
            * [Installation with venv](#installation-with-venv)
        * [Running the Project](#running-the-project)
            * [Notebooks](#notebooks)
            * [Application](#application)
                * [Running the Project Using a Docker Container (Recommended) - Docker Compose](#running-the-project-using-a-docker-container-recommended---docker-compose)
                * [Running the Project using the Single Github-Repositories](#running-the-project-using-the-single-github-repositories)
                * [How to Use](#how-to-use)
    * [License](#license)
    * [Contact](#contact)
* [Textstrip - Backend](#textstrip---backend)
* [Textstrip - Frontend](#textstrip---frontend)

<!-- TOC -->
---

## Aim of the project

The aim of the project is
to develop a web application that can be used to compress texts different document types like Books,
Paper, News. Also, the Modells should reflect a good compression rate.
The application should be able to compress the
text on different compression rates, which the Enduser can select by himself.
It was also requested that the tool can
classify the different Texttypes independently.


---

## Creator of the project

This project was created by the following people:

* [Tobias Kister - 9416513](https://github.com/tkister)
* [Daniel Schmitz - ](https://github.com/dschmtz)
* [Jan Neifeld - ](https://github.com/JanDN312)
* [Michel Medved - ](https://github.com/mimed100)

---

## Setting up and Using the Project

Before you can run the project, some preparations need to be made first. These are described in the following.

### Cloning the Project

To open the project yourself in any IDE, the project must first be cloned. To do this, enter the following command in a
terminal:

```shell
git clone https://github.com/StripTheText/StripTheText.git
```

### Setting Up the Project

After successfully cloning the project, a folder named **TextStrip** should now be located in the current
terminal directory. The project is now located in this folder. The structure of the project is as follows:

```text
|- TextStrip
|  |- data
|  |  |- .gitkeep
|  |  |- __init__.py
|  |  |- Data.md
|  |  |- data_merged.csv
|  |  |- dataset_builder.ipynb
|  |  |- merged_data_2.py
|  |- docs
|  |  |- .gitkeep
|  |  |- Abgabe_Lasten-Pflichtenheft_Projektrealisierung.docx
|  |  |- Gantt_Chart_Abgabe.docx
|  |  |- Gantt_Chart_Abgabe.pdf
|  |  |- Pitch.pptx
|  |- functions
|  |  |- .gitkeep
|  |  |- __init__.py
|  |  |- audio2text.py
|  |  |- file_handling.py
|  |- notebooks
|  |  |- .gitkeep
|  |  |- text_classification_train.ipynb
|  |  |- text_compression_train.ipynb
|  |- .gitignore
|  |- docker-compose.yml
|  |- environment.yml
|  |- LICENSE
|  |- README.md
|  |- requirements.txt
```

The **data** folder contains all data that is needed for the project. The **docs** folder contains all documents that
were created as part of the Project. The **functions** folder contains all supporting functions that arise during the
execution of the project. The **notebooks** folder contains all notebooks that were created as part of the project.

### Installing the Project Dependencies

Before you can run the project, the project's dependencies must first be installed. There are the following options for
this: **[pip](https://pip.pypa.io/en/stable/)**, **[conda](https://docs.conda.io/en/latest/)** and **[venv](https://docs.python.org/3/library/venv.html)**. All three options are described below, but require an installed
version of Python (This project was developed with Python 3.11.*). If there is no suitable version of Python installed,
yet, it can be downloaded from the official **[Python website](https://www.python.org/downloads/)**.

**Note:** In addition to the project's dependencies, there are other dependencies defined by the operating system.
Please pay attention to the corresponding error messages.

#### Installation with pip

To install the dependencies with pip, the following command must be entered into a terminal:

```shell
pip install -r requirements.txt
```

**Note:** This method installs the packages globally. If this is not desired, one of the other methods should be used.

#### Installation with conda

Before you can install the individual dependencies, conda must first be installed and active. Please refer to the
official documentation of **[conda](https://docs.conda.io/en/latest/)**. After conda has been set up, it makes sense to
create a separate environment for this project, where only the required libraries are installed. To do this, follow
these steps:

```shell
conda create --name <Name of the Environment> python=3.11
```

After creating the environment, it must first be activated by the following step.

```shell
conda activate <Name of the Environment>
```

**Note:** If the environment is no longer needed, it can be deactivated again with the following command. It may also be
necessary to reactivate the environment at each new session.

```shell
conda deactivate
```

After the environment has been activated, the dependencies can now be installed. To do this, the following command must
be entered into a terminal (with activated environment):

```shell
conda install --file requirements.txt
```

#### Installation with venv

To install the dependencies with venv, a new environment must also be created by the following command in a terminal:

```shell
python -m venv <Name of the Environment>
```

After the environment has been created, it must first be activated by the following step.

```shell
<Name of the Environment>\Scripts\activate.bat
```

**Note:** If the environment is no longer needed, it can be deactivated again with the following command. It may also be
necessary to reactivate the environment at each new session.

```shell
deactivate
```

After the environment has been activated, the dependencies can now be installed. To do this, the following command must
be entered into a terminal (with activated environment):

```shell
pip install -r requirements.txt
```

With that, all dependencies are now installed and the project can be executed.

### Running the Project

#### Notebooks

To run the project, a Jupiter Notebook server must first be started. To do this, the following command must be entered
into a terminal that either has an active Python environment or an active conda environment:

```shell
jupyter notebook
```

Then you can access the notebooks via the browser. To do this, the following link must be entered in the browser's
address bar:

```text
http://localhost:8888/tree
```

After calling the link, a window should open with the content of the notebooks. Now the notebook can be run.

The following notebooks contain the code for the individual steps of the project:

- **[Dataset](data/dataset_builder.ipynb)**
- **[Text Classification](notebooks/text_classification_train.ipynb)**
- **[Text Commpression](notebooks/text_compression_train.ipynb)**

---

#### Application

In order to run our application there are two options. The first option is to run the application through the provided
Docker Images and the second option is to build the application through the single Github-Repositories.

**Note:** Please note that the installation through the Docker Images is much easier and faster than the installation of
the single Github-Repositories. That's why it is the preferred way to install the application.

##### Running the Project Using a Docker Container (Recommended) - Docker Compose

If you want to run this project using a Docker container, you can do so using the provided Docker image. This can be
particularly useful as it abstracts away dependency management and provides a self-contained environment for running the
application.

First, you need to have Docker installed on your machine. If you don't, you can download it from the official Docker
website: **[Docker](https://www.docker.com/get-started)**.

After installing Docker, you can run the following command in the terminal to start the application:

**Note:** If you want to run the application with Docker, you have to make sure that the Docker-Daemon is running. And
you cloned this repository.

```shell
docker-compose up --build
```

After the Setup is finished, you can access the application via the browser. To do this, the following link must be
entered in the browser's:

| Project Part | Link                  |
|--------------|-----------------------|
| Frontend     | http://localhost      |
| Backend      | http://localhost:8080 |

##### Running the Project using the Single Github-Repositories

If you want to run this project using the single Github-Repositories, you need to clone **both** repositories as the
first step:

```shell
git clone https://github.com/StripTheText/TextStrip-Backend.git
```

```shell
git clone https://github.com/StripTheText/TextStrip-Frontend.git
```

After cloning the repositories, you need to install the dependencies for both repositories. To do this, you can follow
the upper installation guide, but please create a new environments for each repo.

After installing the dependencies, you can run the application. To run it you need to start the backend first. To do so,
use the following command, inside the corresponding environment:

```shell
uvicorn main:app --host localhost --port 8080 --reload
```

Once the Startup of the Backend is finished, you can start the Frontend. To do so, use the following command, inside of
the corresponding environment:

```shell
streamlit run Introduction.py
```

For more detailed information about the Frontend, please refer to the README.md of the Frontend and for the Backend
correspondingly to the README.md of the Backend.

---

##### How to Use

###### Frontend

# [Navigating and Using Text Classification and Summarization Features in the Demo](https://app.tango.us/app/workflow/107e9d05-7a02-4166-ab9a-a5ebc8b83733?utm_source=markdown&utm_medium=markdown&utm_campaign=workflow%20export%20links)

__Creation Date:__ July 24, 2023  
__Created By:__ Tobias Kister  
[View most recent version on Tango.us](https://app.tango.us/app/workflow/107e9d05-7a02-4166-ab9a-a5ebc8b83733?utm_source=markdown&utm_medium=markdown&utm_campaign=workflow%20export%20links)



***




## # [Open the Strip-The-Text Frontend App](http://localhost/)


### 1. Navigate to the Demo - Page
![Step 1 screenshot](https://images.tango.us/workflows/107e9d05-7a02-4166-ab9a-a5ebc8b83733/steps/da2763d9-e502-4224-bf2e-038e17a3d9d4/a7114b30-5b6c-4fdd-929a-1a1aa9077953.png?crop=focalpoint&fit=crop&fp-x=0.1513&fp-y=0.2039&fp-z=1.7212&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=22&mark-y=246&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz01ODAmaD03NCZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


## # Custom User-Input


### 2. Enter your custom Text
![Step 2 screenshot](https://images.tango.us/workflows/107e9d05-7a02-4166-ab9a-a5ebc8b83733/steps/6f4ea164-c9f7-4ab5-89f3-a14d1c13fde9/fd159d6b-4bf5-4a08-b22d-1cf97c68ddac.png?crop=focalpoint&fit=crop&fp-x=0.2813&fp-y=0.5263&fp-z=1.2279&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=102&mark-y=66&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz02MjUmaD02NzQmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


## # Microphone


### 3. Umschalten auf Microphone
![Step 3 screenshot](https://images.tango.us/workflows/107e9d05-7a02-4166-ab9a-a5ebc8b83733/steps/a4995d11-90b5-4c89-993b-abaf8221c731/5a79e2b9-ddeb-4651-8e01-facea009f8c6.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n)


### 4. Record your Text
![Step 4 screenshot](https://images.tango.us/workflows/107e9d05-7a02-4166-ab9a-a5ebc8b83733/steps/c223e343-861e-40ed-bcdf-29c216f8ec05/01d80436-5d69-44b7-90c4-933361826ac3.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n)


## # File Upload


### 5. Select File Upload Option
![Step 5 screenshot](https://images.tango.us/workflows/107e9d05-7a02-4166-ab9a-a5ebc8b83733/steps/d2f90688-1a83-43cb-b6da-3c94b44f29f3/0d006660-ede0-4e30-9fa7-f5c5839bc6d7.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n)


### 6. Select File to Upload
![Step 6 screenshot](https://images.tango.us/workflows/107e9d05-7a02-4166-ab9a-a5ebc8b83733/steps/3414d93e-0d88-4cf8-8a9f-507cebc920ce/7b0fa720-b71f-49c3-896e-7082c4f87f2a.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n)


## # Weiterverarbeitung


### 7. Adjust the Compression Rate
![Step 7 screenshot](https://images.tango.us/workflows/107e9d05-7a02-4166-ab9a-a5ebc8b83733/steps/d7b4b936-d6d3-44a7-b22c-16a0614ea124/8a69db32-23c2-429d-8190-d4412fc490a6.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n)


### 8. Select your desired Activity
![Step 8 screenshot](https://images.tango.us/workflows/107e9d05-7a02-4166-ab9a-a5ebc8b83733/steps/f0faf03b-6dd9-44c8-b2ff-71d20e9cb737/f75a9453-0f88-4605-a0fe-84f73fe8ce09.png?crop=focalpoint&fit=crop&fp-x=0.1866&fp-y=0.9099&fp-z=2.9760&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=536&mark-y=515&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMjkmaD0xNDkmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 9. Click on Go!
![Step 9 screenshot](https://images.tango.us/workflows/107e9d05-7a02-4166-ab9a-a5ebc8b83733/steps/1f5e058d-084c-4f4c-b3fa-6508603c5aa6/ac2201e6-4e51-4a54-9e45-e6fe0f14346f.png?crop=focalpoint&fit=crop&fp-x=0.2810&fp-y=0.9099&fp-z=2.2889&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=412&mark-y=582&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0zNzYmaD0xMTUmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 10. View your Results
---

###### Backend 

# [StripTheText 2.0 - Backend](https://app.tango.us/app/workflow/a5fb78da-563c-4d75-8a72-67f904588f16?utm_source=markdown&utm_medium=markdown&utm_campaign=workflow%20export%20links)

These are the Steps how to perform the different Tasks through the Backend of the Application.

__Creation Date:__ July 24, 2023  
__Created By:__ Tobias Kister  
[View most recent version on Tango.us](https://app.tango.us/app/workflow/a5fb78da-563c-4d75-8a72-67f904588f16?utm_source=markdown&utm_medium=markdown&utm_campaign=workflow%20export%20links)



***




## # [StripTheText 2.0: Classification](http://localhost:8080/#/)
As the first Step it is required to open the Webpage of the Application: [localhost/8080](localhost:8080)


### 1. Select the API-Entpoint
For the Task of the Classification, please select the API-Entpoint "/api/classifier"
![Step 1 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/a02a33d4-2f70-4abb-9164-203ab5e4a686/ebcdcec5-af27-4989-8e2a-d711da276456.png?crop=focalpoint&fit=crop&fp-x=0.4777&fp-y=0.4388&fp-z=1.0281&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=34&mark-y=343&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTExJmg9NDEmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 2. For testing the API please press the Button "Try it Out"
![Step 2 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/7aeec2ca-fdca-4a10-ab8f-9629f33f2598/68098500-7335-4173-87ff-c71ec11ddd26.png?crop=focalpoint&fit=crop&fp-x=0.7439&fp-y=0.6073&fp-z=2.8624&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=383&mark-y=346&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz00MzMmaD0xMTQmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 3. Inserting of Data
In the Textfield change the Value "String" to your requested text, please Note Line Breaks are not supported, caused by the JSON-Format.
![Step 3 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/9bbe6d7a-f1c0-456f-9468-5d6030ef16ab/093b8d1f-528d-4dc3-8a92-3c1c0c4fb690.png?crop=focalpoint&fit=crop&fp-x=0.4924&fp-y=0.4560&fp-z=1.0420&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=35&mark-y=221&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTMxJmg9MzI0JmZpdD1jcm9wJmNvcm5lci1yYWRpdXM9MTA%3D)


### 4. Example Values
![Step 4 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/37368560-2e85-4d94-8510-f0f9c95c002e/d40c0cb5-471b-4d57-bbd0-57f484b89aa0.png?crop=focalpoint&fit=crop&fp-x=0.4924&fp-y=0.5901&fp-z=1.0420&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=35&mark-y=299&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTMxJmg9MzI0JmZpdD1jcm9wJmNvcm5lci1yYWRpdXM9MTA%3D)


### 5. Click on Execute
![Step 5 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/3be9f607-c1c2-4b99-a6d8-2bc4591849d2/cfdc17cd-b677-4c8c-84c7-ce9e1d5dfcc1.png?crop=focalpoint&fit=crop&fp-x=0.2731&fp-y=0.8734&fp-z=1.3393&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=80&mark-y=643&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz03MTgmaD01MyZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 6. Results
When you scroll down, you will see your result in JSON-Format at the position of the StatusCode 200.
![Step 6 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/8cb71a1c-250e-4a87-a226-e6f693d06e82/350cb5ba-358a-4449-8334-10351aba67b7.png?crop=focalpoint&fit=crop&fp-x=0.5303&fp-y=0.4453&fp-z=1.1312&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=38&mark-y=354&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTI1Jmg9OTgmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


## # [StripTheText 2.0: Compression](http://localhost:8080/#/)


### 7. Selcet your API-Endpoint
Both summarizer Entpoints will work, the one with "/compress", will also include the Compression Rate.
![Step 7 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/d7445cd9-3314-467a-954e-09d39b9983d1/3b40ffa8-b3da-4677-aa9d-f948749b4a1f.png?crop=focalpoint&fit=crop&fp-x=0.1751&fp-y=0.2162&fp-z=2.3041&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=299&mark-y=369&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0zNzEmaD02NiZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 8. Click on Try it out
![Step 8 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/08803c8c-9fbd-4b92-9e10-3de44f93243f/d28fdcea-2772-4bc4-9542-04082e82c863.png?crop=focalpoint&fit=crop&fp-x=0.8916&fp-y=0.1148&fp-z=2.8624&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=648&mark-y=208&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0zNTkmaD0xMTQmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 9. Change your Requested Data
![Step 9 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/1651ba95-4af7-47e5-88bb-c03db0703923/252563d7-1ee8-4383-a7af-da930ef242d1.png?crop=focalpoint&fit=crop&fp-x=0.4924&fp-y=0.3659&fp-z=1.0420&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=35&mark-y=145&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTMxJmg9MzI0JmZpdD1jcm9wJmNvcm5lci1yYWRpdXM9MTA%3D)


### 10. Click on Execute
![Step 10 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/5a102442-3f01-4397-aa1b-f3a9336cadd2/104815bd-9be0-4fc5-9106-9a38bd047c85.png?crop=focalpoint&fit=crop&fp-x=0.4924&fp-y=0.6406&fp-z=1.0420&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=35&mark-y=480&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTMxJmg9NDkmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 11. View your Results.
![Step 11 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/4b32d291-9d07-4deb-9666-d61aae0d82b1/3324801c-cb85-4caf-9a52-a7082d75e474.png?crop=focalpoint&fit=crop&fp-x=0.5303&fp-y=0.7124&fp-z=1.1312&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=38&mark-y=452&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTI1Jmg9MTg0JmZpdD1jcm9wJmNvcm5lci1yYWRpdXM9MTA%3D)

---

## License

This project is licensed under the MIT License— see the [LICENSE](LICENSE) file for details.

---

## Contact

In case of questions, suggestions or other concerns, please contact us at the following email
address: [contact@tkister.de](mailto:contact@tkister.de)

---

# Textstrip - Backend

The Source Code of the Backend can be found
here: [Textstrip - Backend](https://github.com/StripTheText/TextStrip-Backend). Further Information about the Backend
and how it can be installed separately can be found in the README.md of the Backend.

---

# Textstrip - Frontend

The Source Code of the Frontend can be found
here: [Textstrip - Frontend](https://github.com/StripTheText/TextStrip-Frontend). Further Information about the Frontend
and how it can be installed separately can be found in the README.md of the Frontend.
