# This File contains the functions for the communication between the frontend (Client) and the backend (Server).
# The following Communication Channels are implemented:
# - REST API
# - Websocket

# Import of the required packages
import os
import requests
import websocket

# Loading of Custom Modules
from ..functions.help_env import load_env_file, find_env_file


# Function to build the URL for the REST API
def build_url_rest_api() -> str:
    """
    This function builds the URL for the REST API.
    :return: URL for the REST API
    """
    # Load the environment variables
    load_env_file()

    # Get the required environment variables
    SERVER_BASE_URL = os.getenv("SERVER_BASE_URL")
    ENDPOINT_API = os.getenv("SERVER_API_DYN_URL")

    # Build the URL
    url_api = f"{SERVER_BASE_URL}/{ENDPOINT_API}"

    # Return the URL
    return url_api


# Function to build the URL for the Websocket
def build_url_websocket() -> str:
    """
    This function builds the URL for the Websocket.
    :return: URL for the Websocket
    """
    # Load the environment variables
    load_env_file()

    # Get the required environment variables
    SERVER_BASE_URL = os.getenv("SERVER_BASE_URL")
    ENDPOINT_WEBSOCKET = os.getenv("SERVER_WEBSOCKET_DYN_URL")

    # Build the URL
    url_websocket = f"{SERVER_BASE_URL}/{ENDPOINT_WEBSOCKET}"

    # Return the URL
    return url_websocket


# Function to send a request to the REST API
def send_request_rest_api(request_type: str, request_data: dict = None) -> dict:
    """
    This function sends a request to the REST API.
    :param request_type: Type of the request
    :param request_data: Data of the request
    :return: Response of the request
    """
    # Build the URL
    url_api = build_url_rest_api()

    # Send the request
    response = requests.request(request_type, url_api, json=request_data)

    # Return the response
    return response.json()


# Function to connect to the Websocket
def connect_websocket() -> websocket.WebSocket:
    """
    This function connects to the Websocket.
    :return: Websocket
    """
    # Build the URL
    url_websocket = build_url_websocket()

    # Connect to the Websocket
    ws = websocket.create_connection(url_websocket)

    # Return the Websocket
    return ws
