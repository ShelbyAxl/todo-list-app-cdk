#!/usr/bin/env python3

import aws_cdk as cdk

from todo_list_app_cdk.todo_list_app_cdk_stack import TodoListAppCdkStack


app = cdk.App()
TodoListAppCdkStack(app, "TodoListAppCdkStack")

app.synth()
