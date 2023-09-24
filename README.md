## Product Management
#### Product management is application for list data product, create or update and delete. you can filter data product based on can be sold and cant be sold.

### Requirements

- Tools
  - python 3.11
  - postgresql
  - browser (chrome or mozilla)
- Libary
  - Django              4.2.5
  - django-bootstrap-v5 1.0.11
  - djangorestframework 3.14.0
  - psycopg2            2.9.7
  - requests            2.31.0
  - virtualenv          20.24.5
  - requests-toolbelt   1.0.0

### How to install

- install library
```bash
pip install requirement.txt
```
- setting your credential database in settings.py
- then run migration
```bash
python manage.py makemigration && python manage.py migrate
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