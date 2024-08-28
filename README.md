# Marketing Analytics Project

## Objective
This project aims to centralize and analyze marketing data from various sources to identify the most effective marketing activities in terms of conversion. The analysis will help guide the marketing team in making data-driven decisions for future campaigns.

## Requirements
- Python 3.8+
- PostgreSQL
- Jupyter Notebook
- Mage (for data pipeline orchestration)
- Various Python libraries (see `requirements.txt`)

## Project Structure
- `data/`: Contains raw, processed, and external data
- `notebooks/`: Jupyter notebooks for analysis and visualization
- `src/`: Source code for data processing and feature engineering
- `mage_pipelines/`: Mage data pipeline scripts
- `config/`: Configuration files (e.g., database connection)
- `tests/`: Unit tests for the project
- `requirements.txt`: Python dependencies
- `environment.yml`: Conda environment file

## Setup
1. Clone the repository
2. Create a virtual environment:
   ```
   conda env create -f environment.yml
   ```
   or
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Set up the PostgreSQL database and update `config/database.ini` with your credentials
4. Run the Mage pipeline to populate the database with data from various sources
5. Start Jupyter Notebook and begin your analysis

## Workflow
1. Data Loading: Use the Mage pipeline to collect and centralize data
2. Data Cleaning: Clean and preprocess the data in `02_data_cleaning.ipynb`
3. Feature Engineering: Create relevant features in `03_feature_engineering.ipynb`
4. Exploratory Data Analysis (EDA): Analyze the data in `04_exploratory_data_analysis.ipynb`
5. Insights and Visualization: Generate insights and visualizations in `05_insights_and_visualization.ipynb`

## Contributing
Please follow PEP 8 style guidelines and write unit tests for new functionality.

## License
[Insert your chosen license here]

## Django Setup

1. Copy `core/settings_example.py` to `core/settings.py` and update with your settings.
2. Copy `config/database_example.ini` to `config/database.ini` and update with your database credentials.
3. Run migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Start the development server: `python manage.py runserver`