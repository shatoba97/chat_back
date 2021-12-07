# 1 Set up a virtual environment for isolated for isolated package installation
```bash or cmd
$ python -m venv venv
```

# 2 Activate the virtual environment
```bash
$ source venv/Scripts/activate
```
OR
```cmd
$ venv\\Scripts\\activate.bat
```

# 3 Install dependencies
```bash or cmd
$ pip install -r requirements.txt
```

# 4 Server in Windows
```bash
set FLASK_APP='main.py' flask run
```
OR
```cmd
$ set FLASK_APP=main
$ flask run
```