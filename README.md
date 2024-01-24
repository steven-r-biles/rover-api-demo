## MARS ROVER

This project is a toy REST API using Django and SQLite. Here are the steps to run it on Windows:


0. Create virtual environment
```
python -m venv .
```

1. Activate virtual environment
```
./Scripts/Activate.ps1
```

2. Install requirements
```
pip install -r requirements.txt
```

3. Start the server 
```
python manage.py runserver
```

4. Run demo.py in another terminal to see the API in action! Make sure the virtual environment is active.
```
python demo.py
```

5. Run the tests
```
python manage.py test
```