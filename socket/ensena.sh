#!/bin/bash
echo "=========================="
echo "Starting ssh tunnel to bus"
echo "=========================="
sshpass -p 'vicho123' ssh -p 34567 -tt -L *:5000:localhost:5000 -o StrictHostKeyChecking=no vicente.berroeta@200.14.84.235 'echo "Logged as:" `whoami`; /bin/bash'