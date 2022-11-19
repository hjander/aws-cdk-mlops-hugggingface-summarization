from aws_cdk import Stage

from stacks.ingest.sa_mail.sa_mail_ingest_stack import SaMailIngestStack
from stacks.ingest.st_poller.twitter_polling_ingest_stack import StPollingIngestStack
from stacks.ingest.twitter_webhook.twitter_ingest_stack import TwitterIngestStack


class MLOpsHuggingFaceSummarizationApplication(Stage):

    def __init__(self, scope, id, *, env=None, outdir=None):
        super().__init__(scope, id, env=env, outdir=outdir)

        twitter_ingest = TwitterIngestStack(self, "TwitterIngestStack")
        saMailIngestStack = SaMailIngestStack(self, "SaMailIngestStack")
        stPollingIngestStack = StPollingIngestStack(self, "StPollingIngestStack")
