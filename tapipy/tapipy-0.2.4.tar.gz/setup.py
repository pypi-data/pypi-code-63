# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tapipy']

package_data = \
{'': ['*'], 'tapipy': ['resources/*', 'specs/*']}

install_requires = \
['PyJWT==1.7.1',
 'atomicwrites>=1.4.0,<2.0.0',
 'certifi>=14.05.14,<15.0.0',
 'cryptography>=2.9.2,<3.0.0',
 'openapi_core>=0.13.0,<0.14.0',
 'python_dateutil>=2.5.3,<3.0.0',
 'requests',
 'setuptools>=21.0.0,<22.0.0',
 'six>=1.10,<2.0',
 'urllib3>=1.15.1,<2.0.0']

setup_kwargs = {
    'name': 'tapipy',
    'version': '0.2.4',
    'description': 'Python lib for interacting with an instance of the Tapis API Framework',
    'long_description': '# tapipy - Tapis V3 Python SDK\n\nPython library for interacting with an instance of the Tapis API Framework.\n\n## Development\n\nThis project is under active development, exploring different approaches to SDK generation.\n\n## Installation\n\n```\npip install tapipy\n```\n\n## Running the tests\n\nTests resources are contained within the `test` directory. `Dockerfile-tests` is at root.\n1. Build the test docker image: `docker build -t tapis/tapipy-tests -f Dockerfile-tests .`\n2. Run these tests using the built docker image: `docker run -it --rm  tapis/tapipy-tests`\n\n## Usage\n\nTODO - provide working examples, e.g., \n```\nimport tapipy\nt = tapipy.Tapis(base_url=\'http://localhost:5001\')\nreq = t.tokens.NewTokenRequest(token_type=\'service\', token_tenant_id=\'dev\', token_username=\'admin\')\nt.tokens.create_token(req)\n\nimport openapi_client\nconfiguration = openapi_client.Configuration()\nconfiguration.host = \'http://localhost:5001\'\napi_instance = openapi_client.TokensApi(openapi_client.ApiClient(configuration))\n\nnew_token = openapi_client.NewTokenRequest(token_type=\'service\', token_tenant_id=\'dev\', token_username=\'admin\')\n\nresp = api_instance.create_token(new_token)\njwt = resp.get(\'result\').get(\'access_token\').get(\'access_token\')\n```\n\n## Important Parameters to Know\n\nThe Tapipy package allows for spec file customization in Tapis object initialization:\n* resource_set: str \n\t* Determines which set of resource to use, master or dev, defaults to master.\n\t* Important to note that if a custom_spec_dictionary is used, it is appended to this resource_set.\n\t\t* For example, you would set master and then specify a custom specs that will be added on.\n* custom_spec_dict: {resource_name: str, resource_url: str}\n\t* Allows users to modify the base resource set urls.\n\t\t* e.g. I can specify actor as a resource name and change the url.\n\t* Also allows users to add new resources to the set.\n\t\t* e.g. I can add a new resource named "test" with a  custom url.\n\t\t* Important that know that any new specs will be downloaded and added to the cache\n\t\t\t* No need to specify download_latest_specs or update spec files.\n* download_latest_specs: bool\n\t* Allows users to re-download all specs regardless on if they already exist in the cache. Defaulted to False\n\t* This will happen every time the Tapis object is initialized, it\'s a tad slower, and can cause live updates to specs.\n\t\t* As such, be warned. There are functions to update spec files below.\n* spec_dir: str\n\t* Allows users to specify folder to save specs to. Defaults to none which uses Tapipy\'s package folder.\n\t* If you are updating specs it\'s wise to use a different folder in order to not modify the base specs.\n\nThe following is an example of some custom parameter setting. As you can see, the abaco resource will now use the spec at `URL#1`, overwriting the resource definition in the master resource set, it\'ll download it if it doesn\'t exist. The same for the longhorn resource. This means that the Tapis object will now have access to all specs in master like normal, but with a modified abaco and with a new longhorn resource. All of these are stored at the new spec_dir because I don\'t want to accidentally overwrite any base specs if I call `update_spec_cache()` later (talked about in the next section).\n```\nfrom tapipy.tapis import Tapis\n\nt = Tapis(base_url=\'https://master.develop.tapis.io\',\n          tenant_id=\'master\',\n          username=\'username\',\n          account_type=\'user\',\n          password=\'password\',\n          resource_set=\'master\',\n          custom_spec_dict={\'abaco\': \'URL#1\',\n                            \'longhorn\': \'URL#2\'},\n          spec_dir=\'/home/username/tapipy_specs\')\nt.get_tokens()\n```\n\n## Update Specs Files\n\nThe Tapipy package now uses a cache to organize spec dictionaries as pickled files and has the ability to accept custom spec files. By default Tapipy keeps a set of base spec files in the `%tapipy%/specs` folder. These specs are pre-pickled at package creation time.\n\nIn order to update all default spec files a user can use the `update_spec_cache()` function. Said function\'s definition is below. If no resources are provided the function will download all default spec urls in the RESOURCES object in `%tapipy%/tapipy/tapis.py` file.\n```\nResources = Dict[ResourceName, ResourceUrl]\nupdate_spec_cache(resources: Resources = None, spec_dir: str = None)\n```\nUsers are able to specify custom resources to download by providing their own resource dictionary. For example, providing `{\'actors\': \'URLToMyActorDictionary\'}` would update that spec.\n\nUsers can also specify here where to update the spec with the `spec_dir` variable.\n\nThe Tapis object itself also has a `update_spec_cache()` function that takes the Tapis parameters given at startup and updates the spec cache. Meaning that if the Tapis object was given a custom dictionary, the `update_spec_cache()` function would update it without the need for setting parameters.\n```\nt.update_spec_cache()\n```\n\n## Build instructions\n\nBuilding is done with poetry as follows:\n```\npip install poetry\npoetry install\n```\nThis installs `tapipy` to a virtual environment. Run a shell in this environment with:\n```\npoetry shell\n```\n\nTo install locally (not in a virtual environment):\n```\npip install poetry\npoetry build\ncd dists\npip install *.whl\n```\n\n## PyPi Push Instructions\n\n```\npoetry build\npoetry publish\n```',
    'author': 'Joe Stubbs',
    'author_email': 'jstubbs@tacc.utexas.edu',
    'maintainer': 'Joe Stubbs',
    'maintainer_email': 'jstubbs@tacc.utexas.edu',
    'url': 'https://github.com/tapis-project/tapipy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
