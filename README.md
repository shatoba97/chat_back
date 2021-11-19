# 1 Set up a virtual environment for isolated for isolated package installation
```bash
$ python -m venv venv
```

# 2 Activate the virtual environment
```bash
$ source venv/Scripts/activate
```

# 3 Install dependencies
```bash
$ pip install -r requirements.txt
```

# 4 Server in Windows
```bash
set FLASK_APP='main.py' flask run
```