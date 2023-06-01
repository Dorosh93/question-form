# Форма для вопросов на День Директора

Форма сделана по направленному ТЗ.
В базе созданы 4 дивизиона, компании (к 3 дивизионам из 4), вопросы от компаний.

Доступ к форме задания вопроса осуществляется по пути "/".
К формам таблиц по пути "result/".

Доступ к "админке" "admin/": Username: admin, Password: password.

## Загрузка базы и запуск приложения

Cоздать и активировать виртуальное окружение:

```
python -m venv venv

source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в основную папку и выполнить миграции:

```
cd  questionform

python manage.py migrate
```

Заполненить базу данных из db.json:

```
python manage.py loaddata db.json
```

Запустить проект:

```
python manage.py runserver
```

#
Разработал Виктор Дорошенко
