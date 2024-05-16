## The Web Scrapping Projects 

```bash 
---------------------------------------------------
Run with Docker 
----------------------------------------------------

get projects and clone the project ---

git clone https://github.com/AlaminSarkerFRII/Oates_Scrapper_Web.git

check python3 installation in your system


Run docker compose up --build -d 
check urls - http://0.0.0.0:8000/ && http://0.0.0.0:8000/docs


------------------------------------------------
Run Manually
------------------------------------------------

Open your Terminal
-RUN git clone https://github.com/AlaminSarkerFRII/Oates_Scrapper_Web.git
-RUN pip install requirements.txt
-Setup Database Server with Creadentials
-RUN python -m venv venv # for Create vertual environment
-RUN cd scraper
-RUN python3 index.py file #for Scraping Data
```

```bash
------------------------------------------------------
-RUN python main.py # for running main site 
- go to browse with this http://0.0.0.0:8000/docs
- check here all methods (CRUD) working properly

```