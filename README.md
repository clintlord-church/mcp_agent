# MCP Agent

## About

This project is an example of how you can consume MCP Servers with LangChain and LangGraph. 

- **Transport:** stdio transport only
- **Examples:** mcp-atlassian (pip installed), mcp/time (Docker image)

## Prerequisites for Multi-Server Example

To run the Docker MCP server (in multi_server.py), ensure you have the following:

1. Docker installed. You can download and install Docker from [here](https://www.docker.com/get-started).
2. The `mcp/time` Docker image pulled. You can pull the image using the following command:
   ```sh
   docker pull mcp/time
   ```

## Dependency Management

This project uses `pipenv` for dependency management. To install `pipenv`, you can use the following command:
```sh
pip install pipenv
```

To install the project dependencies, run:
```sh
pipenv install
```
