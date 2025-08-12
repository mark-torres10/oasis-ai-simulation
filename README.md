# OASIS Reddit Simulation Project

🏝️ This project demonstrates how to set up and run OASIS (Open Agent Social Interaction Simulations) for Reddit-style social media simulations.

## About OASIS

OASIS is a scalable, open-source social media simulator that integrates large language models with rule-based agents to realistically mimic the behavior of up to one million users on platforms like Twitter and Reddit. It's designed to facilitate the study of complex social phenomena such as information spread, group polarization, and herd behavior.

## Project Structure

```
oasis-project/
├── data/
│   └── reddit/
│       └── user_data_36.json      # Agent profiles for 36 Reddit users
├── reddit_simulation.py           # Main simulation script
├── setup_env.py                   # Environment setup helper
├── README.md                       # This file
└── pyproject.toml                  # UV project configuration
```

## Setup Instructions

### 1. Prerequisites

- Python 3.11+
- UV package manager (already installed)
- OpenAI API key

### 2. Installation

The project is already set up with UV and OASIS installed. The setup includes:

- `camel-oasis` package and all dependencies
- Required data files (user profiles)
- Virtual environment in `.venv/`

### 3. Environment Configuration

Run the setup script to configure your OpenAI API key:

```bash
uv run setup_env.py
```

This script will:
- Check your OASIS installation
- Verify required data files
- Help you set up your OpenAI API key
- Optionally configure a custom OpenAI base URL

Alternatively, you can manually set your environment variables:

```bash
# For zsh (default on macOS)
export OPENAI_API_KEY="your_api_key_here"
export OPENAI_API_BASE_URL="https://api.openai.com/v1"  # Optional
```

### 4. Running the Simulation

Once configured, run the Reddit simulation:

```bash
uv run reddit_simulation.py
```

## What the Simulation Does

The simulation demonstrates:

1. **Agent Creation**: Creates 36 AI agents with different Reddit user profiles
2. **Manual Actions**: Executes some predefined actions (creating posts and comments)
3. **Autonomous Behavior**: Lets agents interact autonomously for several steps
4. **Data Persistence**: Saves all interactions to a SQLite database

### Available Agent Actions

Agents can perform these Reddit-like actions:
- `LIKE_POST` / `DISLIKE_POST`
- `CREATE_POST` / `CREATE_COMMENT`
- `LIKE_COMMENT` / `DISLIKE_COMMENT`
- `SEARCH_POSTS` / `SEARCH_USER`
- `FOLLOW` / `MUTE`
- `TREND` / `REFRESH`
- `DO_NOTHING`

## Output

The simulation will:
- Print real-time updates as agents interact
- Create a SQLite database at `./data/reddit_simulation.db`
- Show observations and actions for each simulation step

## Key Features

- **Scalable**: Can simulate up to 1 million agents
- **Realistic**: Uses LLMs to generate human-like behavior
- **Configurable**: Easy to modify agent profiles and available actions  
- **Data-Rich**: Comprehensive logging of all interactions

## Use Cases

- **Research**: Study social phenomena like information spread and group polarization
- **Testing**: Validate social media features and policies
- **Education**: Learn about social dynamics and AI behavior
- **Content Creation**: Generate realistic social media interactions

## Troubleshooting

### Common Issues

1. **Missing API Key**: Make sure `OPENAI_API_KEY` is set
2. **Rate Limits**: OpenAI has rate limits; consider using GPT-4O-MINI for testing
3. **Database Locks**: The simulation removes old databases automatically

### Getting Help

- Check the [OASIS Documentation](https://docs.oasis.camel-ai.org/)
- Visit the [GitHub Repository](https://github.com/camel-ai/oasis)
- Review the [Quickstart Guide](https://docs.oasis.camel-ai.org/quickstart)

## Next Steps

After running the basic simulation, you can:

1. **Customize Agent Profiles**: Modify `user_data_36.json` or create new profiles
2. **Add More Actions**: Extend the available actions list
3. **Scale Up**: Increase the number of agents
4. **Analyze Results**: Query the SQLite database to analyze interactions
5. **Try Twitter Simulation**: Switch to Twitter platform simulation

## License

This project follows the OASIS project license. See the [official repository](https://github.com/camel-ai/oasis) for details.