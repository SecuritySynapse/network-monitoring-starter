"""Implementation of localhost client(s)."""

# TODO: All a complete implementation for both clients

import random
import socket
import string
import time
import xmlrpc.client

from rich.console import Console

# create a console for rich text output
console = Console()


def generate_random_string(length: int = 10) -> str:
    """Generates a random string of specified length."""
    return ""


# Client socket function
def start_client_socket(rounds: int = 100) -> None:
    """Create a client socket to send messages to the server."""
    return None

def start_client_xmlrpc(rounds: int = 100) -> None:
    """Send random strings to the XML-RPC server."""
    return None
