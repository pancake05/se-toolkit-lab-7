"""LMS API client.

TODO: Implement in Task 2.
"""

from config import load_config


class LMSAPIClient:
    """Client for LMS API with Bearer token authentication."""
    
    def __init__(self, config: dict):
        """Initialize LMS API client.
        
        Args:
            config: Configuration dictionary with LMS_API_BASE_URL and LMS_API_KEY.
        """
        self.base_url = config.get("LMS_API_BASE_URL", "")
        self.api_key = config.get("LMS_API_KEY", "")
    
    async def health_check(self) -> dict:
        """Check backend health status.
        
        Returns:
            Health status dictionary.
        """
        # TODO: Implement in Task 2
        return {"status": "ok"}
    
    async def get_labs(self) -> list:
        """Get list of available labs.
        
        Returns:
            List of lab dictionaries.
        """
        # TODO: Implement in Task 2
        return []
    
    async def get_scores(self, lab_name: str) -> dict:
        """Get scores for a specific lab.
        
        Args:
            lab_name: Lab identifier (e.g., "lab-04").
            
        Returns:
            Scores dictionary.
        """
        # TODO: Implement in Task 2
        return {}
