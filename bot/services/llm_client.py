"""LLM client for intent routing.

TODO: Implement in Task 3.
"""

from config import load_config


class LLMClient:
    """Client for LLM API with tool calling support."""
    
    def __init__(self, config: dict):
        """Initialize LLM client.
        
        Args:
            config: Configuration dictionary with LLM_API_KEY and LLM_API_BASE_URL.
        """
        self.api_key = config.get("LLM_API_KEY", "")
        self.base_url = config.get("LLM_API_BASE_URL", "")
        self.model = config.get("LLM_API_MODEL", "qwen3-coder-plus")
    
    async def process_query(self, query: str) -> str:
        """Process a natural language query using LLM.
        
        Args:
            query: User's question in natural language.
            
        Returns:
            Response text.
        """
        # TODO: Implement in Task 3
        return "LLM not implemented yet."
