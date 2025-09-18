#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
<<<<<<< HEAD
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
=======
            "Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable?"
>>>>>>> ce7335629f97d40a13c334895130406c72ec0ccf
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> ce7335629f97d40a13c334895130406c72ec0ccf
