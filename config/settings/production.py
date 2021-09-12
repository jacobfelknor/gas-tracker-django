from .local import *  # noqa

# from .keys import ip_a

DEBUG = False

ALLOWED_HOSTS = ["gastrackerapi.com", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "gastrackerdb",
        "USER": get_parameters_aws("gastrackerdb_user"),
        "PASSWORD": get_parameters_aws("gastrackerdb_password"),
        "HOST": get_parameters_aws("gastrackerdb_endpoint"),
        "PORT": "3306",
    }
}
