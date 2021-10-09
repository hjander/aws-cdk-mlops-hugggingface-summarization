from aws_cdk import core as cdk
from aws_cdk.aws_apigateway import LambdaIntegration, RestApi, AwsIntegration, MethodLoggingLevel
from aws_cdk.aws_iam import Role, ServicePrincipal
from aws_cdk.aws_lambda import Runtime, LambdaInsightsVersion
from aws_cdk.aws_lambda_python import PythonFunction
from aws_cdk.aws_logs import RetentionDays
from aws_cdk.aws_s3 import Bucket
from aws_cdk.aws_secretsmanager import Secret

from aws_cdk.core import Stack


# https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks

class TwitterIngestStack(Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        secret = Secret(self, "twitterConsumerSecret", secret_name="twitter/webhook/api/key")

        crcHandlerFunction = PythonFunction(self, "twitterWebhookCrcHandlerFunction",
                                            entry="src/stacks/ingest/twitter_webhook/lambda",
                                            index="twitter_webhook_handler_lambda.py",
                                            # handler="lambda",
                                            function_name='twitter-webhook-crc-handler',
                                            insights_version=LambdaInsightsVersion.VERSION_1_0_98_0,
                                            log_retention=RetentionDays.TWO_MONTHS,
                                            runtime=Runtime.PYTHON_3_9,
                                            environment={
                                                'TWITTER_CONSUMER_SECRET': secret.secret_value.to_string()
                                            })

        raw_data_bucket = Bucket(self, "rawDataBucket", "twitter-ingest-bucket")

        twitter_ingest_api = RestApi(self, "twitterIngestWebhookApi",
                                     deploy_options={
                                         "logging_level": MethodLoggingLevel.INFO,
                                         "data_trace_enabled": True
                                     })

        api_gw_execute_role = Role(self, "role",
                                   assumed_by=ServicePrincipal('apigateway.amazonaws.com'),
                                   path="/service-role/")

        raw_data_bucket.grant_read_write(api_gw_execute_role)

        twitter_ingest_api_gw_s3_integration = AwsIntegration(service='s3', integration_http_method="PUT",
                                                              path=raw_data_bucket.bucket_name + '/twitter', options={
                'credentials_role': api_gw_execute_role
            })

        twitter_webhook_resource = twitter_ingest_api.root.add_resource("twitter_webhook")
        twitter_webhook_resource.add_method("POST", twitter_ingest_api_gw_s3_integration)
        twitter_webhook_resource.add_method("GET", LambdaIntegration(crcHandlerFunction))
