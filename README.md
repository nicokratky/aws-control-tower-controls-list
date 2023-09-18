# AWS Control Tower Controls List

In order to enable controls programatically (using for example Terraform), it is neccessary to know the unique ID of each control. This ID is unique in every AWS Region. The only method of retrieving these IDs I found was looking them up in the [AWS Control Tower User Guide](https://docs.aws.amazon.com/controltower/latest/userguide/control-metadata-tables.html).

This project parses the metadata table and outputs the IDs as a JSON object to allow for further processing.

## Installation

Use [pip](https://pip.pypa.io/en/stable/) to install required dependencies. It is recommended to use a virtual environment to not pollute the global installation.

```bash
python -m venv .venv                # create a new virtual environment in .venv
source ./venv/bin/activate          # activate the virtual environment
pip install -r requirements.txt
```

## Usage

```bash
> python parser.py
Usage:
        python3 parser.py <REGION>
        e.g.: python3 parser.py eu-central-1

> python parser.py eu-central-1

[...]
"SH.ElasticBeanstalk.1": {
    "arn": "arn:aws:controltower:eu-central-1::control/XXHCDRWNECMP",
    "id": "XXHCDRWNECMP"
},
"SH.ElasticBeanstalk.2": {
    "arn": "arn:aws:controltower:eu-central-1::control/WIZMLNWMCLPL",
    "id": "WIZMLNWMCLPL"
},
"SH.GuardDuty.1": {
    "arn": "arn:aws:controltower:eu-central-1::control/HNRJJLKEIRQJ",
    "id": "HNRJJLKEIRQJ"
},
"SH.IAM.1": {
    "arn": "arn:aws:controltower:eu-central-1::control/RWLDODTORAPO",
    "id": "RWLDODTORAPO"
},
[...]

# store output in a JSON file
> python parser.py eu-central-1 > output/eu-central-1.json
```
