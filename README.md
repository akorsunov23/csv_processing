# Обработка данных .csv файла


## Установка и запуск:

* Клонировать репозиторий
```sh
git clone https://github.com/akorsunov23/csv_processing.git 
```
* Перейти в проект

```sh
cd csv_processing/
```
* Переименовть файл .env.template в .env и добавить недостающие параметры
* Запустить сборку и запуск контейнера

```sh
docker compose up --build
```
* Для добавление суперпользователя можно воспользоваться командой

```sh
docker compose exec web python manage.py createsuperuser
```
* Для удаления контенера 

```sh
docker compose down -v
```

-------------------------------
## Описание проекта:
После запуска проекта он будет доступен по адресу: http://localhost:7000/.


API имеет два метода, загрузка, обработка и запись в БД .csv файла и получение данных из БД о покупателях потративших наибольшую сумму на покупки камней.

* POST - загрузка с дальнейшей обработкой файла deals.csv без сохранения на сервере (находится в корне проекта.)
```sh
/api/v1/load_csv/
```
* GET - получение списка покупателей. На данном методе реализовано кэширование через Redis и при добавление либо удалении записей в БД кэш удаляется. Также добавлены сигналы, реагирующие на одиночные изменения в БД.
```sh
/api/v1/favorites/
```
* GET - документация REDOC
```sh
/api/v1/docs/
```
