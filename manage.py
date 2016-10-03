#!/usr/bin/env python
import os
import socket
import sys

if __name__ == "__main__":
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "certcurity.settings")
    shell_env_query = os.getenv("CERTCURITY_ENV")
    host_name_query = socket.gethostname().split('-')[0]

    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "certcurity.settings.test")
    elif shell_env_query:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "certcurity.settings." + shell_env_query.lower())
    elif host_name_query in ['prod', 'qa', 'dev', 'test']:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "certcurity.settings." + host_name_query.lower())
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "certcurity.settings.local")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
