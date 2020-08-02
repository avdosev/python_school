# Создание сервера

Устанавливаем фласк

```
pip install flask
```
Нужно создать файл `app.py` с вот таким содержимым:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello world"


if __name__ == "__main__":
    app.run()

```

Запускаем сервер

```
flask run
```

Увидим что то такое:
```
 * Serving Flask app "test" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Переходим по url на последней строке. Можно через браузер либо postman.

Далее мы начнем создавать api нашего сервера.
Перед этим лучше прочитать прочитать про `http` и `restapi`, так как  мы будем делать второе используя первое.



Для примера сделаем два метода нашего api

| HTTP методы | Операция которая производится |
|----|----|
| GET | get_all |
| POST | create |
| PUT | update |
| DELETE | delete |

Для методов POST и PUT дополнительный данные мы будем отправлять в поле body в виде json и отдавать ответ так же в нем.

```python
from flask import Flask, jsonify, request
from database import DataBase # Наш класс базы данных

app = Flask(__name__)
accounts_db = DataBase('data/accounts')

@app.route('/api/accounts', methods=['GET'])
def get_accounts():
    return jsonify({'accounts': accounts_db.get_all()})

@app.route('/api/accounts', methods=['POST'])
def create_account():
    if not request.json:
        abort(400)

    for key in ('service', 'email', 'password'): 
        if key not in reques.json:
            abort(400)


    account = {
        'service': request.json['service'],
        'email': request.json['email'],
        'password': request.json['password'],
    }

    # метод create возвращает аккаунт со всеми полями 
    # в их числе id и дата создания записи
    account = accounts_db.create(account)

    return jsonify({'account': account}), 201

if __name__ == '__main__':
    app.run()
```

Для завершения создания простого апи нужно реализовать еще две функции для PUT и DELETE

Ниже представленна небольшая заготовка:
```python
@app.route('/api/accounts/<int:id>', methods=['PUT'])
def update_account(id):
    pass

@app.route('/api/accounts/<int:id>', methods=['DELETE'])
def delete_account(id):
    pass
```

При запуске мы можем перейти на эти страницы через строку в браузере, но через Postman будет удобнее, так как мы сможем выбирать какой http метод мы будем использовать.

