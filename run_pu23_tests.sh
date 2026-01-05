#!/bin/bash

echo "======================================"
echo " All Tests for Putusoththama"
echo "======================================"


cd "$(dirname "$0")"

PYTHON="/c/Users/Prushoth/AppData/Local/Programs/Python/Python38/python.exe"

if [ ! -f "$PYTHON" ]; then
    echo "ERROR: Python not found at $PYTHON"
    exit 1
fi

echo "Using Python: $PYTHON"
echo ""

echo "▶ Black Box Tests"
"$PYTHON" -m unittest discover "pu23/test/Black box/Boundary_value" -p "*.py" -v
"$PYTHON" -m unittest discover "pu23/test/Black box/equivalence_partitioning" -p "*.py" -v
"$PYTHON" -m unittest discover "pu23/test/Black box/Random Testing" -p "*.py" -v

echo ""
echo "▶ White Box Tests"

"$PYTHON" -m unittest discover "pu23/test/White box/Branch Testing" -p "*.py" -v
"$PYTHON" -m unittest discover "pu23/test/White box/Concolic Testing" -p "*.py" -v
"$PYTHON" -m unittest discover "pu23/test/White box/Condition Testing" -p "*.py" -v
"$PYTHON" -m unittest discover "pu23/test/White box/Loop Testing" -p "*.py" -v
"$PYTHON" -m unittest discover "pu23/test/White box/Mutation Testing" -p "*.py" -v
python3 -m unittest discover "pu23/test/White box/Statement Coverage" -p "*.py" -v
"$PYTHON" -m unittest discover "pu23/test/White box/Symbolic Testing" -p "*.py" -v

echo ""
echo "======================================"
echo " All Tests Completed Successfully"
echo "======================================"