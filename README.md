# LAB - Class 28

## Project: Django CRUD and Forms

### Author: Michelangelo Ascalon

## Overview
This project is designed to add full CRUD (Create, Read, Update, Delete) functionality to a Django application. By building this project, users can learn how to implement CRUD operations using Django's powerful features, including its ORM (Object-Relational Mapping), forms, and class-based views. This application manages a "Snacks" database, allowing users to add, view, update, and delete snack items.

### Links and Resources
- [Django Documentation](https://docs.djangoproject.com/en/3.2/)

### Setup

Requirements

- Python 3.8 or later
- Django 3.2 or later

#### Installation

To set up the project environment, run the following commands:

Install the required packages
pip install -r requirements.txt

Running the Application
To run the application, use the following command:

```gitbash
python manage.py runserver
```
This will start the Django development server, and the application will be available at http://127.0.0.1:8000/.

#### How to Use the Application

Navigate to the application URL in your web browser. You'll be presented with a list of snacks. From here, you can:

* Click on a snack to view its details.

* Use the "Add New Snack" link to create a new snack entry.
  
* On the detail page of a snack, use the "Update" button to modify the snack's information or the "Delete" button to remove the snack from the database.
  
#### Tests

How to Run Tests

To run tests, execute the following command:

```gitbash
python manage.py test
```

Notable Tests

* Test model string representation to ensure it correctly displays the snack title.

* Test views for list, detail, create, update, and delete functionality to confirm they're working as expected.