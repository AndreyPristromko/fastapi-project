# FastAPI Project

Этот проект включает два микросервиса на базе FastAPI:
1. ShortURL-сервис — позволяет сокращать длинные URL и предоставлять статистику.
2. TODO-сервис — позволяет управлять списком задач (CRUD-операции).

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
  1. Соберите Docker-образ:
    ```bash
    docker build -t shorturl-service ./shorturl_app
    ```
  1. Запустите контейнер:
    ```bash
    docker run -d -p 8001:80 -v shorturl_data:/app/data --name shorturl-service shorturl-service
    ```  
