#!/bin/bash
set -e

# Ожидание, пока основной сервер будет готов
until pg_isready -h $PRIMARY_HOST -U db_user; do
  sleep 1
done

# Сброс текущих данных и настройка реплики
PGDATA="/var/lib/postgresql/data"
rm -rf ${PGDATA}/*
pg_basebackup -h $PRIMARY_HOST -D ${PGDATA} -U replication_user -Fp -Xs -P -R
