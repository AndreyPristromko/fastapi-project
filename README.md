# FastAPI Project

Этот проект включает два микросервиса на базе FastAPI:
1. ShortURL-сервис — позволяет сокращать длинные URL и предоставлять статистику.
2. TODO-сервис — позволяет управлять списком задач.

---

## 1. ShortURL-сервис

### Описание
Сервис для создания коротких ссылок, перенаправления по ним и получения статистики переходов.

### Эндпоинты
- `POST /shorten`  
  **Описание:** Создать короткую ссылку для указанного URL.  
  **Пример запроса:**
  
  ```json
  {
    "url": "https://example.com"
  }
  ```
  
  **Пример ответа:**
  
  ```json
  {
    "short_id": "abc123",
    "full_url": "https://example.com"
  }
  ```
  
- `GET /{short_id}`
  **Описание:** Получение статистики переходов по короткой ссылке.
  **Пример ответа:**
  
  ```json
  {
    "redirect_to": "https://example.com"
  }
  ```
  
- `GET /stats/{short_id}`
  **Описание:** Получение статистики переходов по короткой ссылке.
  **Пример ответа:**
  
  ```json
  {
    "full_url": "https://example.com",
    "clicks": 10
  }
  ```
### Запуск через Docker
 Соберите Docker-образ:
   ```bash
    docker build -t shorturl-service ./shorturl_app
   ```
 Запустите контейнер:
   ```bash
    docker run -d -p 8001:80 -v shorturl_data:/app/data --name shorturl-service shorturl-service
   ```
## 2. TODO-сервис

### Описание
Сервис для управления списком задач: добавление, чтение, обновление и удаление задач.

### Эндпоинты
- `POST /items`  
  **Описание:** Создать новую задачу.  
  **Пример запроса:**
    
  ```json
  {
    "title": "Купить продукты",
    "description": "Молоко, хлеб, сыр",
    "completed": false
  }
  ```
  
  **Пример ответа:**
  
  ```json
  {
    "id": 1,
    "title": "Купить продукты",
    "description": "Молоко, хлеб, сыр",
    "completed": false
  }
  ```
  
- `GET /items`
  **Описание:** Получить список всех задач.
  **Пример ответа:**
  
  ```json
  [
    {
      "id": 1,
      "title": "Купить продукты",
      "description": "Молоко, хлеб, сыр",
      "completed": false
    }
  ]
  ```
  
- `GET /items/{item_id}`
  **Описание:** Получить задачу по её ID.
  **Пример ответа:**
  
  ```json
  {
    "id": 1,
    "title": "Купить продукты",
    "description": "Молоко, хлеб, сыр",
    "completed": false
  }
  ```
  
- `PUT /items/{item_id}`  
  **Описание:** Обновить задачу по её ID.  
  **Пример запроса:**
  
  ```json
  {
    "title": "Купить продукты и напитки",
    "description": "Молоко, хлеб, сыр, вода",
    "completed": true
  }
  ```
  
  **Пример ответа:**
  
  ```json
  {
    "message": "Task updated successfully"
  }
  ```
  
- `DELETE /items/{item_id}`
  **Описание:** Удалить задачу по её ID.
  **Пример ответа:**
  
  ```json
  {
    "message": "Task deleted successfully"
  }
  ```
  
### Запуск через Docker
Соберите Docker-образ:
  ```bash
   docker build -t todo-service ./todo_app
  ```
Запустите контейнер:
  ```bash
   docker run -d -p 8000:80 -v todo_data:/app/data --name todo-service todo-service
  ```

## Ссылки на образы Docker
- ShortURL-сервис: https://hub.docker.com/r/andreypristromro/shorturl-service
- TODO-сервис: https://hub.docker.com/repository/docker/andreypristromro/todo-service
