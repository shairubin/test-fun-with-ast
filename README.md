# test-fun-with-ast
The repository contains examples of using the [fun-with-ast](https://github.com/shairubin/fun_with_ast) library.
### Install and Run Test Programs(tested on Ubuntu 20.04)
We assume you use python > 3.6 
1. Create an empty directory: e.g., ```mkdir ~/example_fun_with_ast```
1. Change directory into the new directory: ```cd ~/example_fun_with_ast```
1. Create and activate a virtual environment:
   1. Create a virtual environment: ```python3 -m venv environment```
   1. Activate the virtual environment: ```source environment/bin/activate```
1. Download the test-fun-with-ast project: ```git clone https://github.com/shairubin/test-fun-with-ast```
1. Install the fun-with-ast library: 
   2. ```pip uninstall  fun-with-ast```
   3. ```pip install --index-url https://test.pypi.org/simple/  fun-with-ast```
1. Run the example rewrite programs:
    1. ```cd test-fun-with-ast/source_manipulation_examples/```
    1. ```PYTHONPATH=../ python rewrite_if_examples.py``` 
    1. ```PYTHONPATH=../ python swap_if_else_examples.py``` 
1. Run the example source match programs 
   1. ```cd ../preserve_source_examples```
   1. ```PYTHONPATH=../ python source_code_preserve_tests.py``` 
1. Deactivate the virtual environment: `deactivate`
2. Optional: delete the directory: ```rm -rf ~/example_fun_with_ast```

## Contributors are Welcomed 
1. See open issues - or open a new one.
2. Have fun.