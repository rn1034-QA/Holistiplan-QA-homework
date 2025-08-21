**Holistiplan QA Project**

This repository contains automated tests for the Holistiplan Rewards web application, built using Python and Playwright. The application itself runs in Docker containers.

**Getting Started**

Follow these steps to set up the project and run the automated tests locally.

**Prerequisites**

Before you begin, ensure you have the following installed on your machine:
    -Docker Desktop: Essential for running the Holistiplan Rewards application.
        Download Docker Desktop
    -Python 3.9+: For running the Playwright tests.
        Download Python
    -Git: For cloning this repository.

**Setup Instructions**

1. Clone the Repository:
Open your Terminal and clone this repository to your local machine:

git clone https://github.com/rn1034-QA/Holistiplan-QA-homework.git 
cd Holistiplan-QA-homework

2. Create ```.env.local``` File:
The application needs environment variables. Create a file named ```.env.local``` inside the ```qa_homework``` directory.

cd qa_homework
touch .env.local

Then, open this newly created ```.env.local``` file in a text editor (like VS Code) and paste the following content:

```SECRET_KEY=a_very_secret_key_that_you_should_change_for_production_if_this_were_a_real_app
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=*
POSTGRES_DB=holistiplan_db
POSTGRES_USER=holistiplan_user
POSTGRES_PASSWORD=holistiplan_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
EMAIL_HOST=mailhog
EMAIL_PORT=1025
DEFAULT_FROM_EMAIL=webmaster@localhost
```

Save the file.

3. Start the Holistiplan Application with Docker Compose:
Ensure Docker Desktop is running. In your Terminal (still in the qa_homework directory):

```docker-compose -f local.yml up --build -d```

Allow a minute or two for all services to start up. You can check their status:

```docker-compose ps```

All services (django, db, mailhog) should show Up.

4. Install Python Dependencies:
While still in the qa_homework directory, install the necessary Python libraries for testing:

```pip3 install -r requirements/local.txt```

5. Install Playwright Browsers:
This downloads the browsers (Chromium, Firefox, WebKit) that Playwright uses for testing:

```playwright install```

**Running Automated Tests**
Once the Holistiplan application is running in Docker and all Python/Playwright dependencies are installed, you can execute the tests.

1. Verify Application is Accessible:
Open your web browser and navigate to http://localhost:8000. Confirm that you see the Holistiplan Rewards login page or homepage. If you encounter any connection errors here, resolve them before running tests.

2. Run the Tests:
In your Terminal (still in the qa_homework directory):

```python3 -m pytest test_rewards_2.py```

The tests will run in a browser, and the results will be displayed in your terminal.

Common Troubleshooting Tips
net::ERR_EMPTY_RESPONSE or Connection Errors: This almost always means the Docker application is not fully running or accessible. Re-run docker-compose -f local.yml up --build -d, wait, and then check docker-compose ps and http://localhost:8000 in your browser.

Locator expected to be visible or TimeoutError:

Ensure your Docker app is fully loaded and responsive.

The element might not be present, its text/selector might be slightly different, or it's hidden. Use Playwright's --headed mode (python3 -m pytest test_rewards_2.py --headed) to visually debug.

ModuleNotFoundError: No module named 'django': Ensure you are running pytest from the qa_homework directory, and that you have Django installed in your local Python environment (pip3 install Django).

