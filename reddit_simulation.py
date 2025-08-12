import asyncio
import os
from dotenv import load_dotenv
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
import oasis
from oasis import (ActionType, LLMAction, ManualAction, generate_reddit_agent_graph)

# Load environment variables from .env file
load_dotenv()

async def main():
    # Define the model for the agents
    openai_model = ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI,
        model_type=ModelType.GPT_4O_MINI,
    )

    # Define the available actions for the agents
    available_actions = [
        ActionType.LIKE_POST,
        ActionType.DISLIKE_POST,
        ActionType.CREATE_POST,
        ActionType.CREATE_COMMENT,
        ActionType.LIKE_COMMENT,
        ActionType.DISLIKE_COMMENT,
        ActionType.SEARCH_POSTS,
        ActionType.SEARCH_USER,
        ActionType.TREND,
        ActionType.REFRESH,
        ActionType.DO_NOTHING,
        ActionType.FOLLOW,
        ActionType.MUTE,
    ]

    agent_graph = await generate_reddit_agent_graph(
        profile_path="./data/reddit/user_data_36.json",
        model=openai_model,
        available_actions=available_actions,
    )

    # Define the path to the database
    db_path = "./data/reddit_simulation.db"

    # Delete the old database if it exists
    if os.path.exists(db_path):
        os.remove(db_path)

    # Make the environment
    env = oasis.make(
        agent_graph=agent_graph,
        platform=oasis.DefaultPlatformType.REDDIT,
        database_path=db_path,
    )

    # Run the environment
    await env.reset()
    
    # Define manual actions for the first agent
    actions_1 = {}
    actions_1[env.agent_graph.get_agent(0)] = [
        ManualAction(
            action_type=ActionType.CREATE_POST,
            action_args={"content": "Hello, world!"}
        ),
        ManualAction(
            action_type=ActionType.CREATE_COMMENT,
            action_args={
                "post_id": 1,
                "content": "This is a comment!"
            }
        ),
    ]

    # Execute the manual actions
    result_1 = await env.step(actions_1)
    print("Manual actions executed:")
    if result_1:
        for agent_id, observations in result_1.items():
            print(f"Agent {agent_id}: {observations}")
    else:
        print("No observations returned from manual actions")

    # Let a few agents act autonomously for a limited number of steps
    print("\nRunning autonomous simulation for 2 steps with first 3 agents...")
    for step in range(2):
        print(f"\nStep {step + 1}:")
        
        # Let only the first 3 agents decide their actions using LLM to avoid rate limits
        actions = {}
        for i in range(min(3, len(env.agent_graph.get_agents()))):
            agent = env.agent_graph.get_agent(i)
            actions[agent] = [LLMAction()]
        
        # Execute the step
        result = await env.step(actions)
        
        # Print results
        if result:
            for agent_id, observations in result.items():
                if observations:  # Only print if there are observations
                    print(f"Agent {agent_id}: {observations}")
        else:
            print(f"No observations returned for step {step + 1}")

    print("\nSimulation completed!")
    print(f"Database saved at: {db_path}")

if __name__ == "__main__":
    asyncio.run(main())
