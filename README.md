# Integrated Patient Care Management System (IPCMS)

A web-based hospital management system developed using Django and MySQL to manage patient information, doctors, appointments, consultations, prescriptions, receptionists, and system audit records.

## 📌 Project Overview

The **Integrated Patient Care Management System (IPCMS)** is designed to provide a centralized platform for managing essential hospital and patient-care operations.

The system helps authorized users manage patient records, doctor information, appointments, consultations, prescriptions, and other administrative activities through a web-based interface.

## ✨ Features

* 🔐 User authentication and login management
* 👨‍⚕️ Doctor management
* 🧑‍🤝‍🧑 Patient management
* 📅 Appointment scheduling and management
* 🩺 Consultation record management
* 💊 Prescription management
* 👩‍💼 Receptionist management
* 🛡️ Role-Based Access Control (RBAC)
* 📋 Audit logging for system activities
* 📊 Dashboard for hospital management information
* 🗄️ MySQL database integration
* 🔒 Security-focused Django configuration

## 🛠️ Technology Stack

### Backend

* Python
* Django

### Frontend

* HTML
* CSS
* JavaScript
* Django Templates

### Database

* MySQL

### Development Tools

* Visual Studio Code
* Git
* GitHub

## 🏗️ System Modules

### Patient Management

Manage patient information including:

* Patient ID
* Name
* Date of birth
* Age
* Gender
* Phone number
* Blood group
* Emergency contact
* Medical history

### Doctor Management

Manage doctor information including:

* Doctor account
* Specialization
* Contact information

### Appointment Management

Manage appointments between patients and doctors, including:

* Appointment date
* Appointment time
* Doctor
* Patient
* Appointment status

The system also prevents duplicate appointments for the same doctor, date, and time.

### Consultation Management

Store consultation information including:

* Patient
* Doctor
* Symptoms
* Diagnosis
* Treatment

### Prescription Management

Maintain prescription records including:

* Patient
* Doctor
* Medicine
* Dosage
* Duration

### Receptionist Management

Manage receptionist information and contact details.

### Audit Logging

The system includes an audit log module for recording important system activities, including:

* User
* Action
* Model
* Object ID
* Timestamp

## 🔐 Security

IPCMS uses Django's built-in security and authentication mechanisms along with role-based access control.

Production security settings such as HTTPS redirection, secure cookies, HSTS, and `DEBUG = False` are intended to be configured when the application is deployed to a production environment.

> **Note:** Do not place database passwords, Django secret keys, API keys, `.env` files, or other sensitive credentials in the repository.

## 💻 Local Development Setup

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd ipcms_project
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure the database

Create a MySQL database for the project and configure the database credentials in Django's settings.

Do not commit database passwords or other sensitive credentials to GitHub.

### 5. Apply migrations

```powershell
python manage.py migrate
```

### 6. Create a superuser

```powershell
python manage.py createsuperuser
```

### 7. Run the development server

```powershell
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## 📁 Project Structure

```text
ipcms_project/
│
├── hospital/
│   ├── migrations/
│   ├── management/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── ipcms_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── templates/
├── static/
├── manage.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## 🚀 Deployment

The project is currently maintained as a development-stage Django application.

Production deployment will require appropriate configuration for:

* Production database
* Environment variables
* `ALLOWED_HOSTS`
* Static files
* HTTPS/SSL
* Production security settings
* Web server / WSGI configuration

## 👩‍💻 Project

**Integrated Patient Care Management System (IPCMS)**

Developed as a Django-based hospital management project.

## 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.
