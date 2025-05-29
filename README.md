## Тестовое задание Python Developer 
___
### Описание

В данной работе, я реализовал веб-ресурс, 
на котором можно смотреть погоду,
по часам на сегодняшний день в указанном городе.
___
### Технологический стек

- Python 3.11 >=
- Django5
- requests 
- Docker
___

### Запуск приложения

#### 1.
    docker build -t weather_app . 
    
    docker run -p 8000:8000 weather_app

#### 2. 
    docker load < weather_app.tar

    docker run -p 8000:8000 weather_app


Перейти по адресу `http://localhost:8000`
___

Так же можно проверить API по endpoint - `api/stats/`

Отобразит JSON с запросами городов
___
P.S.
HTML и JS сделал с помощью ChatGPT.