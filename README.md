# Weather Data Parser

Python-скрипт для получения текущих данных о погоде для списка городов с помощью API [wttr.in](https://wttr.in/).

## Возможности

- чтение списка городов из файла `cities.txt`;
- удаление дубликатов городов;
- получение текущей температуры и страны для каждого города;
- вывод информации о погоде;
- группировка городов по странам;
- расчёт количества городов и средней, минимальной и максимальной температуры для каждой страны.

## Используемые технологии

- Python 3
- JSON
- wttr.in API

Используются только стандартные возможности Python. Дополнительные Python-пакеты устанавливать не требуется.

## Структура проекта

```text
weather-data-parser/
├── cities.txt
├── weather_scrypt.py
└── README.md
```
## Установка и запуск
### 1. Клонирование репозитория
git clone https://github.com/USERNAME/weather-data-parser.git
cd weather-data-parser
### 2. Подготовка списка городов

В файл cities.txt необходимо добавить названия городов, по одному на строку:

Moscow
Khabarovsk
Saint-Petersburg
Vienna
Izhevsk
Perm
NhaTrang
Villach
### 3. Запуск
python weather_scrypt.py

Для работы программы требуется подключение к интернету.

Пример результата
Погода по городам:

Izhevsk, Russia +10 °C
Khabarovsk, Russia +8 °C
Moscow, Russia +12 °C
Perm, Russia +9 °C
Saint-Petersburg, Russia +8 °C
Vienna, Austria +14 °C
Villach, Austria +13 °C
NhaTrang, Vietnam +28 °C

Статистика по странам:

Austria - 2 cities, avg: +14 °C, min: +13 °C, max: +14 °C
Russia - 5 cities, avg: +9 °C, min: +8 °C, max: +12 °C
Vietnam - 1 cities, avg: +28 °C, min: +28 °C, max: +28 °C

Значения температуры меняются в зависимости от текущей погоды.
