#!/bin/bash

if [ ! -z "${1}" ]; then
    exec "${@}"
fi

echo "Running checkconf..."

/usr/sbin/named-checkconf /opt/named/named.conf

if [ ${?} -ne 0 ]; then
    echo "Failed to verify configuration"
    exit 1
fi

echo "Checkconf completed successfully"
echo "Running BIND DNS server..."

exec "/usr/sbin/named" -f -u named -c /opt/named/named.conf
