#!/bin/bash
set -e

psql -U $POSTGRES_USER <<-EOSQL
    CREATE ROLE replication_user WITH REPLICATION PASSWORD 'replication_password' LOGIN;
EOSQL
echo "host replication replication_user all md5" >> "$PGDATA/pg_hba.conf"
echo "wal_level = replica" >> "$PGDATA/postgresql.conf"
echo "max_wal_senders = 3" >> "$PGDATA/postgresql.conf"
echo "wal_keep_size = 64" >> "$PGDATA/postgresql.conf"
