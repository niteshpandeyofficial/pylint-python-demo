**Overview**
This repository contains a Python script that defines a class MyPerson to handle personal details such as name, age, and address. The class also provides methods for retrieving and setting the person's name. Additionally, code quality and security checks are integrated using Pylint and Bandit to ensure clean and secure code practices.

**Requirements**
The following Python libraries are required for this project:
- pi==0.1.2: A specific version of the pi library.
- pylint: A tool for checking code quality and ensuring adherence to Python coding standards.
- bandit: A tool for checking the security of the code.

You can install these dependencies by running:
```bash
pip install -r requirements.txt
```

**Code Quality and Security Check**
The project includes code quality and security checks using Pylint and Bandit:

- *1. Pylint:* Run the following command to check the code quality and ensure it adheres to Python coding standards:
```bash
    pylint current_file.py


        ************* Module current_file
    current_file.py:5:22: C0303: Trailing whitespace (trailing-whitespace)
    current_file.py:1:0: C0114: Missing module docstring (missing-module-docstring)
    current_file.py:1:0: C0115: Missing class docstring (missing-class-docstring)
    current_file.py:7:4: C0116: Missing function or method docstring (missing-function-docstring)
    current_file.py:7:4: C0103: Method name "getName" doesn't conform to snake_case naming style (invalid-name)
    current_file.py:11:4: C0116: Missing function or method docstring (missing-function-docstring)

    ------------------------------------------------------------------
    Your code has been rated at 5.00/10 (previous run: 5.00/10, +0.00)
```

```bash
   pylint .\modified_file.py
    --------------------------------------------------------------------
    Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```


-  *2.Bandit:* Run the following command to check for any security issues in the code:
```bash
    bandit -r modified_file.py

    Run started:2025-03-23 15:26:06.042144
    Test results:
            No issues identified.

    Code scanned:
            Total lines of code: 28
            Total lines skipped (#nosec): 0

    Run metrics:
            Total issues (by severity):
                    Undefined: 0
                    Low: 0
                    Medium: 0
                    High: 0
            Total issues (by confidence):
                    Undefined: 0
                    Low: 0
                    Medium: 0
                    High: 0
    Files skipped (0):
```

**Conclusion**
This project demonstrates how to define a simple Python class, use pylint for quality checks, and bandit for security checks. It’s a good starting point for integrating these tools into your development workflow for maintaining clean and secure code.
