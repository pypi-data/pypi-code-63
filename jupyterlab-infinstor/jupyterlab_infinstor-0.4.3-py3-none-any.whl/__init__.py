"""
Placeholder
"""
import base64
import json
import re
from collections import namedtuple
import logging
import traceback
from . import servicedefs
import builtins
import configparser
import os
from os.path import expanduser
from os.path import sep as separator
import datetime
from .cognito_utils import perform_infinstor_login, token_renewer

#  from dataclasses import dataclass

import boto3
import tornado.gen as gen
from tornado import ioloop
from botocore.exceptions import NoCredentialsError
from notebook.base.handlers import IPythonHandler, utcnow, APIHandler
from notebook.utils import url_path_join
from traitlets import Unicode
from traitlets.config import SingletonConfigurable

import logging
import sys
import requests
from requests.exceptions import HTTPError
from urllib.parse import urlunparse, urlparse, quote, unquote

from .proxy import MlflowProxyHandler

def setup_credentials():
    home = expanduser("~")
    print("User's Home Directory is " + home);
    config = configparser.ConfigParser()
    newconfig = configparser.ConfigParser()
    credsfile = home + separator + ".aws" + separator + "credentials"
    if (os.path.exists(credsfile)):
        credsfile_save = home + separator + ".aws" + separator + "credentials.save"
        try:
            os.remove(credsfile_save)
        except Exception as err:
            print()
        try:
            os.rename(credsfile, credsfile_save)
        except Exception as err:
            print()
        config.read(credsfile_save)
        for section in config.sections():
            if (section != 'infinstor'):
                newconfig[section] = {}
                dct = dict(config[section])
                for key in dct:
                    newconfig[section][key] = dct[key]
    else:
        dotaws = home + "/.aws"
        if (os.path.exists(dotaws) == False):
            os.mkdir(dotaws, 0o755)
            open(credsfile, 'a').close()

    newconfig['infinstor'] = {}
    newconfig['infinstor']['aws_access_key_id'] = builtins.infinStorAccessKeyId
    newconfig['infinstor']['aws_secret_access_key'] = builtins.infinStorSecretAccessKey

    with open(credsfile, 'w') as configfile:
        newconfig.write(configfile)

class InfinStorHandler(APIHandler):  # pylint: disable=abstract-method
    """
    handle api requests to change auth info
    """
    @gen.coroutine
    def get(self, path=""):
        """
        Checks if the user is already authenticated
        against an s3 instance.
        """
        if builtins.infinStorSecretAccessKey != None:
            self.finish(json.dumps({"authenticated": True}))
        else:
            self.finish(json.dumps({"authenticated": False}))

    @gen.coroutine
    def post(self, path=""):
        """
        Sets s3 credentials.
        """
        try:
            req = json.loads(self.request.body)
            username = req["infinstorusername"]
            password = req["infinstorpassword"]

            print("InfinStorHandler.post: Entered. username=" + username, file=sys.stderr)

            builtins.cognito_username = username
            builtins.cognito_password = password
            response_json = perform_infinstor_login(username, password)
            print(str(response_json))
            challenge = response_json.get('ChallengeName')
            if challenge == "NEW_PASSWORD_REQUIRED":
                self.finish(json.dumps({"success": False, "message": "NEW_PASSWORD_REQUIRED", "res":response_json}))
            
            infinStorEndpoint = 'https://s3proxy.' + builtins.service + '.com'
            builtins.infinStorAccessKeyId = unquote(response_json.get('InfinStorAccessKeyId'))
            builtins.infinStorSecretAccessKey = unquote(
                    response_json.get('InfinStorSecretAccessKey'))
            setup_credentials()
            productCode = response_json.get('productCode')
            builtins.product = "Starter"
            for code in productCode: 
                if code == "9fcazc4rbiwp6ewg4xlt5c8fu":
                    builtins.product = "Premium" 

            print("InfinStorHandler: Creating new boto3 resource using new endpoint="
                    + infinStorEndpoint + ", infinStorAccessKeyId=" + builtins.infinStorAccessKeyId)
            builtins.s3_resource = boto3.resource(
                "s3",
                aws_access_key_id=builtins.infinStorAccessKeyId,
                aws_secret_access_key=builtins.infinStorSecretAccessKey,
                endpoint_url=infinStorEndpoint
            )

            self.finish(json.dumps({"success": True, "service": builtins.service, "product": builtins.product}))
        except Exception as err:
            self.finish(json.dumps({"success": False, "message": str(err)}))

class InfinSnapHandler(APIHandler):  # pylint: disable=abstract-method
    @gen.coroutine
    def post(self, path=""):
        try:
            req = json.loads(self.request.body)
            infinSnapHostname = req["InfinSnapHostname"]

            print("InfinSnapHandler.post: Entered. InfinSnapHostname=" + infinSnapHostname)
            infinStorEndpoint = 'https://' + infinSnapHostname + '.s3proxy.' + builtins.service \
                    + '.com:443/'
            print("InfinSnapHandler: Creating new boto3 resource using new endpoint="
                    + infinStorEndpoint + ", infinStorAccessKeyId=" + builtins.infinStorAccessKeyId)
            builtins.s3_resource = boto3.resource(
                "s3",
                aws_access_key_id=builtins.infinStorAccessKeyId,
                aws_secret_access_key=builtins.infinStorSecretAccessKey,
                endpoint_url=infinStorEndpoint
            )

            self.finish(json.dumps({"success": True}))
        except Exception as err:
            self.finish(json.dumps({"success": False, "message": str(err)}))

class InfinSliceHandler(APIHandler):  # pylint: disable=abstract-method
    @gen.coroutine
    def post(self, path=""):
        try:
            req = json.loads(self.request.body)
            infinSliceHostname = req["InfinSliceHostname"]

            print("InfinSliceHandler.post: Entered. InfinSliceHostname=" + infinSliceHostname)
            infinStorEndpoint = 'https://' + infinSliceHostname + '.s3proxy.' \
                    + builtins.service + '.com:443/'
            print("InfinSliceHandler: Creating new boto3 resource using new endpoint="
                    + infinStorEndpoint + ", infinStorAccessKeyId=" + builtins.infinStorAccessKeyId)
            builtins.s3_resource = boto3.resource(
                "s3",
                aws_access_key_id=builtins.infinStorAccessKeyId,
                aws_secret_access_key=builtins.infinStorSecretAccessKey,
                endpoint_url=infinStorEndpoint
            )

            self.finish(json.dumps({"success": True}))
        except Exception as err:
            self.finish(json.dumps({"success": False, "message": str(err)}))

class AddLabelHandler(APIHandler):  # pylint: disable=abstract-method
    @gen.coroutine
    def post(self, path=""):
        req = json.loads(self.request.body)

        labelname = req["labelname"]
        bucketname = req["bucketname"]
        if 'pathinbucket' in req:
            pathinbucket = req["pathinbucket"]
        else:
            pathinbucket = ""
        timespec = req["timespec"]
        delimiter = "/"

        payload = "label=" + labelname + "&bucketname=" + bucketname \
                + "&delimiter=" + delimiter + "&prefix=" + pathinbucket \
                + "&timespec=" + timespec
        for retry in range(2):
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': builtins.idtoken
                }

            url = 'https://api.' + builtins.service + '.com/addlabel'
            try:
                response = requests.post(url, data=payload, headers=headers)
                resp_json = response.json()
                response.raise_for_status()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
                self.finish(json.dumps({"success": False, "message": str(http_err)}))
                break
            except Exception as err:
                print(f'Other error occurred: {err}')
                login_expired = False
                for lineb in response.iter_lines():
                    line = str(lineb)
                    try:
                        lind = line.index('Login expired')
                    except ValueError:
                        login_expired = False
                    else:
                        print("addlabel: Login expired. Retrying")
                        login_expired = True
                if login_expired == True:
                    perform_infinstor_login(builtins.cognito_username, builtins.cognito_password)
                    continue
                self.finish(json.dumps({"success": False, "message": str(err)}))
                break
            else:
                print('addlabel success!')
                self.finish(json.dumps({"success": True}))
                break

class ListLabelsHandler(APIHandler):  # pylint: disable=abstract-method
    @gen.coroutine
    def post(self, path=""):
        for retry in range(2):
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': builtins.idtoken
                }

            url = 'https://api.' + builtins.service + '.com/listlabels'
            try:
                response = requests.post(url, data="", headers=headers)
                resp_json = response.json()
                response.raise_for_status()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
                self.finish(json.dumps({"success": False, "message": str(http_err)}))
                break
            except Exception as err:
                print(f'Other error occurred: {err}')
                login_expired = False
                for lineb in response.iter_lines():
                    line = str(lineb)
                    try:
                        lind = line.index('Login expired')
                    except ValueError:
                        login_expired = False
                    else:
                        print("listlabels: Login expired. Retrying")
                        login_expired = True
                if login_expired == True:
                    perform_infinstor_login(builtins.cognito_username, builtins.cognito_password)
                    continue
                self.finish(json.dumps({"success": False, "message": str(err)}))
                break
            else:
                print('listLabelsHandler: listlabels success!')
                print(response.json())
                self.finish(json.dumps({"success": True, "AllLabels": response.json()}))
                break

class UseLabelHandler(APIHandler):  # pylint: disable=abstract-method
    @gen.coroutine
    def post(self, path=""):
        for retry in range(2):
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': builtins.idtoken
                }

            req = json.loads(self.request.body)
            labelname = req["labelname"]
            payload = "label=" + labelname

            url = 'https://api.' + builtins.service + '.com/listlabels'
            try:
                response = requests.post(url, data=payload, headers=headers)
                resp_json = response.json()
                response.raise_for_status()
                labels = resp_json['labels']
                first_label = labels[0]
                timespec = first_label['timespec']
                if timespec.find('-') == -1:
                    print("uselabel: Setting up boto3 for InfinSnap")
                    infinStorEndpoint = 'https://' + timespec + '.s3proxy.' \
                        + builtins.service + '.com:443/'
                else:
                    print("uselabel: Setting up boto3 for InfinSlice")
                    infinStorEndpoint = 'https://' + timespec + '.s3proxy.' \
                        + builtins.service + '.com:443/'
                builtins.s3_resource = boto3.resource(
                    "s3",
                    aws_access_key_id=builtins.infinStorAccessKeyId,
                    aws_secret_access_key=builtins.infinStorSecretAccessKey,
                    endpoint_url=infinStorEndpoint
                )
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
                self.finish(json.dumps({"success": False, "message": str(http_err)}))
                break
            except Exception as err:
                print(f'Other error occurred: {err}')
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                login_expired = False
                for lineb in response.iter_lines():
                    line = str(lineb)
                    try:
                        lind = line.index('Login expired')
                    except ValueError:
                        login_expired = False
                    else:
                        print("uselabel: Login expired. Retrying")
                        login_expired = True
                if login_expired == True:
                    perform_infinstor_login(builtins.cognito_username, builtins.cognito_password)
                    continue
                self.finish(json.dumps({"success": False, "message": str(err)}))
                break
            else:
                print('uselabel: listlabels success')
                self.finish(json.dumps({"success": True, "AllLabels": resp_json}))
                break

class AddXformHandler(APIHandler):  # pylint: disable=abstract-method
    def process_xformcode(self, xfin):
        code_str = unquote(xfin)
        clean_code = ''
        code_str_lines = code_str.splitlines()
        for one_line in code_str_lines:
            if (one_line == '%reset -f'):
                continue
            if (one_line == 'from infinstor import test_once # infinstor'):
                continue
            if (one_line.startswith('input_data_spec') and one_line.endswith('# infinstor')):
                continue
            if (one_line.startswith('rv = test_once') and one_line.endswith('# infinstor')):
                continue
            clean_code += (one_line + '\n')
        quoted_clean_code = quote(clean_code)
        return quoted_clean_code

    @gen.coroutine
    def post(self, path=""):
        req = json.loads(self.request.body)

        xformname = req["xformname"]
        xformcode = req["xformcode"]

        cleaned_xformcode = self.process_xformcode(xformcode)

        payload = "xformname=" + xformname + "&xformcode=" + cleaned_xformcode
        for retry in range(2):
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': builtins.idtoken
                }

            url = 'https://api.' + builtins.service + '.com/addxform'
            try:
                response = requests.post(url, data=payload, headers=headers)
                resp_json = response.json()
                response.raise_for_status()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
                self.finish(json.dumps({"success": False, "message": str(http_err)}))
                break
            except Exception as err:
                print(f'Other error occurred: {err}')
                login_expired = False
                for lineb in response.iter_lines():
                    line = str(lineb)
                    try:
                        lind = line.index('Login expired')
                    except ValueError:
                        login_expired = False
                    else:
                        print("addxform: Login expired. Retrying")
                        login_expired = True
                if login_expired == True:
                    perform_infinstor_login(builtins.cognito_username, builtins.cognito_password)
                    continue
                self.finish(json.dumps({"success": False, "message": str(err)}))
                break
            else:
                print('addxform success!')
                self.finish(json.dumps({"success": True}))
                break

class DeleteXformHandler(APIHandler):  # pylint: disable=abstract-method
    @gen.coroutine
    def post(self, path=""):
        req = json.loads(self.request.body)

        xformname = req["xformname"]

        payload = "xformname=" + xformname
        for retry in range(2):
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': builtins.idtoken
                }

            url = 'https://api.' + builtins.service + '.com/deletexform'
            try:
                response = requests.post(url, data=payload, headers=headers)
                resp_json = response.json()
                response.raise_for_status()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
                self.finish(json.dumps({"success": False, "message": str(http_err)}))
                break
            except Exception as err:
                print(f'Other error occurred: {err}')
                login_expired = False
                for lineb in response.iter_lines():
                    line = str(lineb)
                    try:
                        lind = line.index('Login expired')
                    except ValueError:
                        login_expired = False
                    else:
                        print("deletexform: Login expired. Retrying")
                        login_expired = True
                if login_expired == True:
                    perform_infinstor_login(builtins.cognito_username, builtins.cognito_password)
                    continue
                self.finish(json.dumps({"success": False, "message": str(err)}))
                break
            else:
                print('deletexform success!')
                self.finish(json.dumps({"success": True}))
                break

class ListXformsHandler(APIHandler):  # pylint: disable=abstract-method
    @gen.coroutine
    def post(self, path=""):
        for retry in range(2):
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': builtins.idtoken
                }

            url = 'https://api.' + builtins.service + '.com/listxforms'
            try:
                response = requests.post(url, data="", headers=headers)
                resp_json = response.json()
                response.raise_for_status()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
                self.finish(json.dumps({"success": False, "message": str(http_err)}))
                break
            except Exception as err:
                print(f'Other error occurred: {err}')
                login_expired = False
                for lineb in response.iter_lines():
                    line = str(lineb)
                    try:
                        lind = line.index('Login expired')
                    except ValueError:
                        login_expired = False
                    else:
                        print("listxforms: Login expired. Retrying")
                        login_expired = True
                if login_expired == True:
                    perform_infinstor_login(builtins.cognito_username, builtins.cognito_password)
                    continue
                self.finish(json.dumps({"success": False, "message": str(err)}))
                break
            else:
                print('listXformsHandler: listxforms success!')
                print(response.json())
                self.finish(json.dumps({"success": True, "AllXforms": response.json()}))
                break

class S3AuthHandler(APIHandler):  
    @gen.coroutine
    def post(self, path=""):  
        try:
            req = json.loads(self.request.body)
            endpoint_url = req["endpoint_url"]
            client_id = req["client_id"]
            client_secret = req["client_secret"]
            bucket = getAll_Buckets(endpoint_url,client_id,client_secret)
            self.finish(json.dumps({"success": True,"bucket":bucket}))
        except Exception as err:
            self.finish(json.dumps({"success": False, "message": str(err)}))

class ConformAccountHandler(APIHandler):
    @gen.coroutine
    def post(self, path=""):  
        try:
            req = json.loads(self.request.body)
            email = req["email"]
            username = req["username"]
            session = req["Session"]
            password = req["new_password"]
            payload = "{\n"
            payload += "    \"ChallengeResponses\" : {\n"
            payload += "        \"userAttributes.email\" : \"" + email + "\",\n"
            payload += "        \"NEW_PASSWORD\" : \"" + password + "\",\n"
            payload += "        \"USERNAME\" : \"" + username + "\"\n"
            payload += "    },\n"
            payload += "    \"ChallengeName\" : \"NEW_PASSWORD_REQUIRED\",\n"
            payload += "    \"ClientId\" : \"" + builtins.clientid + "\",\n"
            payload += "    \"Session\" : \"" + session + "\"\n"
            payload += "}\n"
            print("payload" + payload)

            url = 'https://cognito-idp.us-east-1.amazonaws.com:443/'

            headers = {
                    'Content-Type': 'application/x-amz-json-1.1',
                    'X-Amz-Target' : 'AWSCognitoIdentityProviderService.RespondToAuthChallenge'
                    }
            response = requests.post(url, data=payload, headers=headers)
            response.raise_for_status()

            self.finish(json.dumps({"success": True, "message": str(response.json)}))
        except Exception as err:
            self.finish(json.dumps({"success": False, "message": str(err)}))

class S3ResourceNotFoundException(Exception):
    pass


# TODO: use this
#  @dataclass
#  class S3GetResult:
#  name: str
#  type: str
#  path: str


def parse_bucket_name_and_path(raw_path):
    if "/" not in raw_path[1:]:
        bucket_name = raw_path[1:]
        path = ""
    else:
        bucket_name, path = raw_path[1:].split("/", 1)
    return (bucket_name, path)

Content = namedtuple("Content", ["name", "path", "type", "mimetype","last_modified", "size"])

# call with
# request_prefix: the prefix we sent to s3 with the request
# response_prefix: full path of object or directory as returned by s3
# returns:
# subtracts the request_prefix from response_prefix and returns
# the basename of request_prefix
# e.g. request_prefix=rawtransactions/2020-04-01 response_prefix=rawtransactions/2020-04-01/file1
# this method returns file1
def get_basename(request_prefix, response_prefix):
    request_prefix_len = len(request_prefix)
    response_prefix_len = len(response_prefix)
    response_prefix = response_prefix[request_prefix_len:response_prefix_len]
    if (response_prefix.endswith("/")):
        response_prefix_len = len(response_prefix) - 1
        response_prefix = response_prefix[0:response_prefix_len]
    return response_prefix

def do_list_objects_v2(s3client, bucket_name, prefix):
    list_of_objects = []
    list_of_directories = []
    try:
        prefix_len = len(prefix)
        response = s3client.list_objects_v2(Bucket=bucket_name,
                Delimiter="/",
                EncodingType='url',
                Prefix=prefix,
                )
        if 'Contents' in response:
            contents = response['Contents']
            for one_object in contents:
                obj_key = one_object['Key']
                get_last_modified = one_object['LastModified']
                last_modified = get_last_modified.strftime('%m/%d/%Y %H:%M:%S')
                size = one_object['Size']
                obj_key_basename = get_basename(prefix, obj_key)
                if len(obj_key_basename) > 0:
                    list_of_objects.append(Content(obj_key_basename, obj_key, "file", "json", last_modified, size))
        if 'CommonPrefixes' in response:
            common_prefixes = response['CommonPrefixes']
            for common_prefix in common_prefixes:
                prfx = common_prefix['Prefix']
                prfx_basename = get_basename(prefix, prfx)
                list_of_directories.append(Content(prfx_basename, prfx, "directory", "json", "", ""))
    except Exception as e:
        traceback.print_exc()

    return list_of_objects, list_of_directories;

def do_get_object(s3client, bucket_name, path):
    try:
        response = s3client.get_object(Bucket=bucket_name, Key=path)
        if 'Body' in response:
            if 'ContentType' in response:
                content_type = response['ContentType']
            else:
                content_type = 'Unknown'
            streaming_body = response['Body']
            data = streaming_body.read()
            return content_type, data
        else:
            return None
    except Exception as e:
        traceback.print_exc()
        return None

def get_s3_objects_from_path(s3, path):
    
    if path == "/":
        # requesting the root path, just return all buckets
        if builtins.product == "Starter":
            test = boto3.resource("s3")
            all_buckets = test.buckets.all()
            result = [
                {"name": bucket.name, "path": bucket.name, "type": "directory"}
                for bucket in all_buckets
            ]
            return result
        else:
            all_buckets = s3.buckets.all()
            result = [
                {"name": bucket.name, "path": bucket.name, "type": "directory"}
                for bucket in all_buckets
            ]
            return result
    else:
        bucket_name, path = parse_bucket_name_and_path(path)
        s3client = s3.meta.client
        if (path == "" or path.endswith("/")):
            list_of_objects, list_of_directories = do_list_objects_v2(s3client, bucket_name, path)
            result = set()
            if (len(list_of_directories) > 0):
                for one_dir in list_of_directories:
                    result.add(one_dir)
            if (len(list_of_objects) > 0):
                for one_object in list_of_objects:
                    result.add(one_object)

            result = list(result)
            result = [
                {
                    "name": content.name,
                    "path": "{}/{}".format(bucket_name, content.path),
                    "type": content.type,
                    "mimetype": content.mimetype,
                    "last_modified": content.last_modified,
                    "size": content.size
                }
                for content in result
            ]
            return result
        else:
            object_content_type, object_data = do_get_object(s3client, bucket_name, path)
            if object_content_type != None:
                result = {
                    "path": "{}/{}".format(bucket_name, path),
                    "type": "file",
                    "mimetype": object_content_type,
                }
                result["content"] = base64.encodebytes(object_data).decode("ascii")
                return result
            else:
                result = {
                    "error": 404,
                    "message": "The requested resource could not be found.",
                }

class S3Handler(APIHandler):
    """
    Handles requests for getting S3 objects
    """

    @gen.coroutine
    def get(self, path=""):
        """
        Takes a path and returns lists of files/objects
        and directories/prefixes based on the path.
        """

        # boto3.set_stream_logger('boto3.resources', logging.DEBUG)
        # boto3.set_stream_logger('botocore', logging.DEBUG)
        try:
            print("S3Handler.post: Using keyId =" + builtins.infinStorAccessKeyId
                    + ", s3_resource " + str(builtins.s3_resource))
            result = get_s3_objects_from_path(builtins.s3_resource, path)
            if isinstance(result, list):
                result.sort(key=lambda x: x.get('name'))
        except S3ResourceNotFoundException as e:
            result = {
                "error": 404,
                "message": "The requested resource could not be found.",
            }
        except Exception as e:
            print(e)
            result = {"error": 500, "message": str(e)}
        self.finish(json.dumps(result))


def _jupyter_server_extension_paths():
    return [{"module": "jupyterlab_infinstor"}]

def token_renewer_task():
    token_renewer()

def load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.

    Args:
        nb_server_app (NotebookWebApplication):
        handle to the Notebook webserver instance.
    """
    web_app = nb_server_app.web_app
    base_url = web_app.settings["base_url"]
    endpoint = url_path_join(base_url, "s3")
    infinhost = 'mlflowserver.' + builtins.service + '.com'
    handlers = [
        (url_path_join(endpoint, "files") + "(.*)", S3Handler),
        (url_path_join(endpoint, "infinstor") + "(.*)", InfinStorHandler),
        (url_path_join(endpoint, "infinsnap") + "(.*)", InfinSnapHandler),
        (url_path_join(endpoint, "infinslice") + "(.*)", InfinSliceHandler),
        (url_path_join(endpoint, "addlabel") + "(.*)", AddLabelHandler),
        (url_path_join(endpoint, "listlabels") + "(.*)", ListLabelsHandler),
        (url_path_join(endpoint, "uselabel") + "(.*)", UseLabelHandler),
        (url_path_join(endpoint, "addxform") + "(.*)", AddXformHandler),
        (url_path_join(endpoint, "deletexform") + "(.*)", DeleteXformHandler),
        (url_path_join(endpoint, "listxforms") + "(.*)", ListXformsHandler),
        (url_path_join(endpoint, "s3auth") + "(.*)", S3AuthHandler),
        (url_path_join(endpoint, "conformaccount") + "(.*)", ConformAccountHandler),
        (url_path_join(endpoint, r'/mlflowproxy/(\d+)(.*)'), MlflowProxyHandler,\
                {'absolute_url': False, 'host_whitelist': [infinhost]})
    ]
    web_app.add_handlers(".*$", handlers)
    tr = ioloop.PeriodicCallback(token_renewer_task, 180000)
    tr.start()
