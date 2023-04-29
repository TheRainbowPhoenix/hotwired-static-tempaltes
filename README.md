# Jinja + hotwired

Just a silly test, trying to get them working together

## Setup

Install the dependencies and go into "dev build" (watch) mode :

```
pnpm i
pnpm run watch
```

Install the python dependencies and go into "watch" mode :

```
python -m venv venv
venv\Script\activate
pip install -r requirements.txt
venv\Scripts\uvicorn app.main:app --reload --port 8080
```

Then open http://127.0.0.1:8080/fr-fr/entreprises/hello-1 !
