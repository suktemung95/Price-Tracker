# README here

- docker run --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
- and make sure to create a table named products (so far)
- uvicorn routes.products:app --reload FROM app directory