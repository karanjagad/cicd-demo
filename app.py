#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_codepipeline.aws_codepipeline_stack import AwsCodepipelineStack


app = cdk.App()
AwsCodepipelineStack(
    app,
    "CicdDemoStack",
    env=cdk.Environment(account="488050839102", region="eu-central-1"),
    stack_name="github-cicd-demo-stack",
)

app.synth()
