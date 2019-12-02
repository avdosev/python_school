import datetime


class Taxi:
    rout: str  # Номер маршрута

    stationBegin: str  # Начальный пункт
    stationEnd: str  # Конечный пункт

    cost: int  # расчетная стоимость
    date: datetime.datetime  # время и дата поездки
