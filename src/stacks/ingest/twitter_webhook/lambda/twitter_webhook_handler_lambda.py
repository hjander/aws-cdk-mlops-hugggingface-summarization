import base64
import hashlib
import hmac
import json
import os

# from aws_lambda_powertools import Logger
from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver, Response

apiGatewayResolver = ApiGatewayResolver(debug=True)

logger = Logger(service="twitter_webhook_crc")


@logger.inject_lambda_context(log_event=False)
@apiGatewayResolver.get("/twitter_webhook")
def webhook_crc_challenge_handler():
    TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')

    crc_token = apiGatewayResolver.current_event.get_query_string_value(name="crc_token")

    sha256_hash_digest = hmac.new(bytes(TWITTER_CONSUMER_SECRET, encoding='utf8'),
                                  bytes(crc_token, encoding='utf8'),
                                  digestmod=hashlib.sha256).digest()
    body = {
        "response_token": "sha256=" + str(base64.b64encode(sha256_hash_digest), encoding='utf8')
    }

    response = Response(status_code=200,
                        content_type="application/json",
                        body=json.dumps(body))

    return response


# entry point
def handler(event, context):
    return apiGatewayResolver.resolve(event, context)
