
Setup Instructions:

Create .env file in root directory and declare two variables. Generate Django SECRET_KEY by running below command in terminal and copy value into .env file.

```
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Obtain OPENAI_KEY from https://platform.openai.com/account/api-keys and copy into .env file.
.env file should look like:

```
SECRET_KEY = "..."

OPENAI_KEY = "..."
```

From root directory, create a virtual environment by running below commands. This should create a "env" folder. If you choose to name the folder to something else, ensure .gitignore is updated accordingly

```
python -m env
source env/bin/activate
```

Install app dependencies

```
pip install -r requirements.txt
```

Navigate into fantasyfit_bot_ai, run migrations and start server
```
cd fantasyfit_bot_ai
python manage.py migrate
python manage.py runserver

```