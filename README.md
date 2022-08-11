# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

![image](https://user-images.githubusercontent.com/58893102/184070333-67e71f10-796f-417c-8005-bbed38e0e8be.png)

### Описание

Скрипт забирает данные с Excel-файла ```wine.xlsx```(файл-образец):
![image](https://user-images.githubusercontent.com/58893102/184127762-0bf4a592-24e2-4d3e-9ba6-a785f1f1850d.png)


После скрипт изменяет шаблон ```template.html```.
В результате создаётся страничка index.html, которая и запускается по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Запуск
* Скачайте код
* Установите зависимости командой 
  
  > pip install -r requirements.txt

* Создайте файл базы данных и сразу примените все миграции командой python3 manage.py migrate.
* Запустите сервер командой:

  > python main.py

* Перейдите на сайт по адресу - [http://127.0.0.1:8000](http://127.0.0.1:8000).

