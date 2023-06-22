# Decision-table

Sample python test for decision table


## main on CMD

cd C:\Users\ABC\Desktop\decision-table-master
pipenv install --dev
pipenv shell
pipenv run  bandit --recursive app
pipenv run  flake8 app
pipenv run  mypy app
pipenv run  black --check --diff app
cd app
python3 main.py

Result:
Status: APPROVED


## Unittest on CMD

cd ..
C:/Users/ABC/AppData/Local/Microsoft/WindowsApps/python3.10.exe c:/Users/ABC/Desktop/decision-table-master/app/test_main.py


Result:
================================================= test session starts =================================================
platform win32 -- Python 3.10.11, pytest-7.1.0, pluggy-1.2.0
rootdir: C:\Users\ABC\Desktop\decision-table-master
collected 7 items

app\test_main.py .                                                                                               [ 14%]
tests\test_abstract.py ..                                                                                        [ 42%]
tests\test_decision_table.py ....                                                                                [100%]

================================================== 7 passed in 0.07s ==================================================

pipenv --rm
