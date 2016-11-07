#!/usr/bin/env bash

dateAndTime=$(date +"%Y%m%d-%H%M%S")
xml_filename="../test_results/TEST-${dateAndTime}.xml"
test_results="../test_results/RES-${dateAndTime}.txt"


pytest --log-format="%(asctime)s %(levelname)s %(message)s" --log-date-format="%Y-%m-%d %H:%M:%S" ../tests/simple_test.py