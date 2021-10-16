import base64
import hashlib
import hmac
import json
import os

from aws_lambda_powertools import Logger
import twitter
from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver, Response

apiGatewayResolver = ApiGatewayResolver(debug=True)

logger = Logger(service="twitter_polling_lambda")


@logger.inject_lambda_context(log_event=True)
def twitter_polling_handler(event, context):

    TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
    TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')

    twitterApi = twitter.Api(consumer_key='OiGEuB6FCJj43bBaSMMBcYw2s',
                      consumer_secret='wFfOP4oRwI3ecNWs9ezkwXpe1MCkV2RjngU4S9yYGBKm6kmisz',
                      access_token_key='1333143704689840130-vZ25lm1tFA2DEDb7gGYa6a9cMLjJn4',
                      access_token_secret='LO9puWozD5wVo3ZZMMa5zTjghiuf6xITBKEMSp4A9oSLM')



    return response

