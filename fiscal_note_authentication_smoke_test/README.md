## Fiscal Note - Authentication Smoke Automation Test

##### Description

This automation project demonstrates selenium automated test cases for the Fiscal Note authentication feature, the following login scenarios are automated using python:

* A user with valid login credentials is able to log into and out of their account.
* A user with invalid login credentials will see an error when attempting to log in.
* A user who leaves the password field blank will see an error message.
* A user who leaves the username field blank will see an error message.
* A user who leaves both fields blank will see an error message.

#### Technologies Used

The automation project uses the following python packages:

    - Python 3.7
    - Pytest
    - Selenium version 3.141.0

##### Project tree

├── README.md
├── __init__.py
├── pageObject
│    ├── __init__.py
│    ├── base_page.py
│    ├── home_page.py
|    └── log_in_page.py
├── requirements.txt
└── tests
    ├── __init__.py
    └── authentication_smoke_test.py


#### How to execute automation project

###### Execution steps

In order to execute the project, you need to have python 3.7 installed in your machine, then follow these required steps:

1. Create a virtual enviroment to install and isolate the test environment as follows:

        virtualenv --python=/usr/local/bin/python3.7 venv

2. Set enviroment variables in .bash_profile file, the values for these are provided for FIscal Note QA team.

        export FISCALNOTEUSERNAME="USERNAME"
        export FISCALNOTEPASSWORD="PASSWORD"

3. Source the .bash_profile in home directory

        source .bash_profile

4. Then install required packages using **"requirements.txt"** file which is located in the root path of the project, so run the following command:

        pip3 install -r requirements.txt

5. To execute the automated test cases, type the following command in terminal:

        pytest -v tests/authentication_smoke_test.py

6. At the end of the execution, the expected output should be something similar to this:

========== test session starts ==========
platform darwin -- Python 3.7.6, pytest-6.1.2, py-1.9.0, pluggy-0.13.1 -- /Users/omar.guzman/PycharmProjects/Fiscal_Note_Engineer_Deliverable-master/fiscal_note_authentication_smoke_test/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/omar.guzman/PycharmProjects/Fiscal_Note_Engineer_Deliverable-master/fiscal_note_authentication_smoke_test
collected 5 items
tests/authentication_smoke_test.py::test_log_in_with_valid_credentials PASSED                                                                                           [ 20%]
tests/authentication_smoke_test.py::test_error_message_with_invalid_credentials PASSED                                                                                  [ 40%]
tests/authentication_smoke_test.py::test_password_field_blank_error_message PASSED                                                                                      [ 60%]
tests/authentication_smoke_test.py::test_username_field_blank_error_message PASSED                                                                                      [ 80%]
tests/authentication_smoke_test.py::test_username_and_password_field_blank_error_message PASSED                                                                         [100%]

======= 5 passed in 70.48s (0:01:10) =======



