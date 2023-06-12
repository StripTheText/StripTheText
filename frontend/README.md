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

### Run the Frontend
#### Run the Frontend directly
```shell
python streamlit run Introduction.py
```
#### Run the Frontend with Docker
```shell
docker-compose up frontend
```

---
### How to use the Frontend
