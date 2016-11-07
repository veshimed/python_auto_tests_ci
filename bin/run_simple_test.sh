#!/usr/bin/env bash

dateAndTime=$(date +"%Y%m%d-%H%M%S")
xml_filename="../test_results/TEST-${dateAndTime}.xml"

pytest -s -vv --junitxml=${xml_filename} ../tests/simple_test.py