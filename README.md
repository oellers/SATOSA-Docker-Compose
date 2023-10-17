# Notes
- Can be used to proxy the communication between OIDC (IDP/OP) -> SAML (SP/RP) by deploying an OIDC RP (backend) and SAML2 IDP (frontend) with satosa using docker compose and official images
- This repository just serves as a starting point for deploying a satosa to proxy communication between the OIDC protocol and Shibboleth/SAML2 Service Providers (e.g., within the DFN-AAI) and is not meant to be used in production without further adaption/review

## Docker Compose 
- If there are python path updates in the docker image, the mount in docker-compose has to be renewed, e.g.
``/usr/local/lib/python3.11/site-packages/satosa/micro_services/processors/prefix_processor.py``

## Metadata
- To regenerate metadata (saml2 frontend idp), 
use:
``satosa-saml-metadata <path to proxy_conf.yaml> <path to key for signing> <path to cert for signing>``
or delete ``etc/backend.*`` as well as ``etc/frontend.xml`` and restart container

- backend keys/certs are not in use, as we just use oidc backend and no saml backend

## Configuration
- Copy .env.example to .env and set variables
- Configure Satosa as desired
- Files with entity IDs configured, e.g., for metadata or special handling:
``./etc/plugins/frontends/saml2_frontend.yaml``, ``./etc/plugins/microservices/hasher-nameid.yaml``
- Look through further files, as paths, certs, entityids and salts needs to be configured. 
