[overview]: #overview
[prerequisites]: #pre-requisites
[local]: #running-locally
[deploy]: #deploy
[logs]: #application-logs
[cleanup]: #cleanup
[scripts]: #scripts
[enroll]: #enroll-your-endpoint-in-asa
[simulate]: #simulate-events
[authorizeandreturns]: #authorize-and-returns
[clearingandvoid]: #clearing-and-void
[listtransactions]: #listing-transactions
[createcard]: #create-a-card
[testing]: #testing

# Auth Stream Access (ASA) Python Example Application

## Table of Contents

- [Overview](#overview)
- [Pre-requisites](#pre-requisites)
- [Running locally](#running-locally)
- [Deploy](#deploy)
- [Application Logs](#application-logs)
- [Cleanup](#cleanup)
- [Scripts](#scripts)
  * [Enroll your endpoint in ASA](#enroll-your-endpoint-in-asa)
  * [Simulate Events](#simulate-events)
    + [Authorize and Returns](#authorize-and-returns)
    + [Clearing and Void](#clearing-and-void)
    + [Listing Transactions](#listing-transactions)
  * [Create a Card](#create-a-card)
- [Testing](#testing)

## Overview

This is a sample application for creating an auth stream access webhook with [AWS API Gateway](https://aws.amazon.com/api-gateway/) and [Lambda](https://aws.amazon.com/lambda/), managed via [AWS Serverless Application Model (SAM)](https://aws.amazon.com/serverless/sam/).

By default, the endpoint is configured to authorize all transactions except those where the merchant is registered in the state of Connecticut (CT), or in which the merchants' category code is "5933" or "5945". These were randomly selected to demonstrate a "deny" workflow. If you wish to modify the behavior, edit the files `webhook/app.py` and `webhook/authorization.py` to your needs.

## Pre-requisites

* This repository uses Python, and requires that you use Python 3.6+. The Lambda uses a runtime of Python 3.9.
* You must have the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) and [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) installed.
* Configure your local AWS environment (run `aws configure`).
* Make sure you have a Sandbox API Key. You can get your API Key by navigating to your [account](https://lithic.com/account) page. After enabling the API, you will have access to both a production and sandbox API key. Be sure to use the **Sandbox** key for this demo. For more information, please refer to our [documentation](https://docs.lithic.com/docs/auth-stream-access-asa).

## Running locally

To start the API locally run the following command:

```bash
sam local start-api
```

The API will start on port 3000. You can perform an authorized request against the local API as follows:

```bash
curl -XPOST http://localhost:3000/webhook -d '{"token": "abcdefgh", "merchant": {"state": "NY", "mcc": "5922"}}'
```

In this example, the lambda will respond with an "authorize" response and echo the token in the response.

## Deploy

To deploy the application, run the following commands:

```bash
sam build
sam deploy --guided
```

Once complete, your new API endpoint will be output to your terminal.

If you make any modifications to the lambda or the template, re-run these two commands to re-deploy your application.

## Application Logs

Once deployed, you can fetch logs with the following command:

```bash
sam logs -n ASAWebhookFunction --stack-name lithic-asa-demo-python --tail
```

## Cleanup

To delete the sample application that you created, run the following:

```bash
aws cloudformation delete-stack --stack-name lithic-asa-demo-python
```

## Scripts

This respository includes some scripts for interacting with the Lithic Sandbox API. Before running these scripts, set up a virtual environment and install local requirements:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.local.txt
```

It may be helpful to store your Lithic Sandbox API key in your `~/.bashrc` or equivalent so that you do not need to include it in each script command:

```bash
echo 'export LITHIC_SANDBOX_KEY={your_key} >> ~/.bashrc`
```

Alternatively, if you do not have the Sandbox API Key set as an environment variable, the scripts will prompt you to enter one when run.

### Enroll your endpoint in ASA

Using the API Gateway endpoint URL (this URL is output to the terminal after you run the deploy), run the following script to enroll in ASA:

```bash
python3 scripts/enroll.py {your_api_endpoint}
```

If you need to change the enrolled endpoint, disenroll before re-enrolling your new endpoint:

```bash
python3 scripts/disenroll.py
```

### Simulate Events

This repository provides a script for simulating any of the following events:

* authorize
* return
* clearing
* void

To do so, run the following script:

```bash
python3 scripts/simulate.py {action}
```

Depending on which action you are simulating, different arguments are required. See below for additional details.

#### Authorize and Returns

* **required** `pan`: A valid PAN; if you need to quickly create a card for testing, see the "Create a Card" script below.
* `amount`: An amount (in cents) to authorize or return. Defaults to 0.
* `descriptor`: Merchant descriptor. Defaults to "Sample descriptor".

Example request:

```bash
python3 scripts/simulate.py authorize --pan 4111111289144142 --amount 52 --descriptor 'coffee shop'
```

#### Clearing and Void

* **required** `token`: a transaction token returned from an `authorize` response.
* `amount`: Amount (in cents) to clear or void. Typically this will match the original authorization, but may be more or less. If no amount is supplied, the amount of the transaction will be cleared or voided. Any transaction that has any amount completed at all do not have access to this behavior.

Example request:

```bash
python3 scripts/simulate.py clearing --token {uuid} --amount 20
```

#### Listing Transactions

Now that you've processed a bunch of transactions, you can list them with:

```bash
python3 scripts/transactions.py
```

Given this can produce a lengthy list of transactions, it may be helpful to pipe the output to [jq](https://stedolan.github.io/jq/):

```bash
python3 scripts/transactions.py | jq
```

### Create a Card

If you need to create a card for testing, you can use the following script:

```bash
python3 scripts/create_card.py
```

This creates an unlocked card in an open state that can be used for testing. 

## Testing

This demo application includes unit tests for testing the endpoint and authorization logic. To run the test suite, from within your virtual environment, install the test dependencies:

```bash
pip3 install -r tests/requirements.txt
```

Once installed, you can run the tests with [pytest](https://docs.pytest.org/en/6.2.x/):

```bash
pytest tests/
```
