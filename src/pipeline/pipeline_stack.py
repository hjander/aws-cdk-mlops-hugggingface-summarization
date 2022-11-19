from aws_cdk import Stack, Environment
from aws_cdk.pipelines import ShellStep
from constructs import Construct

from cdk_pipelines_github import GitHubActionRole, GitHubWorkflow, AwsCredentials

from huggingface_summarization_application import MLOpsHuggingFaceSummarizationApplication


class MLOpsHuggingFaceSummarizationPipelineStack(Stack):


    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # role = GitHubActionRole(self, 'CdkGitHubActionRole', repos=['hjander/aws-cdk-mlops-hugggingface-summarization'])

        pipeline = GitHubWorkflow(self, 'MLOpsHuggingFaceSummarizationGithubWorkflow',
                                  workflow_name="tst",
                                  aws_creds=AwsCredentials.from_open_id_connect(
                                      git_hub_action_role_arn='arn:aws:iam::763597864486:role/GitHubActionRole'),
                                  synth=ShellStep("Synth",
                                                  commands=["npm install -g aws-cdk",
                                                            "pip install -r requirements.txt",
                                                            "cdk synth"]
                                                  )
                                  )

        pipeline.add_stage(MLOpsHuggingFaceSummarizationApplication(self, 'MLOpsHuggingFaceSummarizationApplication'))
