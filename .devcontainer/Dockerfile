# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.163.1/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3.9"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Option] Install Node.js
ARG INSTALL_NODE="false"
ARG NODE_VERSION="lts/*"

# Geosupport release versions, change args in devcontainer.json to build against a new version
ARG RELEASE=21a
ARG MAJOR=21
ARG MINOR=1
ARG PATCH=0

RUN if [ "${INSTALL_NODE}" = "true" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

WORKDIR /geosupport
COPY . .

RUN FILE_NAME=linux_geo${RELEASE}_${MAJOR}_${MINOR}.zip \
    && echo $FILE_NAME \
    && curl -O https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/$FILE_NAME \
    && unzip *.zip \
    && rm *.zip

# Trailing slash ('/') is required
ENV GEOFILES=/geosupport/version-${RELEASE}_${MAJOR}.${MINOR}/fls/
ENV LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/geosupport/version-${RELEASE}_${MAJOR}.${MINOR}/lib/

#
# To update all out-of-date packages:
#
#   RUN pip3 list --outdated --format=freeze | \
#               grep -v '^\-e' | \
#               cut -d = -f 1  | \
#               xargs -n1 pip3 install -U
#
# To update pip and setuptools if they are outdated:
#   RUN pip3 list --outdated --format=freeze | \
#               grep -e 'pip==' -e 'setuptools==' | \
#               cut -d = -f 1  | \
#               xargs -n1 pip3 install -U
#


# Install pyenv, pyenv-cov
# Install tox, tox-pyenv
WORKDIR /
