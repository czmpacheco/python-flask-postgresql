Note: change the DATABASE_URL value to your database url,
also change JWT_SECRET_KEY value to whatever you want to use as your secret key

--------------------------------------

Project Pre-requisites & Dependencies:
python3.x
postgresql
pipenv

flask
flask sqlalchemy
psycopg2
flask-migrate
flask-script
marshmallow
flask-bcrypt
pyjwt
manage

pip install pipenv
pipenv shell
pipenv install flask flask-sqlalchemy psycopg2 flask-migrate flask-script marshmallow flask-bcrypt pyjwt manage

--------------------------------------

Run the following from your terminal (if windows, if linux change SET for $ export)
SET PORT=5432
SET FLASK_ENV=development
SET JWT_SECRET_KEY=admin
SET DATABASE_URL=postgres://postgres:admin@localhost:5432/blog_api_db
SET DATABASE_TEST_URL=postgres://postgres:admin@localhost:5432/blog_api_db

--------------------------------------

Testing USERS on POSTMAN:

~ Create User POST ~
POST http://127.0.0.1:5000/users/
          -Body raw JSON-
{
"email": "testando@mail.com",
"password": "senhatestando",
"name": "nome de teste"
}

---------------

~ Login POST ~
POST http://127.0.0.1:5000/users/login
          -Body raw JSON-
{
"email": "testando@mail.com",
"password": "senhatestando"
}
(copy jwt-token from login call)

---------------

~ Get User GET ~
GET http://127.0.0.1:5000/users/me
          -headers-
api-token       jwt-token value

---------------

~ Edit User PUT ~
PUT http://127.0.0.1:5000/users/me
          -Bodyraw JSON-
{
"name": "novo nome"
}

---------------

~ Get All Users GET ~
GET http://127.0.0.1:5000/users/
          -headers-
api-token       jwt-token value

---------------

~ Delete DELETE ~
DELETE http://127.0.0.1:5000/users/me
          -headers-
api-token       jwt-token value

--------------------------------------

Testing BLOGPOSTS on POSTMAN:

~ Create Blogpost POST ~
POST http://127.0.0.1:5000/blogposts/
          -Body raw JSON-
{
"title": "New POST",
"contents": "primeira postagem",
}

---------------

~ All Blogposts GET ~
GET http://127.0.0.1:5000/blogposts/
          -Pretty JSON-
          
---------------

~ One Blogposts GET ~
GET http://127.0.0.1:5000/blogposts/<int:blogpost_id>
          -Pretty JSON-
          
---------------

~ Blogpost PUT ~
PUT http://127.0.0.1:5000/blogposts/<int:blogpost_id>
          -Body raw JSON-
{
"title": "New Update POST",
"contents": "novos dados na postagem",
}

---------------

~ Blogpost DELETE~
DELETE http://127.0.0.1:5000/blogposts/<int:blogpost_id>
          -Body raw JSON-
{
"title": "New Update POST",
"contents": "novos dados na postagem",
}
