#!/usr/bin/env python3
from aws_cdk import App, Environment

from pipeline.pipeline_stack import MLOpsHuggingFaceSummarizationPipelineStack

env = Environment(account="763597864486", region="us-east-1")

app = App()
MLOpsHuggingFaceSummarizationPipelineStack(app, "MLOpsHuggingFaceSummarizationPipelineStack", env=env)

app.synth()
