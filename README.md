# Talent-Management System

Welcome to the **Talent-Management System** repository!

This repository contains the source code for the **Talent-Management System** project built using Django version 4.0. It includes instructions on how to create a virtual environment, set up Django, and install all the necessary dependencies using a `requirements.txt` file.

## Getting Started

These instructions will help you set up the project on your local machine.

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the Repository:**
   Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/DilosiRichfield/talent-mgt.git
   ```

2. **Navigate to the Project Directory:**
   ```
   cd talent-mgt
   ```

3. **Create a Virtual Environment:**
   Create a virtual environment to isolate project dependencies. Run the following command:
   ```
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

5. **Install Django:**
   After activating the virtual environment, install Django 4.0 using the following command:
   ```
   pip install django==4.0
   ```

6. **Install Dependencies:**
   Use the `requirements.txt` file to install all project dependencies:
   ```
   pip install -r requirements.txt
   ```

7. **Run Migrations:**
   Apply migrations to set up the database:
   ```
   python manage.py migrate
   ```

8. **Run the Development Server:**
   Start the development server:
   ```
   python manage.py runserver
   ```

9. **Access the Application:**
   Open a web browser and navigate to `http://127.0.0.1:8000/` to access the application.

10. **Deactivate the Virtual Environment:**
    When you're done working on the project, deactivate the virtual environment:
    ```
    deactivate
    ```

## Having Setup Issues?

If you encounter issues during the setup process send me an email: `richiedilosi2003@gmail.com`

---

