from agno.team import TeamAgent

from agents.finance_agent import finance_agent
from agents.finance_agent_with_memory import finance_agent_with_memory
from agents.thinking_finance_agent import finance_agent as thinking_agent
from agents.reasoning_finance_agent import agent as reasoning_agent
from agents.basic_agent import agent as basic_finance
from agents.shopping_partner import agent as shopping_agent
from agents.meeting_summarizer_agent import meeting_agent
from agents.agno_assist import create_agent as agno_support

team_finance = TeamAgent(
    name="Team Finance & Business",
    description="Agents pour l'analyse de marché, les rapports financiers, la mémoire utilisateur et le support business.",
    agents=[
        finance_agent,
        finance_agent_with_memory,
        thinking_agent,
        reasoning_agent,
        basic_finance,
        shopping_agent,
        meeting_agent,
        agno_support(),
    ],
    routing_strategy="auto",
    add_history_to_messages=True,
    markdown=True
)

if __name__ == "__main__":
    query = input("Analyse les résultats de Nvidia du dernier trimestre.")
    team_finance.print_response(query, stream=True)
