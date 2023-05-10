#!/bin/bash

set -e

exec python3 ./scout.py &
exec python3 ./exposer.py &