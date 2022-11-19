#!/usr/bin/env python3

from aws_cdk import Environment, App
from pipeline.pipeline_stack import MLOpsHuggingFaceSummarizationPipelineStack

app = App()
MLOpsHuggingFaceSummarizationPipelineStack(app, "MLOpsHuggingFaceSummarizationPipelineStack",
                               env=Environment(account="763597864486", region="us-east-1")
                               )


app.synth()
