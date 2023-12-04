# IT Step lesson API

### env-file
В кореневій директорії проекту створіть файл prod.env
Вкажіть у ньому такі змінні:
- SECRET_KEY
- DATABASE_USER
- DATABASE_PASSWORD
- DATABASE_NAME

### Запуск проекту
Щоб запустити проект в консолі введіть команди:
- `docker-compose --env-file=prod.env up -d`
- `docker exec -it app_container_name python db_first_init.py` (при першому запуску, для ініціалізації БД)
