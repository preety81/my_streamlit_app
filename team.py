from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv
from agno.models.groq import Groq
from agno.team import Team


load_dotenv()

eng_Agent = Agent(name="English Agent", role="You answer questions in English")
Hindi_Agent = Agent(name="Hindi Agent", role="You answer questions in Hindi")
Japanese_Agent = Agent(name="Japenese Agent", role="You answer questions in Japanese")
Chinese_Agent = Agent(name="Chinese Agent", role="You answer questions in Chinese")

team_leader = Team(
    name = "Answer & Translation Team",
    members = [eng_Agent, Hindi_Agent, Japanese_Agent,Chinese_Agent,],
    model = Groq(id="qwen/qwen3-32b"),
    markdown = True,
    show_members_responses = True,
    instructions="""All member agents musst respond to answer in their specific language.
                    Do not route to just one Agent.
                    Output the response of all agent.
                    """
)

team_leader.print_response("What is the capital of India")