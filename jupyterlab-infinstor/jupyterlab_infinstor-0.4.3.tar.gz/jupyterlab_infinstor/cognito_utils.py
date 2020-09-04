import requests
from requests.exceptions import HTTPError
import json
import builtins
import os
from os.path import expanduser
from os.path import sep as separator
import datetime

verbose = False

def read_token_file(tokfile):
    fclient_id = None
    ftoken = None
    frefresh_token = None
    ftoken_time = None
    fservice = None
    with (open(tokfile)) as fp:
        for count, line in enumerate(fp):
            if (line.startswith('ClientId=')):
                fclient_id = line[len('ClientId='):].rstrip()
            if (line.startswith('Token=')):
                ftoken = line[len('Token='):].rstrip()
            if (line.startswith('RefreshToken=')):
                frefresh_token = line[len('RefreshToken='):].rstrip()
            if (line.startswith('TokenTimeEpochSeconds=')):
                ftoken_time = int(line[len('TokenTimeEpochSeconds='):].rstrip())
            if (line.startswith('Service=')):
                fservice = line[len('Service='):].rstrip()
    return ftoken, frefresh_token, ftoken_time, fclient_id, fservice

def write_token_file(tokfile, token_time, token, refresh_token, client_id, service):
    os.makedirs(os.path.dirname(tokfile), exist_ok=True)
    with open(tokfile, 'w') as wfile:
        wfile.write("Token=" + token + "\n")
        wfile.write("RefreshToken=" + refresh_token + "\n")
        wfile.write("ClientId=" + client_id + "\n")
        wfile.write("TokenTimeEpochSeconds=" + str(token_time) + "\n")
        wfile.write("Service=" + service + "\n")
        wfile.close()

def renew_token(tokfile, refresh_token, client_id, service):
    payload = "{\n"
    payload += "    \"AuthParameters\" : {\n"
    payload += "        \"REFRESH_TOKEN\" : \"" + refresh_token + "\"\n"
    payload += "    },\n"
    payload += "    \"AuthFlow\" : \"REFRESH_TOKEN_AUTH\",\n"
    payload += "    \"ClientId\" : \"" + client_id + "\"\n"
    payload += "}\n"

    url = 'https://cognito-idp.us-east-1.amazonaws.com:443/'

    headers = {
            'Content-Type': 'application/x-amz-json-1.1',
            'X-Amz-Target' : 'AWSCognitoIdentityProviderService.InitiateAuth'
            }

    if (verbose):
        print("Calling renew_token with payload=" + payload)

    try:
        response = requests.post(url, data=payload, headers=headers)
    except Exception as err:
        print("renew_token: Caught " + str(err))
        raise
    else:
        if (response.status_code != 200):
            print("renew_token: Error. http status_code is " + str(response.status_code)
                    + ", response=" + str(response.text))
        else:
            authres = response.json()['AuthenticationResult']
            token = authres['IdToken']
            token_time = round(datetime.datetime.timestamp(datetime.datetime.utcnow()))
            write_token_file(tokfile, token_time, token, refresh_token, client_id, service)

def token_renewer():
    home = expanduser("~")
    dotinfinstor = home + separator + ".infinstor"
    tokfile = dotinfinstor + separator + "token"

    token = None
    refresh_token = None
    token_time = None
    client_id = None
    service = None
    token, refresh_token, token_time, client_id, service = read_token_file(tokfile)
    time_now = round(datetime.datetime.timestamp(datetime.datetime.utcnow()))
    if ((token_time + (30 * 60)) < time_now):
        if (verbose):
            print('InfinStor token has expired. Calling renew ' + str(token_time)\
                + ', ' + str(time_now))
        renew_token(tokfile, refresh_token, client_id, service)
        token, refresh_token, token_time, client_id, service = read_token_file(tokfile)
    else:
        if (verbose):
            print('InfinStor token has not expired ' + str(token_time) + ', ' + str(time_now))

def perform_infinstor_login(username, password):
    payload = "{\n"
    payload += "    \"AuthParameters\" : {\n"
    payload += "        \"USERNAME\" : \"" + username + "\",\n"
    payload += "        \"PASSWORD\" : \"" + password + "\"\n"
    payload += "    },\n"
    payload += "    \"AuthFlow\" : \"USER_PASSWORD_AUTH\",\n"
    payload += "    \"ClientId\" : \"" + builtins.clientid + "\"\n"
    payload += "}\n"

    url = 'https://cognito-idp.us-east-1.amazonaws.com:443/'

    headers = {
            'Content-Type': 'application/x-amz-json-1.1',
            'X-Amz-Target' : 'AWSCognitoIdentityProviderService.InitiateAuth'
            }

    try:
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        raise
    except Exception as err:
        print(f'Other error occurred: {err}')
        raise
    else:
        print('Authorization success!')
        challenge = response.json().get('ChallengeName')
        if challenge == "NEW_PASSWORD_REQUIRED":
            return response.json()
        else:
            authres = response.json()['AuthenticationResult']
            builtins.idtoken = authres['IdToken']
            builtins.refreshtoken = authres['RefreshToken']

    setup_token_for_mlflow()

    payload = ("ProductCode=" + builtins.prodcode)
    headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': builtins.idtoken
            }

    url = 'https://api.' + builtins.service + '.com/customerinfo'

    try:
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        raise
    except Exception as err:
        print(f'Other error occurred: {err}')
        raise
    else:
        print('customerinfo success!')
        return response.json()


def setup_token_for_mlflow():
    home = expanduser("~")
    dotinfinstor = home + separator + ".infinstor"
    print("Setting up token for mlflow in " + dotinfinstor)
    if (not os.path.exists(dotinfinstor)):
        try:
            os.mkdir(dotinfinstor, mode=0o755)
        except Exception as err:
            print('Error creating dir ' + dotinfinstor)
    tokfile = dotinfinstor + separator + "token"
    with open(tokfile, 'w') as wfile:
        wfile.write("Token=" + builtins.idtoken + "\n")
        wfile.write("RefreshToken=" + builtins.refreshtoken + "\n")
        wfile.write("ClientId=" + builtins.clientid + "\n")
        wfile.write("TokenTimeEpochSeconds="\
                + str(round(datetime.datetime.timestamp(datetime.datetime.utcnow()))) + "\n")
        wfile.write("Service=" + builtins.service + "\n")
        wfile.close()

