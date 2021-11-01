[![Ansible Molecule](https://github.com/wi19b008/UbuntuSetupRole/actions/workflows/main.yml/badge.svg?branch=main&event=push)](https://github.com/wi19b008/UbuntuSetupRole/actions/workflows/main.yml)

Role
------------

- Description: Setup for a Ubuntu Server
- Name: ubuntu_setup
- Namespace: my_namespace

Description
-----------

Role installs following packages:
- nvm (node version manager)
- sdkman
- tfenv
- pyenv

and creates:
- User: github
- Group: github
- Directory: /home/github/actions-runner

Requirements
------------

- grzegorznowak.nvm_node
- comcast.sdkman
- giner.tfenv
- gantsign.pyenv

Author Information
------------------

- wi19b008
- wi19b054
- wi19b067
- wi19b088
