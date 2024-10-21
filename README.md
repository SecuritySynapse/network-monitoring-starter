# 🔬 Network Monitoring

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## ✨ Table of Contents

<!---toc start-->

* [🔬 Network Monitoring](#-network-monitoring)
  * [✨ Table of Contents](#-table-of-contents)
  * [🏁 Introduction](#-introduction)
  * [🤝 Seeking Assistance](#-seeking-assistance)
  * [🛫 Project Overview](#-project-overview)
    * [Features](#features)
    * [Command-Line Interface](#command-line-interface)
    * [Diagnostic Information](#diagnostic-information)
    * [Running the Program](#running-the-program)
    * [Getting Started](#getting-started)
    * [Additional Information](#additional-information)

<!---toc end-->

## 🏁 Introduction

If you are a student completing this project as part of a class at Allegheny
College, you can check the schedule on the course web site for the due date or
ask the course instructor for more information about the due date. You can also
find the deadline for the project, as reported by GitHub Classroom, by clicking
the grey box at the top of this file. Please furthermore note that the content
provided in the `README.md` file for this GitHub repository is an overview of
the project and thus may not include the details for every step needed to
successfully complete every project deliverable. This means that you may need to
schedule a meeting during the course instructor's office hours to discuss
aspects of this project.

## 🤝 Seeking Assistance

Even though the course instructor will have covered all of the concepts central
to this project before you start to work on it, please note that not every
detail needed to successfully complete the assignment will have been covered
during prior classroom sessions. This is by design as an important skill that
you must practice as an algorithm engineer is to search for and then understand
and ultimately apply the technical content found in additional resources.

## 🛫 Project Overview

This project invites you to implement and use a program called `networkmonitor`
that conducts network monitoring by creating clients and servers on localhost
and then monitoring the network traffic between the client and the server. The
program supports different modes of operation, including server and client modes
using either sockets or XML-RPC, and interception modes for monitoring network
communication with either of the aforementioned protocols.

### Features

- **Modes**:
  - **Client and Server Protocols**:
    - *Server Socket*: Start a server using sockets.
    - *Client Socket*: Start a client using sockets.
    - *Server XML-RPC*: Start a server using XML-RPC.
    - *Client XML-RPC*: Start a client using XML-RPC.
  - **Interception Mechanisms**:
    - *Intercept Socket*: Intercept network communication that uses sockets.
    - *Intercept XML-RPC*: Intercept network communication that uses XML-RPC.

### Command-Line Interface

The `networkmonitor` program uses the `typer` library to provide a command-line
interface. You can specify its mode of operation using the `--mode` option.

- Example usage for running the server:

```sh
poetry run networkmonitor --mode server_socket
```

- Example usage for running the client:

```sh
poetry run networkmonitor --mode client_socket
```

- Example usage for running the socket-based interception as `root` on Linux:

```sh
sudo poetry run networkmonitor --mode intercept_socket
```

Please note that these commands must be run in this order and, in particular,
the use of the program's `intercept_socket` mode will require root privileges on
most operating systems. The completed implementation of your `networkmonitor`
program should also support all of the aforementioned modes for the XML-RPC
protocol. It is also important to note that your implementation of the
`networkmonitor` should assume that the client and server are running on the
same machine; this limiting assumption is acceptable for the purposes of this
assignment because it ensures that you do not need to address any ethical and
compliance issues related to network monitoring on the College's network.

### Diagnostic Information

When it is run in `client` mode, the `networkmonitor` program should randomly
generate strings of a specified length and send them to the server. When it is
run in `server` mode, the program should receive the strings from the client and
then it should echo the received strings along with a timestamp that shows the
precise moment in time when the string was received.

The `networkmonitor` program also displays diagnostic information about the
configuration parameters and the network communication interception. When the
client communicates with the server and the `networkmonitor` is run in
interception mode, then it should report the following information for each
intercepted packet:

- Complete contents of intercepted packet in `byte`s
- TCP-Based payload of the intercepted packet in `byte`s
- IP-Based payload of the intercepted packet in `byte`s
- Source IP address embedded in the packet's IP header
- Destination IP address embedded in the packet's IP header
- Source Port embedded in the packet
- Destination Port embedded in the packet

To implement the `intercept` mode of `networkmonitor`, you should use the
features provided by the `socket` module that is built-in to Python. Here are
some additional details about the `intercept` mode:

- Details about the `parse_ip_header` function in the `intercept.py` file.
  - **Purpose**: Parses the IP header from a given byte sequence.
  - **Steps**:
    - Unpacks the first 20 bytes of the data using the IP header format.
    - Extracts the source IP address.
    - Extracts the destination IP address.
    - Returns the source IP, destination IP, and the remaining data after the IP
    header.

- Details about the `parse_tcp_header` function in the `intercept.py` file.
  - **Purpose**: Parses the TCP header from a given byte sequence.
  - **Steps**:
    - Unpacks the first 20 bytes of the data using the TCP header format.
    - Extracts the source port.
    - Extracts the destination port.
    - Returns the source port, destination port, and the remaining data after
    the TCP header.

### Running the Program

To run the `networkmonitor` program, you can use the following command:

```sh
poetry run networkmonitor --mode <mode>
```

When running the program, make sure to replace `<mode>` with one of the
supported modes: `server_socket`, `client_socket`, `server_xmlrpc`,
`client_xmlrpc`, `intercept_socket`, `intercept_xmlrpc`. It is possible that
your implementation of the interception mode may be general-purpose enough to
handle client-server communication with both sockets and XML-RPC. Please see the
course instructor to receive a demonstration of the various types of program
output that are expected when running the `networkmonitor` program in its
various modes.

### Getting Started

After cloning this repository to your computer, please take the following steps
to get started on the project:

- Make sure that you are using a recent version of Python 3.12 to complete this
assignment by typing `python --version` in your terminal; if you are not using a
recent version of Python please upgrade before proceeding.
- Make sure that you are using a recent version of Poetry 1.8 to complete this
assignment by typing `poetry --version` in your terminal; if you are not using a
recent version of Poetry please upgrade before proceeding.
- Before moving to the next step, you may need to again type `poetry install`
one or more times in order to avoid the appearance of warnings when you next run
the `networkmonitor` program.

### Additional Information

- If you have already installed the
[GatorGrade](https://github.com/GatorEducator/gatorgrade) program that runs the
automated grading checks provided by
[GatorGrader](https://github.com/GatorEducator/gatorgrader) you can, from the
repository's base directory, run the automated grading checks by typing
`gatorgrade --config config/gatorgrade.yml`.
- You may also review the output from running GatorGrader in GitHub Actions.
- Don't forget to provide all of the required responses to the technical writing
prompts in the `writing/reflection.md` file.
- Please make sure that you completely delete the `TODO` markers and their
labels from all of the provided source code. This means that instead of only
deleting the `TODO` marker from the code you should delete the `TODO` marker and
the entire prompt and then add your own comments to demonstrate that you
understand all of the source code in this project.
- Please make sure that you also completely delete the `TODO` markers and their
labels from every line of the `writing/reflection.md` file. This means that you
should not simply delete the `TODO` marker but instead delete the entire prompt
so that your reflection is a document that contains polished technical writing
that is suitable for publication on your professional web site.
