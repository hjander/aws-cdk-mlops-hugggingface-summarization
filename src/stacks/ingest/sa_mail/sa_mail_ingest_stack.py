import aws_cdk.aws_ses as ses
import aws_cdk.aws_ses_actions as actions
from aws_cdk import core as cdk
from aws_cdk.aws_s3 import Bucket
from aws_cdk.core import Stack


# https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks

class SaMailIngestStack(Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # secret = Secret(self, "saMailAddress", secret_name="sa/mail/address")
        sa_mail_address = "sa_mail@holygraal.io"

        saMailIngestBucket = Bucket(self, "SaMailIngestBucket", bucket_name="sa-mail-ingest-bucket")

        # saMailHandlerFunction = PythonFunction(self, "saMailHandlerFunction",
        #                                        entry="src/stacks/ingest/sa_mail/lambda",
        #                                        index="sa_mail_handler_lambda.py",
        #                                        # handler="lambda",
        #                                        function_name='sa-mail-handler',
        #                                        insights_version=LambdaInsightsVersion.VERSION_1_0_98_0,
        #                                        log_retention=RetentionDays.TWO_MONTHS,
        #                                        runtime=Runtime.PYTHON_3_9)

        ses.ReceiptRuleSet(self, "SaMailIngestSesRuleSet", rules=[
            ses.ReceiptRuleOptions(
                recipients=[sa_mail_address],
                actions=[
                    actions.S3(
                        bucket=saMailIngestBucket,
                        object_key_prefix="sa_mail/"
                    )
                ]
            )
        ])
