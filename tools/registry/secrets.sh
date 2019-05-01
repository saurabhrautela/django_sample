#!/bin/sh

set -e

if [
mkdi -p certs

openssl req \
-newkey rsa:4096 -nodes -sha256 -keyout certs/domain.key \
-x509 -days 365 -out certs/domain.crt


