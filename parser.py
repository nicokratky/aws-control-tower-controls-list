from bs4 import BeautifulSoup
import json
import re
import requests
import sys

CONTROL_METADATA_LINK = 'https://docs.aws.amazon.com/controltower/latest/userguide/control-metadata-tables.html'


def usage():
    print('Usage:')
    print('\tpython3 parser.py <REGION>')
    print('\te.g.: python3 parser.py eu-central-1')


def get_control_metadata():
    response = requests.get(CONTROL_METADATA_LINK)
    return response.text


def main(region):
    metadata = get_control_metadata()

    soup = BeautifulSoup(metadata, 'html.parser')
    main = soup.find_all(id='main-col-body')

    headings = soup.find_all(
        lambda tag: tag.name == 'h2' and tag.has_attr('id'))

    controls = dict()

    for control in headings:
        control_name = control.string.strip()

        try:
            control_arn = control.find_next_sibling().find_all('td')[3].find(
                string=re.compile(region)).parent.parent.find('code').string
            control_id = control_arn.split('/')[1]

            controls[control_name] = {
                'arn': control_arn,
                'id': control_id
            }
        except AttributeError:
            pass

    print(json.dumps(controls, sort_keys=True, indent=2))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        exit()

    main(sys.argv[1])
