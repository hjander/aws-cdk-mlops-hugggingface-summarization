from aws_cdk.core import Stage

from stacks.ingest.twitter_webhook.twitter_ingest_stack import TwitterIngestStack


class MLOpsHuggingFaceSummarizationApplication(Stage):

    def __init__(self, scope, id, *, env=None, outdir=None):
        super().__init__(scope, id, env=env, outdir=outdir)

        twitter_ingest = TwitterIngestStack(self, "TwitterIngestStack")
