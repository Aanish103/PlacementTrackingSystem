#!/bin/bash

echo "======================================"
echo " All Tests for Apurva"
echo "======================================"


cd "$(dirname "$0")"

PYTHON="../.venv/Scripts/python.exe"

if [ ! -f "$PYTHON" ]; then
    echo "ERROR: Python not found at $PYTHON"
    exit 1
fi

echo "Using Python: $PYTHON"
echo ""

echo "▶ Black Box Tests"
"$PYTHON" -m unittest discover "ka470/test/Black box/Boundary value analysis" -p "*.py" -v
"$PYTHON" -m unittest discover "ka470/test/Black box/Equivalence Partition" -p "*.py" -v
"$PYTHON" -m unittest discover "ka470/test/Black box/Random Testing" -p "*.py" -v

echo ""
echo "▶ White Box Tests"

"$PYTHON" -m unittest discover "ka470/test/White box/Branch Coverage" -p "*.py" -v
"$PYTHON" -m unittest discover "ka470/test/White box/Concolic Testing" -p "*.py" -v
"$PYTHON" -m unittest discover "ka470/test/White box/Condition Testing" -p "*.py" -v
"$PYTHON" -m unittest discover "ka470/test/White box/Loop Testing" -p "*.py" -v
"$PYTHON" -m unittest discover "ka470/test/White box/Mutation Testing" -p "*.py" -v
"$PYTHON" -m unittest discover "ka470/test/White box/Statement Coverage" -p "*.py" -v
"$PYTHON" -m unittest discover "ka470/test/White box/Symbolic Execution" -p "*.py" -v

echo ""
echo "======================================"
echo " All Tests Completed Successfully"
echo "======================================"