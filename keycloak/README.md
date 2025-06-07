# Keycloak Server

This directory contains the Docker Compose setup to run Keycloak with MySQL.

- Docs: [Keycloak](https://www.keycloak.org/documentation)

## Prerequisites

1. Docker and Docker Compose installed.
2. Copy example env and rename:

   ```bash
   cp example-env .env
   ```
3. Open `.env` and set:
   - DB_ADDR
   - DB_PORT
   - DB_DATABASE
   - DB_USER
   - DB_PASSWORD
   - KC_ADMIN
   - KC_ADMIN_PASSWORD

## Start Keycloak

```bash
docker-compose up -d
```

- The Keycloak admin console will be available at `https://<KC_HOSTNAME>/auth`.
- Use `KC_ADMIN`/`KC_ADMIN_PASSWORD` to log in.

---

> [!TIP] 
>Make sure you set the domain for the keycloak instance in the Proxys Web UI. Otherwise you wont be able to see the Keycloak Web UI. 
> 