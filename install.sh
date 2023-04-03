#!/bin/bash

# Instala as dependências do apt-get
sudo apt-get update
sudo apt-get install -y w3m

# Instala as dependências do pip
pip install -r requirements.txt
