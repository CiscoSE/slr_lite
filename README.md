# Lightweight SLR Authorization File Generator

This lightweight tool automatically generates authorization files for Cisco devices within the scope of Specific License Reservation (SLR).
It requires a list of devices to be registered together with the corresponding reservation request codes and license entitlement tags.

---
## Table of Contents
  * [1. Requirements](#1-requirements)
  * [2. Setup](#2-setup)
    + [Get API access](#get_api_access)
    + [Install required libraries](#install-required-libraries)
    + [Edit configuration file](#edit-configuration-file)
  * [3. Usage](#3-usage)
    + [Edit host file](#edit-host-file)
    + [Run the tool](#run-the-tool)

---

## 1. Requirements

Prior to installing and running the program, the following requirements should be met:
- A valid CCO/Cisco.com account
- Python 3.X
- Internet conection to Cisco Software Central

---

## 2. Setup

Copy the repository to your local machine and follow the steps described in the following.

### Get API access
In order to use the tool, it is necessary to get access to the Smart Licensing API. The API calls inside the code are authenticated by a `client ID` and the corresponding `client secret`. To register and get the client ID and secret, make sure you have a valid CCO/Cisco.com account and click on [Mulesoft - Cisco API Server](https://anypoint.mulesoft.com/apiplatform/apx#/portals/organizations/1c92147b-332d-4f44-8c0e-ad3997b5e06d/apis/5418104/versions/102456/pages/425744)
  
The link has instructions to register a new application:

    * Use an arbitrary application name
    * Select 'Resource Owner Grant' and 'Client Credentials Grant' type from the options for OAuth grant type.

A confirmation will appear upon successful application registration. Also, an email notification will be sent as confirmation to the email id(s) mentioned while submitting the request. Please note down the Client Id & Secret. These will be used to generate the OAuth 2.0 Bearer token to access APIs.

Important - The Client Id & Secret generated will be ready to use immediately under normal circumstances. If you get an 401 while making the API call, please allow another 30 mins while the Client Id propagates to all the availability zones. If you have any questions or concerns please reach out to operations team at smart-operations@cisco.com

### Install required libraries
Open the terminal and type in:

```bash
$ pip3 install -r requirements.txt
```

### Edit configuration file
The `config.json` file is the central configuration file for the tool. It should be edited for API authentication and authorization purposes:
- `client_id`: Smart licensing API client ID
- `client_secret`: Smart licensing API client secret
- `username`: Cisco.com username
- `password`: Cisco.com password
- `smartAccountDomain`: Smart account domain name
- `virtualAccountName`: Name of the virtual account within the smart account domain

---

## 3. Usage

In order to run the app, you need to define the devices to be registered. The devices are listed in the `hosts.json` file which is used as an input for the tool.

### Edit the host file
Relace the variable names inside the default `hosts.json` file with the right values for your devices.

### Run the tool
After editing the host file, run the app by typing:

```bash
$ python3 main.py
```