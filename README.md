# Setup and execution instructions

*********Important: The script requires python3 for successful execution*********

## Setup

1. installing python3 for Ubuntu:
http://docs.python-guide.org/en/latest/starting/install3/linux/

2. installing python3 for MAC: 
http://docs.python-guide.org/en/latest/starting/install3/osx/

## Execution

1. the company_list text file should be populated with the company list that should be fed into the tool

2. The script can be executed from the command line like so:

`python3 clearbit.py "outputfilename"`

eg: `python3 clearbit.py "company_domain_mapping"`

3. The outputfilename arguement is optional. If it is not specified, the default output filename will be company_domain_mapping.csv

4. The company,domain tuple will be saved to a csv file upon execution.

