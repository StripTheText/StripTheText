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