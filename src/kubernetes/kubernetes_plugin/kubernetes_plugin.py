import subprocess


def _kubectl_command(command: str) -> str:
    """Execute a kubectl command.

    Args:
        command (str): The command.

    Returns:
        str: The response.
    """

    response = subprocess.check_output(command, shell=True).decode("utf-8", errors="replace")

    return response

