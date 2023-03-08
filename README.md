# French Learning Tool

App to learn French, word by word.

### First time setup

- Create admin user
```shell
export FLASK_APP=app
flask fab create-admin
```

- Start the app
```shell
flask run
```

- Create migration
```shell
export FLASK_APP=app
flask db migrate -m "Migration description."

# On the database:
flask db upgrade
```

- Copy the `static/appbuilder` folder from the library into `app/static/appbuilder`.
- Set `FAB_STATIC_FOLDER = basedir + "/app/static/appbuilder/"` in `conf.py`.
- Modify the file `static/appbuilder/css/boostrap.min.css` directly.
