#!/usr/bin/env python3
from aws_cdk import App, Environment
from aws_cdk.pipelines import ShellStep
from cdk_pipelines_github import GitHubWorkflow, AwsCredentials

from huggingface_summarization_application import MLOpsHuggingFaceSummarizationApplication
from pipeline.pipeline_stack import MLOpsHuggingFaceSummarizationPipelineStack

env = Environment(account="763597864486", region="us-east-1")

app = App()

pipeline = GitHubWorkflow(app, 'MLOpsHuggingFaceSummarizationGithubWorkflow',
                          workflow_name="tst",
                          aws_creds=AwsCredentials.from_open_id_connect(
                              git_hub_action_role_arn='arn:aws:iam::763597864486:role/GitHubActionRole'),
                          synth=ShellStep("Synth",
                                          commands=["npm install -g aws-cdk",
                                                    "pip install -r requirements.txt",
                                                    "cdk synth"]
                                          )
                          )

pipeline.add_stage(MLOpsHuggingFaceSummarizationApplication(app, 'MLOpsHuggingFaceSummarizationApplication', env=env))

app.synth()
