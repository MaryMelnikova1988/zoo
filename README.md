# zoo
проект питомника для собак, который предназначен для демонстрации определенных собак питомника, а также их родословной. 
20.1.11 ORM в Django
Список задач:
 +Создайте новое приложение «Собаки».
 +Опишите модель «Собака» с полями: кличка собаки, порода, фотография, дата рождения.
 +Добавьте модель «Порода» с полями: название, описание.
 +В модели «Собака» замените поле «порода» на ссылку на модель «Порода».
+ В админку выведите список пород, а также список собак.
 +У списка собак добавьте фильтрацию по породам.
 Сформируйте фикстуры для наполнения базы пород и собак.(выполнено сохранение, сначала создав через админку)
Скринкасты с решением задач

/// решение идет через http://127.0.0.1:8000/admin/
через создание: python manage.py createsuperuser
очень важная опция( сохранение кириллицы, как работать с фикстурами): python -Xutf8 manage.py dumpdata dogs -o data_dogs.json
