from aws_cdk import core as cdk
from aws_cdk.aws_events import Schedule, Rule
from aws_cdk.aws_events_targets import LambdaFunction
from aws_cdk.aws_lambda import LambdaInsightsVersion, Runtime
from aws_cdk.aws_lambda_python import PythonFunction
from aws_cdk.aws_logs import RetentionDays
from aws_cdk.aws_s3 import Bucket
from aws_cdk.aws_ssm import StringParameter, ParameterTier
from aws_cdk.core import Stack, Duration


# https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks

class StPollingIngestStack(Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        twitterPollingIngestBucket = Bucket(self, "TwitterPollingIngestBucket",
                                            bucket_name="twitter-poller-ingest-bucket")

        twitterPollerFunction = PythonFunction(self, "TwitterPollerFunction",
                                               entry="src/stacks/ingest/st_poller/lambda",
                                               index="twitter_polling_handler_lambda.py",
                                               # handler="lambda",
                                               function_name='twitter_polling_handler',
                                               insights_version=LambdaInsightsVersion.VERSION_1_0_98_0,
                                               log_retention=RetentionDays.TWO_MONTHS,
                                               runtime=Runtime.PYTHON_3_9)

        pollingScheduleRule = Rule(self, "TwitterPollingScheduleRule",
                                   schedule=Schedule.rate(duration=Duration.minutes(5)),
                                   targets=[LambdaFunction(twitterPollerFunction)]
                                   )

        ssmPollingState = StringParameter(self, "TwitterPollingState",
                                          allowed_pattern=".*",
                                          description="The currect state of polling parameter",
                                          parameter_name="max_id",
                                          string_value="0",
                                          tier=ParameterTier.STANDARD
                                          )

        #twitterPollerFunction.grant_invoke(pollingScheduleRule)

        ssmPollingState.grant_read(twitterPollerFunction)
        twitterPollingIngestBucket.grant_read_write(twitterPollerFunction)
