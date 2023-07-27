#!/bin/bash
set -x
my_path=$HOME/test_fun_with_ast/devops
echo "CD INTO $my_path"
cd $my_path || exit 255
echo "Current directory is $PWD"
echo "REMOVE OLD VENV"
rm -r test_fun_with_ast
echo "CREATE VENV"
python3 -m venv test_fun_with_ast
echo "Activate virtual env"
source test_fun_with_ast/bin/activate
python -m pip install --index-url https://test.pypi.org/simple/ fun-with-ast
