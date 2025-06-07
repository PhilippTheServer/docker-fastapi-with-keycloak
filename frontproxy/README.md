# Frontproxy (Reverse Proxy)

This directory contains the configuration to run your front-end proxy (e.g., Nginx or Traefik).

- Docs: [Nginx Proxy Manager](https://nginxproxymanager.com/guide/)

## Prerequisites

1. Docker and Docker Compose installed.
2. Copy example env and rename:

   ```bash
   cp example-env .env
   ```
3. Open `.env` and set your domain, certificates, and service URLs:
    - mysql-user-pw
    - mysql-admin-pw

## Start the Proxy

```bash
docker-compose up -d
```

- The proxy listens on ports 80/443 and forwards to FastAPI and Keycloak.
- To view logs: `docker-compose logs -f frontproxy`

---

# Configuration

Go to http://localhost:81 and use the default credentials:
`admin@example.com` and `changeme` as the password.

Create an Administrator account.

If you want to apply a domain to running docker container, add a new proxy host.
The Proxy host needs the domain that it shell listen to and the destination. In case of docker containers that would be the IPv4 address in the `frontproxy_fnet` network and the associated Port. 