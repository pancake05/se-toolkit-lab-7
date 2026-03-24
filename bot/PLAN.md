# SE Toolkit Bot — Development Plan

## Overview

This document describes the development plan for the SE Toolkit Telegram bot. The bot provides students with access to their LMS (Learning Management System) data through a Telegram interface. It supports slash commands like `/start`, `/help`, `/health`, `/labs`, and `/scores`, and later integrates with an LLM to understand natural language questions.

## Architecture

### Separation of Concerns

The bot follows the **separation of concerns** pattern:

- **Handlers** (`handlers/`) — Pure functions that take a command and return text. They don't know about Telegram, making them testable without a Telegram connection.
- **Services** (`services/`) — External API clients (LMS API, LLM API). These handle HTTP requests, authentication, and error handling.
- **Entry Point** (`bot.py`) — Telegram startup logic and `--test` mode. Routes incoming commands to handlers.
- **Configuration** (`config.py`) — Loads secrets from `.env.bot.secret` using environment variables.

### Test Mode

The `--test` flag allows running commands locally without Telegram:

```bash
uv run bot.py --test "/start"
```

This calls handlers directly and prints responses to stdout. The same handlers are used by both test mode and the real Telegram bot.

## Task Breakdown

### Task 1: Scaffold (Current)

- Create `bot/` directory structure
- Implement `--test` mode
- Create placeholder handlers for `/start`, `/help`, `/health`, `/labs`, `/scores`
- Set up `pyproject.toml` with dependencies
- Write this plan

### Task 2: Backend Integration

- Create `services/lms_api.py` — HTTP client for LMS API
- Implement Bearer token authentication using `LMS_API_KEY`
- Replace placeholder handlers with real API calls:
  - `/health` — Check backend health endpoint
  - `/labs` — Fetch list of available labs
  - `/scores` — Fetch scores for a specific lab

### Task 3: LLM Intent Routing

- Create `services/llm_client.py` — Client for LLM API
- Add tool definitions for each command (describe what each handler does)
- Implement natural language understanding:
  - User asks "what labs do I have?" → LLM calls `handle_labs`
  - User asks "my score for lab-04" → LLM calls `handle_scores("lab-04")`
- Update system prompt with tool descriptions

### Task 4: Docker Deployment

- Create `Dockerfile` for the bot
- Configure Docker networking to reach backend and LLM services
- Use service names (not `localhost`) for container-to-container communication
- Deploy to VM and verify end-to-end functionality

## Dependencies

- `python-telegram-bot` — Telegram Bot API
- `httpx` — Async HTTP client for API calls
- `python-dotenv` — Load environment variables from `.env.bot.secret`

## Environment Variables

Required in `.env.bot.secret`:

- `BOT_TOKEN` — Telegram bot token
- `LMS_API_BASE_URL` — Base URL for LMS backend
- `LMS_API_KEY` — API key for LMS authentication
- `LLM_API_KEY` — API key for LLM service (Task 3+)
- `LLM_API_BASE_URL` — Base URL for LLM service (Task 3+)
