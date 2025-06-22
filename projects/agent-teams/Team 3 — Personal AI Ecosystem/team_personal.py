from agno.team import TeamAgent

from agents.book_recommendation import book_recommendation_agent
from agents.movie_recommedation import movie_recommendation_agent
from agents.recipe_creator import recipe_agent
from agents.recipe_rag_image import agent as recipe_visual_agent
from agents.youtube_agent import youtube_agent
from agents.translation_agent import agent as translator_agent
from agents.study_partner import study_partner
from agents.agno_support_agent import create_agent as agno_helper
from agents.airbnb_mcp import run_agent as airbnb_agent

team_personal = TeamAgent(
    name="Team Personal AI",
    description="Agents utiles au quotidien : recommandation, apprentissage, traduction, vidéo, cuisine.",
    agents=[
        book_recommendation_agent,
        movie_recommendation_agent,
        recipe_agent,
        recipe_visual_agent,
        youtube_agent,
        translator_agent,
        study_partner,
        agno_helper(),
        # airbnb_agent est async — à intégrer séparément dans une app async
    ],
    routing_strategy="auto",
    add_history_to_messages=True,
    markdown=True
)

if __name__ == "__main__":
    query = input("Je veux une recette végétarienne rapide avec riz et poivron.")
    team_personal.print_response(query, stream=True)
