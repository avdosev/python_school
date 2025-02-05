# Функции

Функция или подпрограмма — фрагмент программного кода, к которому можно обратиться из другого места программы. В большинстве случаев с функцией связывается идентификатор, но многие языки допускают и безымянные функции. С именем функции неразрывно связан адрес первой инструкции, входящей в функцию, которой передаётся управление при обращении к функции. После выполнения функции управление возвращается обратно в адрес возврата — точку программы, где данная функция была вызвана.

Функция может принимать параметры и должна возвращать некоторое значение, возможно пустое. Функции, которые возвращают пустое значение, часто называют процедурами. В некоторых языках программирования объявления функций и процедур имеют различный синтаксис, в частности, могут использоваться различные ключевые слова.

## Введение

```python
def add(a, b):
    return a + b
```

Для определения функции нужно всего лишь написать ключевое слово `def` перед ее именем, а после — поставить двоеточие. Следом идет блок инструкций.

Cтрока в блоке инструкций может начинаться с `return`, если нужно вернуть какое-то значение. Если инструкции `return` нет, тогда по умолчанию функция будет возвращать объект `None`.

## Вызов

Для вызова функции нужно написать название функции и её аргументы в круглых скобках.

```python
print("arg1", "arg2")
```

Если функция возвращает какое то значение, то его можно использовать как отправив сразу как аргумент другой функции так и запомнить в переменной.

```python
summa = add(1, add(1, 2)) # add(1, add(1, 2)) => add(1, 3) => 4
print(summa) # 4
```

## Инструкция return
### Возврат простого значения

Аргументы можно использовать для изменения ввода и таким образом получать вывод функции. Но куда удобнее использовать инструкцию `return`, примеры которой уже встречались ранее. Если ее не написать, функция вернет значение None.

Эта инструкция может встречаться несколько раз в одной функции и не обязательно в её конце.

### Возврат нескольких значений

Пока что функция возвращала только одно значение или не возвращала ничего (объект None). А как насчет нескольких значений? Этого можно добиться с помощью массива или кортежа. Технически, это все еще один объект. Например:

```python
def stats(data):
    """данные должны быть списком"""
    total = sum(data)
    mean = total / len(data)
    return total, mean # возвращаем x, y — кортеж!

m, v = stats([1, 2, 1])
```

## Рекурсивные функции
Рекурсия — это не особенность Python. Это общепринятая и часто используемая техника в Computer Science, когда функция вызывает сама себя. Самый известный пример — вычисление факториала `n! = n * (n - 1) * (n - 2) * … * 1`. Зная, что `0! = 1`, факториал можно записать следующим образом:

```python
def factorial(n):
    if n != 0:
        return n * factorial(n-1)
    else:
        return 1
```

## Анонимная функция: лямбда

Лямбда-функция — это короткая однострочная функция, которой даже не нужно дававть имя. Такие выражения содержат лишь одну инструкцию, поэтому многострочные конструкции в них  использовать нельзя. Их также можно присваивать переменным, но делать это не рекомендуется.
Но для примера можно.

```python
square = lambda a: a**2
print(square(3))
```