#!/bin/bash
echo "================================"
echo "Inicializando todos los servicios"
echo "================================"
python3 Newsletter.py &
python3 Feedback.py