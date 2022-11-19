from aws_cdk import Stack
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from constructs import Construct

from huggingface_summarization_application import MLOpsHuggingFaceSummarizationApplication



class MLOpsHuggingFaceSummarizationPipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
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
