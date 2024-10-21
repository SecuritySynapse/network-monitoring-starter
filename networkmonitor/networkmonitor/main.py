"""Create clients and servers on localhost and then monitor network traffic."""

from enum import Enum

import typer
from rich.console import Console

from networkmonitor.client import start_client_socket, start_client_xmlrpc
from networkmonitor.intercept import start_intercept_socket_xmlrpc
from networkmonitor.server import start_socket_server, start_xmlrpc_server

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for rich text output
console = Console()


class Mode(Enum):
    """An enumeration of the possible modes for the network monitoring tool."""

    server_socket = "server_socket"
    client_socket = "client_socket"
    intercept_socket = "intercept_socket"
    intercept_xmlrpc = "intercept_xmlrpc"
    server_xmlrpc = "server_xmlrpc"
    client_xmlrpc = "client_xmlrpc"


@cli.command()
def networkmonitor(
    mode: Mode = typer.Option(
        Mode.server_socket,
        "--mode",
        help="Specify the mode for the network monitor.",
    ),
) -> None:
    """Conduct a network monitoring campaign with different components."""
    # TODO: Add a complete implementation of the main function
    # for the network monitoring tool as described in the README.md file
    return None
