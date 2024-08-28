# Far Capital Analytics

## Project Overview
FarCapital Analytics is a Django-based web application with integrated data pipeline management using Mage and Jupyter notebooks for data analysis.

This project aims to centralize and analyze marketing data from various sources to identify the most effective marketing activities in terms of conversion. The analysis will help guide the marketing team in making data-driven decisions for future campaigns.

## Requirements

- Python 3.8+
- Docker and Docker Compose
- Various Python libraries (see `requirements.txt`)

## Project Structure

- `analytics/`: Django app for analytics models and views
- `core/`: Django project settings and configuration
- `pipelines/`: Mage data pipeline scripts
- `notebooks/`: Jupyter notebooks for analysis and visualization
- `docker-compose.yml`: Docker Compose configuration
- `Dockerfile`: Docker image definition
- `manage.py`: Django management script
- `requirements.txt`: Python dependencies

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/nadeemramli/farcapital-analytics.git
   cd farcapital-analytics
   ```

2. Make sure Docker and Docker Compose are installed on your system

3. Build and start the Docker containers:
   ```
   docker-compose up --build
   ```

4. Run database migrations:
   ```
   docker-compose exec web python manage.py migrate
   ```

5. Create a superuser for Django admin:
   ```
   docker-compose exec web python manage.py createsuperuser
   ```

## Accessing Services

- Django Admin: http://localhost:8000/admin
- Django Application: http://localhost:8000
- Mage UI: http://localhost:6789
- Jupyter Notebook: http://localhost:8888 (check Docker logs for access token)

## Development Workflow

1. **Data Loading**: Use the Mage pipeline to collect and centralize data
2. **Data Analysis**: Use Jupyter Notebooks for data cleaning, feature engineering, and analysis
3. **Django Integration**: Use Django models to store and retrieve processed data

4. Make changes to Django models in `analytics/models.py`
5. Create migrations:
   ```
   docker-compose exec web python manage.py makemigrations
   ```
6. Apply migrations:
   ```
   docker-compose exec web python manage.py migrate
   ```
7. Develop Mage pipelines in the `pipelines/` directory
8. Create and run Jupyter notebooks in the `notebooks/` directory

## Troubleshooting

- If services are not accessible, check Docker logs:
  ```
  docker-compose logs
  ```
- Ensure all required ports are open and not in use by other applications

## Contributing

Please follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines and write unit tests for new functionality.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any queries, please contact [Your Name](mailto:your.email@example.com).