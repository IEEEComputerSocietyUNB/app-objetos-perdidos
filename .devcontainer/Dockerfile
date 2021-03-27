# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.163.1/containers/ubuntu/.devcontainer/base.Dockerfile

# [Choice] Ubuntu version: bionic, focal
ARG VARIANT="focal"
FROM mcr.microsoft.com/vscode/devcontainers/base:0-${VARIANT}

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    python3 \
    python3-pip \
    mysql-server \
    && pip3 install Flask pytest coverage mysql-connector-python sqlalchemy \
    && /etc/init.d/mysql start \
    && echo "CREATE USER 'dev'@'localhost' IDENTIFIED BY 'password';" | mysql -u root -p='' \
    && echo "GRANT ALL PRIVILEGES ON *.* TO 'dev'@'localhost';" | mysql -u root -p='' \
    && echo "FLUSH PRIVILEGES;" | mysql -u root -p='' \
    && echo "CREATE DATABASE dbtest;" | mysql -u root -p=''


