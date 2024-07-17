from infra.services import Services

class HelloStampConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="HelloStamp",
            path="./functions/hello_stamp",
            description="A simple hello word",
            
        )

        services.api_gateway.create_endpoint("GET", "/hello_stamp", function, authorizer="secret")

            