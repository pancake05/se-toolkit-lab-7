"""Command handlers implementation.

Each handler is a function that takes a command string and returns a text response.
Handlers don't know about Telegram — they're pure functions.
"""


def handle_start(command: str) -> str:
    """Handle /start command.
    
    Args:
        command: The command string (e.g., "/start").
        
    Returns:
        Welcome message text.
    """
    return "Welcome to SE Toolkit Bot! Use /help to see available commands."


def handle_help(command: str) -> str:
    """Handle /help command.
    
    Args:
        command: The command string (e.g., "/help").
        
    Returns:
        List of available commands.
    """
    return """Available commands:
/start — Welcome message
/help — Show this help
/health — Check backend status
/labs — List available labs
/scores — View your scores"""


def handle_health(command: str) -> str:
    """Handle /health command.
    
    Args:
        command: The command string (e.g., "/health").
        
    Returns:
        Backend health status.
    """
    # TODO: In Task 2, check actual backend health
    return "Backend status: OK (placeholder)"


def handle_labs(command: str) -> str:
    """Handle /labs command.
    
    Args:
        command: The command string (e.g., "/labs").
        
    Returns:
        List of available labs.
    """
    # TODO: In Task 2, fetch from LMS API
    return "Available labs: lab-01, lab-02, lab-03, lab-04 (placeholder)"


def handle_scores(command: str) -> str:
    """Handle /scores command.
    
    Args:
        command: The command string with optional lab name (e.g., "/scores lab-04").
        
    Returns:
        Scores information.
    """
    # TODO: In Task 2, fetch from LMS API
    return "Scores: Not implemented yet (placeholder)"
