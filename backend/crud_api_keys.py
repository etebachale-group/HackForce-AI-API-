"""
CRUD operations for API Keys
"""

from sqlalchemy.orm import Session
from sqlalchemy import func
# from models import APIKey  # Temporarily disabled - enable after creating api_keys table
from datetime import datetime, timedelta
from typing import Optional, List

# Placeholder - will be enabled when APIKey model is uncommented
APIKey = None


def create_api_key(db: Session, name: str, email: str, company: Optional[str] = None, 
                   rate_limit: int = 1000, expires_in_days: Optional[int] = None) -> APIKey:
    """
    Create a new API key
    
    Args:
        db: Database session
        name: Friendly name for the key
        email: User email
        company: Optional company name
        rate_limit: Requests per day limit
        expires_in_days: Optional expiration in days
    
    Returns:
        Created APIKey object
    """
    # Generate unique key
    key = APIKey.generate_key()
    
    # Calculate expiration if specified
    expires_at = None
    if expires_in_days:
        expires_at = datetime.utcnow() + timedelta(days=expires_in_days)
    
    # Create API key
    api_key = APIKey(
        key=key,
        name=name,
        email=email,
        company=company,
        rate_limit=rate_limit,
        expires_at=expires_at
    )
    
    db.add(api_key)
    db.commit()
    db.refresh(api_key)
    
    return api_key


def get_api_key_by_key(db: Session, key: str) -> Optional[APIKey]:
    """
    Get API key by key string
    
    Args:
        db: Database session
        key: API key string
    
    Returns:
        APIKey object or None
    """
    return db.query(APIKey).filter(APIKey.key == key).first()


def get_api_key_by_id(db: Session, key_id: int) -> Optional[APIKey]:
    """
    Get API key by ID
    
    Args:
        db: Database session
        key_id: API key ID
    
    Returns:
        APIKey object or None
    """
    return db.query(APIKey).filter(APIKey.id == key_id).first()


def get_api_keys_by_email(db: Session, email: str) -> List[APIKey]:
    """
    Get all API keys for an email
    
    Args:
        db: Database session
        email: User email
    
    Returns:
        List of APIKey objects
    """
    return db.query(APIKey).filter(APIKey.email == email).all()


def get_all_api_keys(db: Session, skip: int = 0, limit: int = 100) -> List[APIKey]:
    """
    Get all API keys with pagination
    
    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum number of records to return
    
    Returns:
        List of APIKey objects
    """
    return db.query(APIKey).offset(skip).limit(limit).all()


def validate_api_key(db: Session, key: str) -> tuple[bool, Optional[str], Optional[APIKey]]:
    """
    Validate an API key
    
    Args:
        db: Database session
        key: API key string
    
    Returns:
        Tuple of (is_valid, error_message, api_key_object)
    """
    api_key = get_api_key_by_key(db, key)
    
    if not api_key:
        return False, "Invalid API key", None
    
    if not api_key.is_active:
        return False, "API key is inactive", None
    
    if api_key.expires_at and api_key.expires_at < datetime.utcnow():
        return False, "API key has expired", None
    
    # Check rate limit (simple daily check)
    if api_key.last_used_at:
        # Reset counter if it's a new day
        if api_key.last_used_at.date() < datetime.utcnow().date():
            api_key.usage_count = 0
    
    if api_key.usage_count >= api_key.rate_limit:
        return False, f"Rate limit exceeded ({api_key.rate_limit} requests per day)", None
    
    return True, None, api_key


def increment_api_key_usage(db: Session, api_key: APIKey):
    """
    Increment usage count and update last used timestamp
    
    Args:
        db: Database session
        api_key: APIKey object
    """
    api_key.usage_count += 1
    api_key.last_used_at = datetime.utcnow()
    db.commit()


def update_api_key(db: Session, key_id: int, **kwargs) -> Optional[APIKey]:
    """
    Update API key properties
    
    Args:
        db: Database session
        key_id: API key ID
        **kwargs: Fields to update
    
    Returns:
        Updated APIKey object or None
    """
    api_key = get_api_key_by_id(db, key_id)
    
    if not api_key:
        return None
    
    # Update allowed fields
    allowed_fields = ['name', 'is_active', 'rate_limit', 'expires_at']
    for field, value in kwargs.items():
        if field in allowed_fields and hasattr(api_key, field):
            setattr(api_key, field, value)
    
    db.commit()
    db.refresh(api_key)
    
    return api_key


def deactivate_api_key(db: Session, key_id: int) -> bool:
    """
    Deactivate an API key
    
    Args:
        db: Database session
        key_id: API key ID
    
    Returns:
        True if successful, False otherwise
    """
    api_key = get_api_key_by_id(db, key_id)
    
    if not api_key:
        return False
    
    api_key.is_active = 0
    db.commit()
    
    return True


def delete_api_key(db: Session, key_id: int) -> bool:
    """
    Delete an API key
    
    Args:
        db: Database session
        key_id: API key ID
    
    Returns:
        True if successful, False otherwise
    """
    api_key = get_api_key_by_id(db, key_id)
    
    if not api_key:
        return False
    
    db.delete(api_key)
    db.commit()
    
    return True


def get_api_key_stats(db: Session, key_id: int) -> Optional[dict]:
    """
    Get usage statistics for an API key
    
    Args:
        db: Database session
        key_id: API key ID
    
    Returns:
        Dictionary with stats or None
    """
    api_key = get_api_key_by_id(db, key_id)
    
    if not api_key:
        return None
    
    return {
        "id": api_key.id,
        "name": api_key.name,
        "email": api_key.email,
        "total_requests": api_key.usage_count,
        "rate_limit": api_key.rate_limit,
        "remaining_requests": max(0, api_key.rate_limit - api_key.usage_count),
        "last_used": api_key.last_used_at.isoformat() if api_key.last_used_at else None,
        "created_at": api_key.created_at.isoformat() if api_key.created_at else None,
        "is_active": bool(api_key.is_active),
        "expires_at": api_key.expires_at.isoformat() if api_key.expires_at else None
    }
