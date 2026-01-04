#!/bin/bash

echo " All Tests for Aanish"

cd "$(dirname "$0")"

echo ""
echo "Black Box Tests"
python3 -m unittest discover ama103/test/blackbox -v

echo ""
echo "White Box Tests"

python3 -m unittest discover "ama103/test/whitebox/Branch Testing" -v
python3 -m unittest discover "ama103/test/whitebox/Concolic Testing" -v
python3 -m unittest discover "ama103/test/whitebox/Condition Testing" -v
python3 -m unittest discover "ama103/test/whitebox/Loop Testing" -v
python3 -m unittest discover "ama103/test/whitebox/Mutation Testing" -v
python3 -m unittest discover "ama103/test/whitebox/Statement Coverage" -v
python3 -m unittest discover "ama103/test/whitebox/Symbolic Execution" -v

echo ""
echo "All Tests Completed"
