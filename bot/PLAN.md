# SE Toolkit Bot — Plan

## Overview

Telegram bot for LMS access with commands `/start`, `/help`, `/health`, `/labs`, `/scores`, plus LLM.

## Architecture

**Separation of concerns**:

- **Handlers**  Pure functions, testable without Telegram.
- **Services**  API clients for LMS and LLM.
- **Entry Point**  `bot.py` with `--test` mode.
- **Configuration**  Loads `.env.bot.secret.
