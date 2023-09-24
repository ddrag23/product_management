## Product Management
#### Product management is application for list data product, create or update and delete. you can filter data product based on can be sold and cant be sold.

### Requirements

- Tools
  - python 3.11
  - postgresql
  - browser (chrome or mozilla)
- Libary
    - asgiref==3.7.2
    - beautifulsoup4==4.12.2
    - certifi==2023.7.22
    - charset-normalizer==3.2.0
    - distlib==0.3.7
    - Django==4.2.5
    - django-bootstrap-v5==1.0.11
    - djangorestframework==3.14.0
    - filelock==3.12.4
    - idna==3.4
    - platformdirs==3.10.0
    - psycopg2==2.9.7
    - pytz==2023.3.post1
    - requests==2.31.0
    - requests-toolbelt==1.0.0
    - soupsieve==2.5
    - sqlparse==0.4.4
    - tzdata==2023.3
    - urllib3==2.0.5
    - virtualenv==20.24.5


### How to install
- clone this repository using ssh or https
```bash
git clone git@github.com:ddrag23/product_management.git
```
```bash
git clone https://github.com/ddrag23/product_management.git
```
- go to directory project, if you using linux. you can do it:
```bash
cd <yout-path>/<project-path>
```
- setting venv (optional)
```bash
python -m venv <your-name-env>
```
- activate venv, if you using linux or mac you can do it : (optional)
```bash
source env/bin/activate
```
- if you using windows. you can do it
```bash
.\env\Scripts\activate
```
- install library
```bash
pip install -r requirement.txt
```
- setting your credential database in settings.py
- then run migration
```bash
python manage.py makemigrations && python manage.py migrate
```
- after success migration table. then running shell.py for initial data product from service api
```bash
python shell.py
```
- after success running. then running this app using:
```bash
python manage.py runserver
```
- open url host in :
```bash
127.0.0.1:8000
```
### Notes :
- for requirement library above you can look via requirement.txt file or you can manually install following requirement in above
- for the url used for access this site. it doesn't have to be port 8000  you can setting manually or you can look in your terminal when running runserver
- here i'm just use python 3.11.x, in my local machine there no orther python versions like python version 2.x.x. if your local machine have python 2.x.x. you can try running python3 or according to your machine's local settings