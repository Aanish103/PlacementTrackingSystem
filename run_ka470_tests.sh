#!/bin/bash

echo " All Tests for Keerthi"

cd "$(dirname "$0")"

echo ""
echo "Black Box Tests"
python -m unittest discover ka470/test/blackbox -v

echo ""
echo "White Box Tests"
python -m unittest discover ka470/test/whitebox -v

echo ""
echo "All Tests Completed"