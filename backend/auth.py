"""
Authentication middleware for API Key validation
"""

from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
import crud_api_keys


async def verify_api_key(
    x_api_key: str = Header(..., description="API Key for authentication"),
    db: Session = Depends(get_db)
):
    """
    Verify API key from header
    
    Args:
        x_api_key: API key from X-API-Key header
        db: Database session
    
    Returns:
        APIKey object if valid
    
    Raises:
        HTTPException if invalid
    """
    is_valid, error_message, api_key = crud_api_keys.validate_api_key(db, x_api_key)
    
    if not is_valid:
        raise HTTPException(
            status_code=401,
            detail=error_message or "Invalid API key",
            headers={"WWW-Authenticate": "ApiKey"}
        )
    
    # Increment usage count
    crud_api_keys.increment_api_key_usage(db, api_key)
    
    return api_key


async def optional_api_key(
    x_api_key: str = Header(None, description="Optional API Key"),
    db: Session = Depends(get_db)
):
    """
    Optional API key verification
    Returns None if no key provided, validates if provided
    
    Args:
        x_api_key: Optional API key from X-API-Key header
        db: Database session
    
    Returns:
        APIKey object if valid, None if not provided
    
    Raises:
        HTTPException if provided but invalid
    """
    if not x_api_key:
        return None
    
    return await verify_api_key(x_api_key, db)
