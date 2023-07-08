#Two versions of django-docker builds

**app_no_migrations**

- This build has the basis of debian docker (python 3.10 slim) with *celery*, *redis*, *certbot*, *nginx*, *postgresql*

- Added *watchdog* service

- Launching this app happens with the support of sh script *pre-docker.sh*, where migrations are creating inside of python container

- Some examples of django apps are provided


**app_with_migrations**

- This build has the basis of alpine docker (python 3.10 alpine) with *certbot*, *nginx*, *postgresql*

- Launching is simple and provided with no any additionals

- Some examples of django apps are provided
