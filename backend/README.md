## Backend

---
### Project structure
```lua
|-- backend
|   |-- functions
|   |   |-- .gitkeep
|   |-- models
|   |   |-- classifier
|   |   |   |-- .gitkeep
|   |   |-- summarization
|   |   |   |-- .gitkeep
|   |   |-- whisper
|   |   |   |-- .gitkeep
|   |-- static
|   |   |-- files
|   |   |   |-- .gitkeep
|   |   |-- images
|   |   |   |-- .gitkeep
|   |-- Dockerfile
|   |-- enviroment.yml
|   |-- main.py
|   |-- README.md
|   |-- requirements.txt
```

### Project setup
#### Installment of dependencies with Pip
```shell
pip install -r requirements.txt
```
#### Installment of dependencies with Conda
```shell
conda install --file requirements.txt
```

### Run the Frontend
#### Run the Backend directly
```shell
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
#### Run the Backend with Docker
```shell
docker-compose up backend
```

---
### How to use the Backend
