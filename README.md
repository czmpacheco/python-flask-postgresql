Note: change the DATABASE_URL value to your database url,
also change JWT_SECRET_KEY value to whatever you want to use as your secret key

Run the following from your terminal (if windows)

SET PORT=5432
SET FLASK_ENV=development
SET JWT_SECRET_KEY=admin
SET DATABASE_URL=postgres://postgres:aDmin@localhost:5432/blog_api_db
SET DATABASE_TEST_URL=postgres://postgres:admin@localhost:5432/blog_api_db

(if linux)

$ export PORT=5432
$ export FLASK_ENV=development
$ export JWT_SECRET_KEY=admin
$ export DATABASE_URL=postgres://postgres:aDmin@localhost:5432/blog_api_db
$ export DATABASE_TEST_URL=postgres://postgres:admin@localhost:5432/blog_api_db