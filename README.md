# Theranostics Databank

A comprehensive web application for managing patient data in theranostic treatment, developed using Django framework.

## Features

- Patient Management
  - Add, edit, and view patient details
  - Track diagnosis dates, surgery dates, and treatment information
  - Record histopathology results and Gleason scores

- Physical Examination
  - Record and monitor physical exam data
  - Automatic BMI calculation based on height and weight
  - Track vital signs and symptoms

- Screening Management
  - Record PSA, blood tests, and other laboratory results
  - Track imaging results (GA PSMA, FDG PET/CT)
  - Document lesion details with location, SUV, and size measurements

- Follow-up Management
  - Track patient progress over time
  - Monitor changes in test results and imaging findings
  - Document assessments and treatment plans

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- Git
- PostgreSQL (recommended) or SQLite

## Dependencies

The project uses the following main dependencies:
- Django 4.2.5
- django-crispy-forms 2.0
- crispy-bootstrap4 2022.1
- Pillow 10.0.0 (for image handling)
- django-bootstrap-modal-forms 3.0.4
- psycopg2-binary 2.9.7 (for PostgreSQL)
- whitenoise 6.5.0 (for static files)

For a complete list of dependencies, see `requirements.txt`.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hi191-grp4-theranostics.git
cd hi191-grp4-theranostics
```

2. Create a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Configure the database:
   - By default, the project uses SQLite
   - To use PostgreSQL:
     - Create a PostgreSQL database
     - Update DATABASES in settings.py
     - Install psycopg2-binary (included in requirements.txt)

5. Set up the database:
```bash
python manage.py makemigrations part_1
python manage.py makemigrations part_4
python manage.py migrate
```

6. Create a superuser (admin account):
```bash
python manage.py createsuperuser
```
Follow the prompts to set up your admin username and password.

7. Collect static files:
```bash
python manage.py collectstatic
```

## Running the Application

1. Start the development server:
```bash
python manage.py runserver
```

2. Open your web browser and navigate to:
- Main application: `http://127.0.0.1:8000/`
- Admin interface: `http://127.0.0.1:8000/admin/`

## Testing the Application

### Testing Patient Management

1. Adding a New Patient:
   - Click "Add Patient" on the home page
   - Fill in required fields:
     - Patient name
     - Age
     - Address
     - Diagnosis date
     - Surgery date (if applicable)
     - Histopathology details
     - Treatment information

2. Editing Patient Details:
   - Navigate to patient details
   - Click "Edit" button
   - Modify information as needed
   - Save changes

### Testing Physical Examination

1. Adding Physical Exam:
   - Navigate to patient details
   - Click "Add Physical Exam"
   - Enter height and weight (BMI will calculate automatically)
   - Fill in other vital signs and symptoms
   - Save the exam

2. Editing Physical Exam:
   - Find the physical exam record
   - Click "Edit"
   - Update measurements and observations
   - Verify BMI updates automatically

### Testing Screening

1. Adding Screening Results:
   - Navigate to patient details
   - Click "Add Screening"
   - Enter laboratory results
   - For imaging sections (GA PSMA, FDG PET/CT):
     - Set lesion status for each organ
     - If "Present", fill in location, SUV, and size
     - If "Absent", verify fields are disabled
   - Complete assessment and plan (required)

2. Editing Screening:
   - Locate screening record
   - Click "Edit"
   - Modify results as needed
   - Verify lesion fields behave correctly based on status

### Testing Follow-up

1. Adding Follow-up:
   - Navigate to patient details
   - Click "Add Follow-up"
   - Enter follow-up date
   - Update test results and imaging findings
   - Complete assessment and plan

2. Editing Follow-up:
   - Find follow-up record
   - Click "Edit"
   - Update information
   - Save changes

## Common Issues and Solutions

1. Database Migration Issues:
```bash
# Reset migrations if needed
python manage.py migrate --fake part_1 zero
python manage.py migrate --fake part_4 zero
python manage.py makemigrations
python manage.py migrate
```

2. Static Files Not Loading:
```bash
# Collect static files
python manage.py collectstatic

# Verify STATIC_ROOT and STATIC_URL in settings.py
# Ensure whitenoise is in MIDDLEWARE
```

3. Image Upload Issues:
```bash
# Verify MEDIA_ROOT and MEDIA_URL in settings.py
# Check file permissions in media directory
# Ensure Pillow is installed correctly
```

4. Permission Issues:
- Ensure you're logged in as admin
- Check user permissions in Django admin interface
- Verify file permissions for media and static directories

## Project Structure

```
hi191-grp4-theranostics/
├── manage.py
├── requirements.txt
├── README.md
├── theranostics/          # Main project directory
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── part_1/               # Patient and screening management
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── part_4/               # Follow-up management
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── templates/            # HTML templates
│   ├── part_1/
│   └── part_4/
├── static/              # Static files (CSS, JS, images)
└── media/              # User-uploaded files
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support:
1. Check the documentation
2. Review common issues above
3. Open an issue in the GitHub repository
4. Contact the development team

## Acknowledgments

- Django Framework and its contributors
- Bootstrap for the frontend framework
- All contributors to the project
