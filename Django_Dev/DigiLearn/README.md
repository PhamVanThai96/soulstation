## https://www.virtono.com/community/tutorial-how-to/how-to-install-django-on-linux/
## https://www.w3schools.com/django/django_install_django.php


Section 1: Preparing Your Linux Environment

    Before installing Django on Linux, let’s ensure your Linux environment is ready. Follow these steps to set up the necessary dependencies:

    Update Your System:

    To begin, open a terminal and run the following command to update your system:

        'sudo apt update && sudo apt upgrade'

    Install Python:

        Django on Linux is built with Python, so make sure it’s installed on your Linux machine. Run the following command to install Python:

        'sudo apt install python3'

    Install Pip:

        'sudo apt install python3-pip'

Section 2: Installing Django on Linux depend on your python version - should create virtual environment for each project

    Create a Virtual Environment:

        'apt install python3.10-venv'
        'python3 -m venv myenv'

    Activate the Virtual Environment:

        For Bash/Zsh: source myenv/bin/activate

        For Fish: . myenv/bin/activate.fish

        For Csh/Tcsh: source myenv/bin/activate.csh

    Install Django on Linux:

        'pip install django'

    Verify the Installation:

        'python -m django --version'

        */ If the version is displayed, congratulations! Django on Linux is installed correctly.

Section 3: Creating Your First Django Project

    Start a New Django Project:

        'django-admin startproject soulstation'
        'cd soulstation'

    Run the Development Server:

        'python manage.py migrate'
        'python manage.py runserver 0.0.0.0:8000'

    Add allowed host in setting.py:

        ALLOWED_HOSTS = [
            '8000-abc.xyz.com',
        ]

    Create web application or each web page or feature:

        'python3 manage.py startapp members'

    Lets update urlpartern startapp and template:

        path('members/', views.members, name='members'),
        path('', include('members.urls')),

    Access Your Django Application:

        Open a web browser and visit http://you-server-IP:8000/. If you see the default Django landing page, your application is running successfully.

        http://127.0.0.1:8001/members/
        http://127.0.0.1:8001/solveproblem/


Section 4: Setting up a Database

    Django supports various databases, and you can choose the one that suits your project requirements. Here’s an example of setting up a PostgreSQL database:

    Install PostgreSQL or can use LiteSQL as default:

        'sudo apt install postgresql'

    Create a Database in PostgreSQL:

        'sudo su - postgres'
        'createdb mydatabase'

    Migrate database LiteSQL:

        'python3 manage.py makemigrations members'
        
        'python3 manage.py migrate'

    View SQL:

        'python3 manage.py sqlmigrate member 001'



Create a new user:

Once you are in the PostgreSQL command-line interface, run the following command to create a new user:

sudo -u postgres psql
CREATE USER your_username WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_username;

Update Django Settings:

In your Django project directory, open the settings.py file and locate the DATABASES section. Update it as follows:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

Section 5: Additional Django Configuration

    Creating a Superuser:

        'python manage.py createsuperuser'

    Use python shell to add records"

        'python manage.py shell'

    Modifying Allowed Hosts:

        By default, Django only allows requests from localhost. To allow requests from your domain or IP address, open the settings.py file and locate the ALLOWED_HOSTS list. Add your domain or IP address to the list, like this:

        ALLOWED_HOSTS = ['yourdomain.com', 'your_ip_address']
