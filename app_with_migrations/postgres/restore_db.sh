#!/bin/bash

backup_filename="../backup/db.sql" # todo normal path and workdir
#if [[ ! -f "${backup_filename}" ]]; then
#    echo "No backup with the specified filename found in ${working_dir}. Check out the 'backups' maintenance script output to see if there is one and try again."
#    exit 1
#fi

echo "Restoring the '${POSTGRES_DB}' database from the '${backup_filename}' backup..."

if [[ "${POSTGRES_USER}" == "postgres" ]]; then
    echo "Restoring as 'postgres' user is not supported. Assign 'POSTGRES_USER' env with another one and try again."
    exit 1
fi

export PGHOST="${POSTGRES_HOST}"
export PGPORT="${POSTGRES_PORT}"
export PGUSER="${POSTGRES_USER}"
export PGPASSWORD="${POSTGRES_PASSWORD}"
export PGDATABASE="${POSTGRES_DB}"

echo "Dropping the database..."
dropdb "${PGDATABASE}"

echo "Creating a new database..."
createdb --owner="${POSTGRES_USER}"

echo "Applying the backup to the new database..."
psql -U ${POSTGRES_USER} -f ${backup_filename}

echo "The '${POSTGRES_DB}' database has been restored from the '${backup_filename}' backup."
