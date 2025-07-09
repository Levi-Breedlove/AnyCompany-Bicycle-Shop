# AnyCompanyBicycleShop
# Django Bicycle Parts E-commerce Application

This project is a Django-based e-commerce application for selling bicycle parts. It provides functionality for managing products, orders, and customer interactions in a bicycle parts online store.

The application is designed to run on AWS infrastructure, utilizing services such as RDS for the database and S3 for static file storage.

## Repository Structure

```
.
├── JSON
|    └── Json-S3.txt
├── anycompany_bicycle_parts_files
│   └── list of images 
├── django
│   ├── bicycle_app
|   |   ├── __init__.py
|   |   ├── models.py
|   |   ├── templates/
|   |   ├── urls.py
|   |   └── views.py
│   |── bicycle_project
├   |   ├── __init__.py
|   |   ├── asgi.py
|   |   ├── settings.py
|   |   ├── urls.py
|   |   └── wsgi.py
│   ├── static
|   |    ├── admin
|   |    └──css
│   ├── db.sqlite3
│   ├── manage.py
│   ├── rear-light.jpeg
|   └── requirements.txt
├── .gitignore
├── README.md
├── anycompany_bicycle_parts_website.html
│── order_details.json
│── orders.json
│── products.json
└── setup.sh
```

### Key Files:
- `setup.sh`: Script for setting up the Django project and configuring the environment
- `django/bicycle_project/settings.py`: Main Django settings file
- `products.json`: Sample product data
- `orders.json`: Sample order data
- `order_details.json`: Sample order details data

### Important Integration Points:
- Database: MySQL database hosted on Amazon RDS
- Static Files: Stored on Amazon S3

## Infrastructure

The application utilizes the following AWS resources:

- EC2: Hosts the Django application
- RDS: MySQL database for storing product and order information
- S3: Stores static files and media uploads
- Elastic Beanstalk: Manages the application deployment and scaling

## Architecture Diagram


![Django Bicycle Parts E-commerce Application Architecture](./django/static/websitearchitecture.png)


This diagram illustrates the high-level architecture of the Django Bicycle Parts E-commerce Application. It shows how the different AWS services (EC2, RDS, S3, and Elastic Beanstalk) interact with the Django application to provide a scalable and robust e-commerce platform for selling bicycle parts. 



## Usage Instructions

### Installation

Prerequisites:
- Python 3.10+
- MySQL client libraries

1. Clone the repository
2. Run the setup script:
   ```
   ./setup.sh
   ```
   This script will:
   - Create a virtual environment
   - Install Django and other dependencies
   - Set up the Django project structure
   - Configure the database connection

### Configuration

1. Update `django/bicycle_project/settings.py` with your specific settings:
   - Set `DATABASES` configuration to point to your RDS instance
   - Configure `AWS_STORAGE_BUCKET_NAME` and `AWS_S3_REGION_NAME` for S3 static file storage

2. Set up environment variables:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`

### Running the Application

1. Activate the virtual environment:
   ```
   source django/.venv/bin/activate
   ```

2. Run migrations:
   ```
   python manage.py migrate
   ```

3. Load sample data:
   ```
   python manage.py loaddata products.json orders.json order_details.json
   ```

4. Start the development server:
   ```
   python manage.py runserver
   ```

5. Access the application at `http://localhost:8000`

### Deployment

The application is designed to be deployed on AWS Elastic Beanstalk. Follow these steps:

1. Install the Elastic Beanstalk CLI
2. Initialize your EB environment:
   ```
   eb init -p python-3.10 bicycle-parts-app
   ```
3. Create the environment:
   ```
   eb create bicycle-parts-env
   ```
4. Deploy your application:
   ```
   eb deploy
   ```

## Data Flow

1. User requests arrive at the Django application.
2. Django processes the request, interacting with the MySQL database on RDS as needed.
3. For product images and static files, Django interacts with the configured S3 bucket.
4. The response is generated and sent back to the user.

```
[User] <-> [Django App] <-> [RDS MySQL]
                 ^
                 |
                 v
            [S3 Bucket]
