#!/bin/bash

### install python3.10 over and ubuntu 20 over

sudo apt update && sudo apt upgrade

pip install django
pip install djangorestframework
pip install markdown  		# Markdown support for browsable API
pip install django-filter 	# Filtering support

pip install googletrans		# Install translator
pip install request beautifulsoup4

## check python version
python3 -c "import django; print(django.get_version())"


 
