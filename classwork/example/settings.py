import os


APP_PROJECT_DIRECTORY = os.environ.get(
    "APP_PROJECT_DIRECTORY",
    default=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
)

APP_LOG_LEVEL = os.environ.get(
    "APP_LOG_LEVEL",
    default="INFO"
)

APP_TIMESTAMP_FORMAT = os.environ.get(
    "APP_TIMESTAMP_FORMAT",
    default="%Y-%m-%dT%H:%M:%SZ"
)
