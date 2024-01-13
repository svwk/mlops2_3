# Домашнее задание 3

## Автоматизация администрирования MLOps

### Исполнитель: Савоськина С.В.

## Обзор
Проект реализует ML-конвейер для отслеживания количества лайков для одного видеоролика с сервиса Youtube.com с заданным идентификатором.
Он включает скачивание данных, их обработку, подготовку признаков, обучение и применение моделей машинного обучения. 
В проекте используются Airflow для организации задач и MLflow для мониторинга процесса обучения.

## Python скрипты
- **`get_data.py`**: Скачивание данных с помощью `Youtube` API.
- **`process_data.py`**: Обработка и преобразование данных.
- **`train_test_split.py`**: Разделение данных на тренировочный и тестовый наборы.
- **`train_model.py`**: Обучение модели и логирование в MLflow.
- **`inference.py`**: Загрузка обученной модели и оценка ее качества на тестовых данных.

## Airflow
- **DAG**: `youtube_likes_score.py` определяет задачи и их последовательность.
 
- **Конфигурация**:
  - В файле конфигурации изменены два параметра `airflow.cfg`:
    ```
    dags_folder = /home/admin/airflow/dags
    load_examples = False
    ```
  - Перед запуском Airflow установлены переменную окружения:
    ```
    export AIRFLOW_HOME=~/airflow
    ```

## MLflow
- **Логирование**: Параметры, метрики и модели логируются во всех скриптах.
- **Артефакты**: Модели и метрики качества сохраняются для каждого запуска пайплайна.

# Скриншоты работы конвейера
![airflow1.jpg](images%2Fairflow1.jpg)
![airflow2.jpg](images%2Fairflow2.jpg)
![airflow3.jpg](images%2Fairflow3.jpg)
![airflow4.jpg](images%2Fairflow4.jpg)
![airflow5.jpg](images%2Fairflow5.jpg)
![airflow6.jpg](images%2Fairflow6.jpg)
![mlflow1.jpg](images%2Fmlflow1.jpg)
![mlflow2.jpg](images%2Fmlflow2.jpg)
![mlflow3.jpg](images%2Fmlflow3.jpg)
![mlflow4.jpg](images%2Fmlflow4.jpg)
![mlflow5.jpg](images%2Fmlflow5.jpg)
![mlflow6.jpg](images%2Fmlflow6.jpg)