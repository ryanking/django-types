from django.core.management.commands.runserver import (
    Command as RunserverCommand,  # type: ignore
)

class Command(RunserverCommand): ...
