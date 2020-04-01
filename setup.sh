#!/bin/sh

echo "user is ${USER}"
echo "username is ${USERNAME}"

ans=0

python=$(python3.6 -V > /dev/null 2>&1)
response=$?
if [ $response -eq $ans ]
then
    echo "python3.6 recognized"
else
    echo "python3.6  not recognized"
    echo "install python3.6"
fi

pip=$(pip3 -V > /dev/null 2>&1)
response=$?
if [ $response -eq $ans ]
then
    echo "pip3 recognized"
    pip3 install mysql-connector
else
    echo "pip3 not recognized"
fi