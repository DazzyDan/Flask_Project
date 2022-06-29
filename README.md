# Flask_Project
1. Install vituralenv
python3 -m venv env/
. env/bin/activate
2. Install Flask
python3 -m pip install Flask flask-sqlalchemy
3. Jinja2 Template:
https://jinja.palletsprojects.com/en/3.1.x/templates/
4. Create database:
under virtual env, type 'python3' in terminal, and then put 'from app import db', 'db.create_all()'
The test.db will be created