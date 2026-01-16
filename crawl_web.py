from crawl4ai import AsyncWebCrawler
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("crawlWeb_to_markdown")


@mcp.tool()
async def crawlWeb_to_markdown(url: str) -> str:
    """获取URL的内容并转换为Markdown"""
    try:
        # Create an instance of AsyncWebCrawler
        async with AsyncWebCrawler() as crawler:
            # Run the crawler on a URL
            result = await crawler.arun(url=url)
            print(result.markdown)
            # Return the markdown content of the result
            return result.markdown if result.markdown else "未能获取到内容"
    except Exception as e:
        return f"爬取过程中出现错误: {str(e)}"



def main():
    mcp.run(transport="streamable-http")

if __name__ == "__main__":
    main()
