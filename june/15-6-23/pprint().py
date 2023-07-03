import json
import pprint
from urllib.request import urlopen
with urlopen('https://pypi.org/pypi/sampleproject/json') as resp:
    project_info = json.load(resp)['info']

pprint.pprint(project_info)