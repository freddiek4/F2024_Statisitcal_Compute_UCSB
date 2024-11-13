# An in-depth analysis of my understanding of mathematical conceptualities, starting from the basic fundamentals, and going in-depth of the theories of Bernoulli, Poisson, and many more using computation to prove their theorems, and applying these to more complex and applicable solutions.

A brief description of what this project does and who it's for.

## Table of Contentsx
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview
In the code, I will alternate between code and mathematics, walking through my understanding of each concept, utilizing a code whenever I need to run a computation. 

## Installation
Instructions on how to install and set up the project locally:
1. Clone the repository:
   ```bash
   git clone git@github.com:yourusername/your-repo-name.git


## Neural Tangent Kernels
Paper Inspiration: https://arxiv.org/pdf/1912.02803


# Database Formulations Set-Up
1.	Python 3.x: Ensure you have Python 3 installed. You can check your Python version by running:
python3 --version

2.	Required Packages: The script requires the pymysql and pandas packages. To install these packages, use:
pip install pymysql pandas sqlalchemy

Database Setup

1.	MySQL Database: You need a MySQL database set up on your local machine or a remote server. Follow these steps:
- Ensure MySQL is installed and running.
- Create a database named DemoDB (or update the script with the name of your own database).

2.	User Credentials: Update the load_data.py script with your MySQL credentials:
user = 'your_username'
password = 'your_password'  # Leave as an empty string if no password is required
host = 'localhost'  # Or the IP address if connecting to a remote server
database = 'DemoDB'

3. Running the Script
To run the script that loads data into the MySQL database, use:
python3 load_data.py
The script will load the Titanic dataset into a table named TitanicData in the specified MySQL database.