#!/bin/sh

echo "Run celery";
celery -A coffee_shop worker -l info
