FROM postgres:15

RUN apt-get update && \
      apt-get -y install sudo
RUN apt-get install postgresql

COPY /backup /backup/
COPY restore_db.sh /db_scripts/restore_db.sh
RUN chmod 744 db_scripts/restore_db.sh
