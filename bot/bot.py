"""SE Toolkit Bot — Telegram bot entry point.

Usage:
    uv run bot.py              # Start Telegram bot
    uv run bot.py --test "/start"  # Test mode (no Telegram connection)
"""

import sys
from telegram import Update
from telegram.ext import Application, CommandHandler

from config import load_config
from handlers import handle_start, handle_help, handle_health, handle_labs, handle_scores


def get_handler_for_command(command: str):
    """Get the handler function for a command.
    
    Args:
        command: Command string (e.g., "/start" or "/scores lab-04").
        
    Returns:
        Handler function or None if command not found.
    """
    # Strip leading slash and take only the first word (command name)
    cmd = command.lstrip("/").lower().split()[0]
    
    handlers_map = {
        "start": handle_start,
        "help": handle_help,
        "health": handle_health,
        "labs": handle_labs,
        "scores": handle_scores,
    }
    
    return handlers_map.get(cmd)


async def start_handler(update: Update, context) -> None:
    """Telegram handler for /start command."""
    response = handle_start("/start")
    await update.message.reply_text(response)


async def help_handler(update: Update, context) -> None:
    """Telegram handler for /help command."""
    response = handle_help("/help")
    await update.message.reply_text(response)


async def health_handler(update: Update, context) -> None:
    """Telegram handler for /health command."""
    response = handle_health("/health")
    await update.message.reply_text(response)


async def labs_handler(update: Update, context) -> None:
    """Telegram handler for /labs command."""
    response = handle_labs("/labs")
    await update.message.reply_text(response)


async def scores_handler(update: Update, context) -> None:
    """Telegram handler for /scores command."""
    # Get the lab name from arguments if provided
    args = context.args
    command = "/scores"
    if args:
        command = f"/scores {' '.join(args)}"
    response = handle_scores(command)
    await update.message.reply_text(response)


def run_test_mode(command: str) -> None:
    """Run a command in test mode (no Telegram connection).
    
    Args:
        command: Command string (e.g., "/start").
    """
    handler = get_handler_for_command(command)
    
    if handler is None:
        print(f"Unknown command: {command}. Use /help to see available commands.")
        sys.exit(0)  # Exit with 0 even for unknown commands
    
    response = handler(command)
    print(response)
    sys.exit(0)


def run_telegram_bot(config: dict) -> None:
    """Start the Telegram bot.
    
    Args:
        config: Configuration dictionary with BOT_TOKEN.
    """
    bot_token = config.get("BOT_TOKEN")
    
    if not bot_token:
        print("Error: BOT_TOKEN not found in .env.bot.secret")
        sys.exit(1)
    
    # Create application
    application = Application.builder().token(bot_token).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("help", help_handler))
    application.add_handler(CommandHandler("health", health_handler))
    application.add_handler(CommandHandler("labs", labs_handler))
    application.add_handler(CommandHandler("scores", scores_handler))
    
    # Start polling
    print("Bot started...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


def main() -> None:
    """Main entry point."""
    # Check for --test mode
    if len(sys.argv) >= 2 and sys.argv[1] == "--test":
        if len(sys.argv) < 3:
            print("Usage: uv run bot.py --test <command>")
            print("Example: uv run bot.py --test '/start'")
            sys.exit(1)
        
        command = sys.argv[2]
        run_test_mode(command)
        return
    
    # Normal mode: start Telegram bot
    config = load_config()
    run_telegram_bot(config)


if __name__ == "__main__":
    main()
