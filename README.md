# g-7-serialization
This project is designed for serialization in a web application context, utilizing Flask and SQLAlchemy.
#### Setup Instructions
1. Install dependencies and activate the virtual enviroment:
        pipenv install
        pipenv shell
2. Change to  server directory
        cd server
3. Ensure database migration have been appllied, if not done:
        flask db init
        flask db migrate-m 'migration message'
        flask db upgrade
4. Populate the database with initial data:
        python seed.py        

