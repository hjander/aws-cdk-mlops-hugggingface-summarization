from aws_cdk import Stack, Environment
from aws_cdk.pipelines import ShellStep
from constructs import Construct

from cdk_pipelines_github import GitHubActionRole, GitHubWorkflow, AwsCredentials

from huggingface_summarization_application import MLOpsHuggingFaceSummarizationApplication


class MLOpsHuggingFaceSummarizationPipelineStack(Stack):


    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        role = GitHubActionRole(self, 'CdkGitHubActionRole', repos=['hjander/aws-cdk-mlops-hugggingface-summarization'])
