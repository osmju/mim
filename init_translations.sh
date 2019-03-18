#!/bin/sh

pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .
pybabel init -i messages.pot -d translations -l fr
pybabel init -i messages.pot -d translations -l nl

