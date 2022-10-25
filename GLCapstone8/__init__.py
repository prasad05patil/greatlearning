import logging

import azure.functions as func
from . import sumNumber

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    v1 = req.params.get('v1')
    v2 = req.params.get('v2')
    print("You are in Great learning function app", v1,v2)
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully. Sum of {v1} + {v2} = {sumNumber.sumnumbers(v1,v2)}")

    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
