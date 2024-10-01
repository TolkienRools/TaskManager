# TaskManager

TaskManager — это веб-приложение для управления задачами, которое позволяет пользователям создавать, редактировать и отслеживать свои задачи и списки задач. Приложение предоставляет удобный интерфейс для организации работы и повышения продуктивности.

## Функциональные возможности

- Создание и удаление списков задач
- Добавление, редактирование и удаление задач
- Установка статуса задач (ожидание, в процессе, завершено, отменено)
- Установка приоритета задач (низкий, средний, высокий)
- Установка сроков выполнения задач
- Аутентификация пользователей

## Технологии

- Python
- Django
- PostgreSQL
- HTML/CSS
- JavaScript

## Установка

### С помощью Docker и Docker Compose

1. Убедитесь, что у вас установлены [Docker](https://www.docker.com/get-started) и [Docker Compose](https://docs.docker.com/compose/install/).

2. Клонируйте репозиторий
3. Запустите контейнеры:

  ```bash
  docker-compose build
  docker-compose up
  ```
4. Откройте браузер и перейдите по адресу http://0.0.0.0:11002/
