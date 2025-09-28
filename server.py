# server.py

from fastmcp import FastMCP
from resources import register_resources
from tools import register_tools
from prompts import register_prompts
from sendQueue import start_send_queue_processor
from tools import register_tools
from readQueue import start_read_queue

def setup_server() -> FastMCP:
    """Initializes and configures the MCP server instance."""
    print("Setting up MCP server...")
    mcp = FastMCP("MHacks 2025 MCP Server")
    
    # Register all handlers
    register_resources(mcp, {"IR-GP2Y0A21YK0F"})
    register_tools(mcp, {"Piezo Buzzer"})
    register_prompts(mcp)
    print("All resources, tools, and prompts have been registered.")

    start_send_queue_processor()
    start_read_queue()
    
    return mcp

# Create the server object for FastMCP Cloud
mcp = setup_server()

if __name__ == "__main__":
    mcp.run()