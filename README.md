# 🏥 Integrated Patient Care Management System (IPCMS)

A web-based healthcare management system developed using Django to streamline patient, doctor, appointment, consultation, prescription, analytics, and administrative workflows through a centralized platform.

<p align="center">

</p>

**[🌐 Live Demo]((https://ipcms-production.up.railway.app/accounts/login/?next=/dashboard/))** •


---

## 📌 Project Overview

The **Integrated Patient Care Management System (IPCMS)** is a web-based healthcare management application designed to digitally manage essential patient-care activities.

The system provides centralized management of patient information, doctors, appointments, consultations, prescriptions, analytics, and administrative operations.

The project was developed progressively through **four milestones**, covering core management, clinical management, APIs and security-related functionality, followed by analytics, testing, optimization, and final deployment.

### 🎯 Project Objectives

* Digitize patient-care management workflows.
* Centralize patient and healthcare information.
* Simplify appointment and consultation management.
* Manage prescriptions and treatment information.
* Provide dashboard-based analytics and reporting.
* Improve data organization and accessibility.
* Provide a deployed, production-ready project for demonstration.

---

## ✨ Key Features

### 👤 Patient Management

* Add new patient records.
* View patient information.
* Update patient details.
* Delete patient records.
* Maintain medical and contact information.
* Manage emergency contact and blood-group information.

### 👨‍⚕️ Doctor Management

* Add and manage doctor records.
* Store doctor specialization.
* Maintain doctor contact information.
* Associate doctors with healthcare activities.

### 📅 Appointment Management

* Create appointments.
* Assign patients to doctors.
* Manage appointment date and time.
* Track appointment status.
* Prevent conflicting appointment slots for the same doctor.

### 🩺 Consultation Management

* Record patient consultations.
* Store symptoms.
* Record diagnosis.
* Store treatment information.
* Associate consultations with patients and doctors.

### 💊 Prescription Management

* Create prescriptions.
* Store medicine details.
* Record dosage.
* Record treatment duration.
* Associate prescriptions with patients and doctors.

### 📊 Analytics & Dashboard

* Centralized dashboard.
* Healthcare activity statistics.
* Appointment-related analytics.
* Summary metrics for important system activities.
* Visual reporting of healthcare information.

### 🔐 Authentication & Security

* User authentication.
* Authorization and role-based access control.
* Protected application functionality.
* CSRF protection.
* Secure handling of configuration and sensitive information.

### 🔌 REST API

* RESTful API functionality.
* Standard HTTP methods.
* Structured API data exchange.
* Django REST Framework integration.

### 📝 Administrative Management

* Django Admin interface.
* Centralized management of database records.
* Administrative access to project data.

---

## 🏆 Project Milestones

| Milestone       | Scope                                                        | Status      |
| --------------- | ------------------------------------------------------------ | ----------- |
| **Milestone 1** | Patient, Doctor & Appointment Management                     | ✅ Completed |
| **Milestone 2** | Consultation, Diagnosis, Treatment & Prescription Management | ✅ Completed |
| **Milestone 3** | APIs, Authentication, Authorization & Security               | ✅ Completed |
| **Milestone 4** | Analytics, Testing & Optimization                            | ✅ Completed |
| **Deployment**  | Production Deployment                                        | ✅ Completed |

### 🎉 Final Project Status

**Completed and Deployed**

---

## 🛠️ Technology Stack

### Backend

* Python
* Django
* Django REST Framework
* Django ORM

### Frontend

* HTML5
* CSS3
* JavaScript
* Django Templates

### Database

* MySQL

### Authentication & Security

* Django Authentication
* Role-Based Access Control (RBAC)
* JWT-based authentication where implemented
* CSRF protection
* Environment variables

### Deployment

* Railway
* Gunicorn
* WhiteNoise

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

## 🏗️ System Architecture

The application follows the Django **Model-View-Template (MVT)** architecture.

```text
                         ┌─────────────────────┐
                         │        Users        │
                         │ Patient / Doctor /  │
                         │ Admin / Receptionist│
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Web Interface    │
                         │ HTML / CSS / JS     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    URL Routing      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Django Views     │
                         │ Business Logic      │
                         └──────────┬──────────┘
                                    │
                      ┌─────────────┼─────────────┐
                      │             │             │
                      ▼             ▼             ▼
                 Validation      APIs       Authentication
                      │             │             │
                      └─────────────┼─────────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     Django ORM      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │       MySQL         │
                         │      Database       │
                         └─────────────────────┘
```

---

## 🧩 Main Modules

```text
IPCMS
│
├── Patient Management
├── Doctor Management
├── Appointment Management
├── Consultation Management
├── Prescription Management
├── Authentication
├── Authorization / RBAC
├── REST APIs
├── Analytics & Dashboard
├── Testing & Optimization
└── Deployment
```

---

## 🗄️ Database Relationships

The major entities used by the application include:

* User
* Doctor
* Patient
* Appointment
* Consultation
* Prescription
* Receptionist

Major relationships include:

```text
User
 │
 └── Doctor

Patient
 ├── Appointments
 ├── Consultations
 └── Prescriptions

Doctor
 ├── Appointments
 ├── Consultations
 └── Prescriptions
```

The application uses Django ORM relationships such as `OneToOneField` and `ForeignKey` to maintain relationships between entities.

---

## 🔌 REST API

The project includes REST API functionality using **Django REST Framework**.

The API layer supports standard HTTP operations such as:

```text
GET       Retrieve data
POST      Create data
PUT       Update data
DELETE    Delete data
```

Example API structure:

```text
GET     /api/patients/
POST    /api/patients/
PUT     /api/patients/<id>/
DELETE  /api/patients/<id>/
```

The API provides structured data exchange between clients and the backend application.

---

## 🔐 Authentication & Authorization

The system separates **authentication** and **authorization**.

* **Authentication** verifies the identity of a user.
* **Authorization** determines what an authenticated user is allowed to access.
* **RBAC** allows access permissions to be associated with user roles.

Security considerations include:

* Authentication and authorization.
* CSRF protection.
* Secure environment configuration.
* Protected application functionality.
* Production configuration.

---

## 📊 Analytics Dashboard

The completed dashboard provides a centralized view of important healthcare activities.

The dashboard includes summary information such as:

* Upcoming Appointments
* Completed Appointments
* Active Prescriptions
* Medical Records
* Pending Lab Tests
* Notifications

The analytics section provides visual information to help users understand appointment activity and other important healthcare statistics.

---

## 🧪 Testing

The completed project was tested across major application workflows.

Testing areas include:

* Patient CRUD operations.
* Doctor CRUD operations.
* Appointment CRUD operations.
* Consultation CRUD operations.
* Prescription CRUD operations.
* Form submission and validation.
* Database operations.
* Authentication and authorization.
* API functionality.
* Dashboard functionality.
* Deployed application functionality.

Testing was performed to identify and resolve functional, database, template, and workflow-related issues.

---

## ⚡ Optimization

Optimization and final project refinement focused on:

* Efficient database interaction.
* Proper Django ORM usage.
* Database relationship handling.
* Static-file management.
* Production configuration.
* Secure environment-variable usage.
* Application maintainability.
* Deployment readiness.

---

## 📁 Project Structure

```text
IPCMS/
│
├── ipcms_project/
│   ├── hospital/
│   ├── ipcms_project/
│   ├── manage.py
│   └── ...
│
├── screenshots/
│   ├── login.png
│   ├── dashboard.png
│   ├── patients.png
│   ├── doctors.png
│   ├── appointments.png
│   ├── consultations.png
│   ├── prescriptions.png
│   ├── analytics.png
│   └── admin.png
│
├── docs/
│   └── IPCMS_Project_Documentation.pdf
│
├── .gitignore
├── README.md
├── requirements.txt
└── ...
```

> The structure above represents the major project components. Additional Django files and configuration files are omitted for readability.

---

## 📚 Project Documentation

The complete project documentation is available as a PDF.

The documentation contains detailed information about the project, including its objectives, functionality, implementation, technologies, testing, and deployment.

---

## 🚀 Deployment

The completed application has been deployed using **Railway**.

### Production Components

* Django application
* Gunicorn application server
* WhiteNoise for static-file handling
* MySQL database
* Environment-based configuration
* Production deployment configuration

### 🌐 Live Application

**[🚀 Open the Deployed IPCMS Application](https://ipcms-production.up.railway.app/accounts/login/?next=/dashboard/)**

---

## ⚙️ Local Installation

### 1. Clone the repository

```bash
git clone https://github.com/roy07barsha/IPCMS.git
cd IPCMS
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file and provide the required configuration values.

Example:

```env
SECRET_KEY=your_secret_key
DEBUG=False
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port
```

> Never commit the `.env` file or real credentials to GitHub.

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Create an administrator

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🔮 Future Enhancements

Possible future improvements include:

* Advanced patient medical timeline.
* Automated appointment reminders.
* Email/SMS notification integration.
* Enhanced reporting.
* Doctor availability scheduling.
* Prescription PDF generation.
* Advanced security monitoring.
* Additional healthcare workflow modules.

---

## 👩‍💻 Author

### Barsha Roy

**BCA Student**
Future Institute of Engineering and Management

GitHub: [@roy07barsha](https://github.com/roy07barsha)

---

## 📄 License

This project is developed as an academic and educational project.

If a specific open-source license is added to the repository, the license information should be updated here accordingly.

---

## ⭐ Project Status

> **IPCMS — Integrated Patient Care Management System**
>
> **Milestones 1–4 Completed • Tested • Optimized • Deployed**

---
