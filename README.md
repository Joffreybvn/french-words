# French Learning Tool

App to learn French, word by word.

### First time setup

- Create admin user
```shell
export FLASK_APP=french_words
flask fab create-admin
```

- Start the app
```shell
flask run
```

- Copy the `static/appbuilder` folder from the library into `app/static/appbuilder`.
- Set `FAB_STATIC_FOLDER = basedir + "/app/static/appbuilder/"` in `conf.py`.
- Modify the file `static/appbuilder/css/boostrap.min.css` directly.
