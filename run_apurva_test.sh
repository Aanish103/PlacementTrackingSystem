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
"$PYTHON" -m unittest discover aat25/test/Blackbox -p "*.py" -v

echo ""
echo "▶ White Box Tests"

"$PYTHON" -m unittest discover "aat25/test/Whitebox/branch_testing" -p "*.py" -v
"$PYTHON" -m unittest discover "aat25/test/Whitebox/concolic_testing" -p "*.py" -v
"$PYTHON" -m unittest discover "aat25/test/Whitebox/condition_testing" -p "*.py" -v
"$PYTHON" -m unittest discover "aat25/test/Whitebox/loop_testing" -p "*.py" -v
"$PYTHON" -m unittest discover "aat25/test/Whitebox/mutation_testing" -p "*.py" -v
"$PYTHON" -m unittest discover "aat25/test/Whitebox/statement_coverage" -p "*.py" -v
"$PYTHON" -m unittest discover "aat25/test/Whitebox/symbolic_execution" -p "*.py" -v

echo ""
echo "======================================"
echo " All Tests Completed Successfully"
echo "======================================"
