# gas-tracker-django
Backend for my gas tracker angular app, written with Django Rest Framework

## Setup
1. Clone the repository
2. Install OS dependencies with `sudo apt-get install python3-dev default-libmysqlclient-dev build-essential` 
3. create a virtual environment with Python 3.7
4. install requirements with `pip install -r requirements.txt`
5. Create a `systemd` service file at `/etc/systemd/system/gas-tracker-django.service`

```ini
[Unit]
Description=Backend for my gastracker application

[Service]
ExecStart=/path/to/gas-tracker-django/runserver.sh
WorkingDirectory=/path/to/gas-tracker-django

[Install]
WantedBy=multi-user.target
```

6. Start and enable the service
  - `systemctl start gas-tracker-django`
  - `systemctl enable gas-tracker-django`
