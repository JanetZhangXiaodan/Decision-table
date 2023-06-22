# Decision-table

Sample python test for decision table


## main on CMD

cd C:\Users\ABC\Desktop\decision-table-master \
pipenv install --dev \
pipenv shell \
pipenv run  bandit --recursive app \
pipenv run  flake8 app \
pipenv run  mypy app \
pipenv run  black --check --diff app \
cd app \
python3 main.py

Result: \
Status: APPROVED


## Unittest on CMD

cd .. \
C:/Users/ABC/AppData/Local/Microsoft/WindowsApps/python3.10.exe c:/Users/ABC/Desktop/decision-table-master/app/test_main.py


Result: \
================================================= test session starts ================================================= \
platform win32 -- Python 3.10.11, pytest-7.1.0, pluggy-1.2.0 \
rootdir: C:\Users\ABC\Desktop\decision-table-master \
collected 7 items 

app\test_main.py .                                                                                               [ 14%]
tests\test_abstract.py ..                                                                                        [ 42%]
tests\test_decision_table.py ....                                                                                [100%]

================================================== 7 passed in 0.07s ==================================================

pipenv --rm


![image](https://github.com/JanetZhangXiaodan/Decision-table/assets/15668158/82b707c5-e307-48f0-907f-57d66a5d7508) \
![image](https://github.com/JanetZhangXiaodan/Decision-table/assets/15668158/37100c83-7c16-49cb-8cb8-e6224f357a68) \
![image](https://github.com/JanetZhangXiaodan/Decision-table/assets/15668158/f30f5788-6d1a-4956-a66d-989a426c4657) \
![image](https://github.com/JanetZhangXiaodan/Decision-table/assets/15668158/548eb50a-a3b6-4c2d-8ca8-e82215028741)

