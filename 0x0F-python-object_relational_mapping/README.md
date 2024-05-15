# ALX Project: ORM, SQL, Python, OOP, MySQL and SQLAlchemy

## Overview

This project is part of the ALX curriculum, focusing on Object-Relational Mapping (ORM) with SQL and SQLAlchemy. The goal is to connect Python scripts to a database using SQLAlchemy and perform various database operations. The project runs within a Python virtual environment (venv) to ensure dependencies are managed properly.

## Table of Contents

- [Project Overview](#overview)
- [Setup Instructions](#setup-instructions)
  - [Virtual Environment](#virtual-environment)
  - [Dependencies](#dependencies)
- [Usage](#usage)
  - [Running the Scripts](#running-the-scripts)
- [Project Structure](#project-structure)
- [Author](#author)
- [License](#license)

## Setup Instructions

### Virtual Environment

To ensure a clean and isolated environment for your project, it's recommended to use a Python virtual environment.

1. **Create a Virtual Environment**:

    ```sh
    python3 -m venv venv
    ```

2. **Activate the Virtual Environment**:

    - On Linux or macOS:

        ```sh
        source venv/bin/activate
        ```

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

### Dependencies

After activating the virtual environment, install the required dependencies using the `install requirements on the proect page`.

1. **Install Dependencies**:

    ```sh
    pip install -r requirements
    ```

    Ensure your `requirements` file includes:

    ```text
    SQLAlchemy==2.0
    mysqlclient==2.1.0
    ```

## Usage

### Running the Scripts

To run the Python scripts connecting to the database via SQLAlchemy:

1. **Ensure the Virtual Environment is Activated**:

    ```sh
    source venv/bin/activate
    ```

2. **Run the Desired Script**:

    ```sh
    python script_name.py
    ```

Project Structure
The directory structure of the project is as follows:

## 0x0F-python-object_relational_mapping/
│
├── venv/                # Virtual environment directory
├── list_states.py       # Script to list states from the database
├── other_script.py      # Other project scripts
└── README.md            # This README file

## Author

This project is created by Mojibola Olalekan, a student of the ALX program.

## License

This project is licensed under the MIT License. 