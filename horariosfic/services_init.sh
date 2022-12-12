#!/bin/bash
echo "================================"
echo "Inicializando todos los servicios"
echo "================================"
python3 Newsletter.py &
python3 Feedback.py &
python3 Courses.py &
python3 Evaluations.py &
python3 Mailing.py &
python3 UserTracker.py