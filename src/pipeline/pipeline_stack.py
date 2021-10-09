from aws_cdk import core as cdk
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep

from huggingface_summarization_application import MLOpsHuggingFaceSummarizationApplication


class MLOpsHuggingFaceSummarizationPipelineStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline = CodePipeline(self, "MLOpsHuggingFaceSummarizationBuildPipeline",
                                pipeline_name="MLOpsHuggingFaceSummarizationBuildPipeline",
                                docker_enabled_for_synth=True,
                                synth=ShellStep("Synth",
                                                input=CodePipelineSource.git_hub(
                                                    repo_string="hjander/aws-cdk-mlops-hugggingface-summarization",
                                                    branch="master"),
                                                commands=["npm install -g aws-cdk",
                                                          "pip install -r requirements.txt",
                                                          "cdk synth"]
                                                )
                                )

        pipeline.add_stage(MLOpsHuggingFaceSummarizationApplication(self, 'MLOpsHuggingFaceSummarizationApplication'))
