#!/usr/bin/env python3

from aws_cdk import core as cdk

from pipeline.pipeline_stack import MLOpsHuggingFaceSummarizationPipelineStack

app = cdk.App()
MLOpsHuggingFaceSummarizationPipelineStack(app, "MLOpsHuggingFaceSummarizationPipelineStack",
                               env=cdk.Environment(account="763597864486", region="us-east-1")
                               )


app.synth()
