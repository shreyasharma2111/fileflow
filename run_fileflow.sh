!/usr/bin/env bash

#make sure input folder exists
mkdir -p input processed quarantine archive logs summary

#run docker container with all files
MSYS_NO_PATHCONV=1 docker run --rm \
    -v "$(pwd)/input:/app/input" \
    -v "$(pwd)/processed:/app/processed" \
    -v "$(pwd)/quarantine:/app/quarantine" \
    -v "$(pwd)/archive:/app/archive" \
    -v "$(pwd)/logs:/app/logs" \
    -v "$(pwd)/summary:/app/summary" \
    fileflow

    echo "FileFlow processing finished!"
