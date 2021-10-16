import os

import twitter
from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver

apiGatewayResolver = ApiGatewayResolver(debug=True)

logger = Logger(service="twitter_polling_lambda")

TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')



@logger.inject_lambda_context(log_event=True)
def twitter_polling_handler(event, context):




    twitter.GetHomeTimeline(
        count=200,
        since_id=None,
        max_id=None,
        trim_user=False,
        exclude_replies=False,
        contributor_details=False,
        include_entities=True)

    return response
