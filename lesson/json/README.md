# json
JSON или JavaScript Object Notation — текстовый формат обмена данными, основанный на JavaScript. Как и многие другие текстовые форматы, JSON легко читается людьми. Формат JSON был разработан Дугласом Крокфордом.

пример:
~~~json
{
   "firstName": "Иван",
   "lastName": "Иванов",
   "address": {
       "streetAddress": "Московское ш., 101, кв.101",
       "city": "Ленинград",
       "postalCode": 101101
   },
   "phoneNumbers": [
       "812 123-1234",
       "916 123-4567"
   ]
}
~~~

На языке XML подобная структура выглядела бы примерно так:
~~~xml
<person>
  <firstName>Иван</firstName>
  <lastName>Иванов</lastName>
  <address>
    <streetAddress>Московское ш., 101, кв.101</streetAddress>
    <city>Ленинград</city>
    <postalCode>101101</postalCode>
  </address>
  <phoneNumbers>
    <phoneNumber>812 123-1234</phoneNumber>
    <phoneNumber>916 123-4567</phoneNumber>
  </phoneNumbers>
</person>
~~~

Как работать?

Пример сериализации JSON Python

~~~Python
import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian",
        "age": 54
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
~~~
или для строки
~~~Python
json_string = json.dumps(data)
~~~

Пример десериализации JSON Python

Представьте что у вас есть некие данные, хранящиеся на диске, которыми вы хотите манипулировать в памяти. Вам все еще нужно будет воспользоваться контекстным менеджером, но на этот раз, вам нужно будет открыть существующий data_file.json в режиме для чтения.

~~~Python
import json

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    print(data)
~~~
или для строки
~~~Python
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
 
data = json.loads(json_string)
~~~

