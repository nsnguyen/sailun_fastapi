# sailun_fastapi
This project is for Sailun's API tutorial

## Heroku
First create an account on Heroku
Then download [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

```
heroku container:login
heroku create {container_name} (do only once)
heroku container:push web --app {container_name}
heroku container:release web
```
