from authorizers.secret.config import SecretAuthorizerConfig
from functions.hello_stamp.config import HelloStampConfig
from functions.hello_world.config import HelloWorldConfig
from docs.config import DocsConfig
from aws_cdk import Stack
from constructs import Construct
from infra.services import Services


class LambdaStack(Stack):
    def __init__(self, scope: Construct, context, **kwargs) -> None:

        super().__init__(scope, f"{context.name}-Lambda-Stack", **kwargs)

        self.services = Services(self, context)

        # Authorizers
        SecretAuthorizerConfig(self.services)

        # Docs
        DocsConfig(self.services)

        # HelloWorld
        HelloWorldConfig(self.services)

        # HelloStamp
        HelloStampConfig(self.services)
