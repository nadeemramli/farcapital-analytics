# Marketing Analytics Project

## Objective

This project aims to centralize and analyze marketing data from various sources to identify the most effective marketing activities in terms of conversion. The analysis will help guide the marketing team in making data-driven decisions for future campaigns.

## Requirements

- Python 3.8+
- Docker and Docker Compose
- Various Python libraries (see `requirements.txt`)

## Project Structure

- `analytics/`: Django app for analytics models and views
- `core/`: Django project settings and configuration
- `marketing_pipelines/`: Mage data pipeline scripts
- `notebooks/`: Jupyter notebooks for analysis and visualization
- `docker-compose.yml`: Docker Compose configuration
- `Dockerfile`: Docker image definition
- `manage.py`: Django management script
- `requirements.txt`: Python dependencies

## Setup

1. Clone the repository
2. Make sure Docker and Docker Compose are installed on your system
3. Build the Docker images:
   ```
   docker-compose build
   ```
4. Start the services:
   ```
   docker-compose up
   ```

## Accessing Services

- Django: http://localhost:8000
- Jupyter Notebook: http://localhost:8888
- Mage: http://localhost:6790

## Workflow

1. **Data Loading**: Use the Mage pipeline to collect and centralize data
2. **Data Analysis**: Use Jupyter Notebooks for data cleaning, feature engineering, and analysis
3. **Django Integration**: Use Django models to store and retrieve processed data

## Django Setup

1. Run migrations:
   ```
   docker-compose run web python manage.py migrate
   ```
2. Create a superuser:
   ```
   docker-compose run web python manage.py createsuperuser
   ```

## Contributing

Please follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines and write unit tests for new functionality.

## License

[MIT License](LICENSE)

## Contact

For any queries, please contact [Your Name](mailto:your.email@example.com).