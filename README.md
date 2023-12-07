# IT Step lesson API

### env-file
В кореневій директорії проекту створіть файл prod.env
Вкажіть у ньому такі змінні:
- SECRET_KEY
- DATABASE_HOST
- DATABASE_USER
- DATABASE_PASSWORD
- DATABASE_NAME

DATABASE_HOST це назва контейнера БД, скоріш за все, за замовчуванням буде it_step_db_1.
Інші значення змінних можна заповнити довільно

### Запуск проєкту
Щоб запустити проєкт в консолі введіть команди:
- `docker-compose --env-file=prod.env up -d`
- `docker exec -it app_container_name python db_first_init.py` (При першому запуску, для ініціалізації БД. app_container_name замінити на відповідне значення)
