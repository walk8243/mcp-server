from mcp.server.fastmcp import FastMCP

# サーバーの定義
mcp = FastMCP("My Dockerized MCP Server")

@mcp.tool()
def add(x: int, y: int) -> int:
    """2つの数字を足し算します"""
    return x + y

if __name__ == "__main__":
    # Docker内で実行するため、stdioで待ち受けます
    mcp.run()
