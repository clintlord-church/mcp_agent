from langchain_openai import AzureChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
import os

model = AzureChatOpenAI(model="gpt-4o-mini")

atlassian_parameters = {
    "command": "mcp-atlassian",
    "args": [f"--confluence-url={os.environ.get('CONFLUENCE_URL')}", 
          f"--confluence-personal-token={os.environ.get('CONFLUENCE_PERSONAL_TOKEN')}", 
          f"--jira-url={os.environ.get('JIRA_URL')}", 
          f"--jira-username={os.environ.get('JIRA_USERNAME')}", 
          f"--jira-token={os.environ.get('JIRA_API_TOKEN')}"]
}

async def main():
    async with MultiServerMCPClient() as client:
        await client.connect_to_server("Atlassian", command=atlassian_parameters['command'], args=atlassian_parameters['args'])

        agent = create_react_agent(model, client.get_tools())
        agent_response = await agent.ainvoke({"messages": "Find the ticket in the STAV project that talks about setting up the mac mini with splunk.  Keep trying searches until you find it."})
        # agent_response = await agent.ainvoke({"messages": "Give me the details on ticket STAV-2660"})
        # agent_response = await agent.ainvoke({"messages": "Find the machine configuration for the agentic design workshop.  Keep trying different searches until you find the one with specific setup steps."})
        return agent_response

# run the main function
if __name__ == "__main__":
    import asyncio
    result = asyncio.run(main())
    print(result['messages'][-1].content)  # Print the final response from the model