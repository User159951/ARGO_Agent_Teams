from agno.team import TeamAgent

from agents.deep_knowledge import create_agent as deep_knowledge
from agents.research_agent import research_agent
from agents.research_agent_exa import research_scholar
from agents.competitor_analysis_agent import competitor_analysis_agent
from agents.media_trend_analysis_agent import agent as media_trend_analyst
from agents.web_extraction_agent import agent as web_extractor
from agents.social_media_agent import social_media_agent
from agents.readme_generator import readme_gen_agent

team_research = TeamAgent(
    name="Team Research & Strategy",
    description="Agents spécialisés en recherche stratégique, concurrentielle, et rédaction avancée.",
    agents=[
        deep_knowledge(),
        research_agent,
        research_scholar,
        competitor_analysis_agent,
        media_trend_analyst,
        web_extractor,
        social_media_agent,
        readme_gen_agent,
    ],
    routing_strategy="auto",
    add_history_to_messages=True,
    markdown=True
)

if __name__ == "__main__":
    query = input("Fais-moi un SWOT de OpenAI contre Anthropic.")
    team_research.print_response(query, stream=True)
