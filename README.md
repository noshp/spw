# spw
Submission for student pathways challenge by Mackenzie Nichols and Sonal Ranjit

## Setup Dev Environment
---

**Clone the Repo**
```bash
git clone git@github.com:noshp/spw.git
```
cd into the project folder

Have `virtualenv` installed on your machine.

```bash
virtualenv venv -p python3
```

Activate your virtualenv
```bash
source venv/bin/activate
```

**Install the pip requirements**
```bash
pip install -r requirements.txt
```

**Running the Flask app**

Export the Flask app in your terminal session
```bash
export FLASK_APP=run.py
```

Then run the flask app
```bash
flask run
```

