## Frontend

---
### Project structure
```lua
|-- frontend
|   |-- functions
|   |   |-- .gitkeep
|   |-- pages
|   |   |-- .gitkeep
|   |   |-- 2_Demo.py
|   |   |-- 3_Validation_Models.py
|   |   |-- 4_Handbook.py
|   |-- .env-template
|   |-- Dockerfile
|   |-- enviroment.yml
|   |-- Introduction.py
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

Conda setup full Frontend-Environment:
```shell
conda env create -f environment.yml
```
Activate the new environment:
```shell
conda activate StripTHeText_Frontend
```

### Run the Frontend
#### Run the Frontend directly
```shell
streamlit run Introduction.py
```
#### Run the Frontend with Docker
```shell
docker-compose up frontend
```

---
### How to use the Frontend
