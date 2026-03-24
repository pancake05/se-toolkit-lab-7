# SE Toolkit Bot — Development Plan

## Overview

This document describes the development plan for the SE Toolkit Telegram bot. The bot provides students with access to their LMS (Learning Management System) data through a Telegram interface. It supports slash commands like `/start`, `/help`, `/health`, `/labs`, `/scores`, and later integrates with an LLM to understand natural language questions.

## Architecture

The bot follows the **separation of concerns** pattern:

- **Handlers** (`handlers/`) — Pure functions that take a command and return text. They don't know about Telegram, making them testable without a Telegram connection via `--test` mode.
- **Services** (`services/`) — External API clients for LMS and LLM. These handle HTTP requests, authentication with Bearer tokens, and error handling.
- **Entry Point** (`bot.py`) — Telegram startup logic and `--test` mode. Routes incoming commands to appropriate handlers.
- **Configuration** (`config.py`) — Loads secrets from `.env.bot.secret` using environment variables.

## Task Breakdown

**Task 1: Scaffold** — Create `bot/` directory structure with `handlers/` and `services/`. Implement `--test` mode for offline verification. Create placeholder handlers for all commands. Write this development plan.

**Task 2: Backend Integration** — Create `services/lms_api.py` with HTTP client for LMS API. Implement Bearer token authentication. Replace placeholder handlers with real API calls for `/health`, `/labs`, `/scores`.

**Task 3: LLM Intent Routing** — Create `services/llm_client.py` for LLM API. Add tool definitions describing each command. Enable natural language understanding so users can ask questions without slash commands.

**Task 4: Docker Deployment** — Create `Dockerfile` for the bot. Configure Docker networking to reach backend and LLM services using service names instead of `localhost`. Deploy to VM and verify end-to-end functionality.

## Dependencies

- `python-telegram-bot` — Telegram Bot API library
- `httpx` — Async HTTP client for API calls
- `python-dotenv` — Load environment variables from `.env.bot.secret`

## Environment Variables

Required in `.env.bot.secret`:

- `BOT_TOKEN` — Telegram bot token from BotFather
- `LMS_API_BASE_URL` — Base URL for LMS backend (e.g., `http://localhost:42002`)
- `LMS_API_KEY` — API key for LMS authentication
- `LLM_API_KEY` — API key for LLM service (Task 3+)
- `LLM_API_BASE_URL` — Base URL for LLM service (Task 3+)
