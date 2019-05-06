import os

try:
    # settings initialized from environment goes here
    SECRET_KEY_VALUE = os.environ["SECRET_KEY_VALUE"]
    # Check if environment staging
    if os.environ["APP_ENVIRONMENT"] == "staging":
        DEBUG_VALUE = os.environ["DEBUG_VALUE"]
    else:
        DEBUG_VALUE = "false"

    ALLOWED_HOSTS_VALUE = os.environ["ALLOWED_HOSTS_VALUE"]

    DATABASE_NAME_VALUE = os.environ["DATABASE_NAME_VALUE"]

    DATABASE_USER_FILE = os.environ["DATABASE_USER_FILE"]
    DATABASE_PASSWORD_FILE = os.environ["DATABASE_PASSWORD_FILE"]

    with open(DATABASE_USER_FILE, "r") as f:
        DATABASE_USER_VALUE = f.read()[:-1]
    with open(DATABASE_PASSWORD_FILE, "r") as f:
        DATABASE_PASSWORD_VALUE = f.read()[:-1]

    DATABASE_HOSTNAME_VALUE = os.environ["DATABASE_HOSTNAME_VALUE"]
    DATABASE_PORT_VALUE = os.environ["DATABASE_PORT_VALUE"]
except:
    # settings used for development
    SECRET_KEY_VALUE = "z+4d!1k@ebw+a8hh-jc)ahaee5*grj2j$np34f_+6!v^n_rh=k"
    # Check to ensure it is not production environment
    DEBUG_VALUE = "true"
    ALLOWED_HOSTS_VALUE = "*"

    DATABASE_NAME_VALUE = "django_sample"
    DATABASE_USER_VALUE = "postgres-admin"
    DATABASE_PASSWORD_VALUE = "password123"
    DATABASE_HOSTNAME_VALUE = "0.0.0.0"
    DATABASE_PORT_VALUE = "5433"

    try:
        env = "development"
        env = os.environ["APP_ENVIRONMENT"].lower()
        raise
    except:
        if env != "development":
            raise
