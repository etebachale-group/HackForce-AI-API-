"""
API Key management endpoints
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session
from typing import Optional, List
from database import get_db
import crud_api_keys
# from models import APIKey  # Temporarily disabled - enable after creating api_keys table

# Placeholder - will be enabled when APIKey model is uncommented
APIKey = None

router = APIRouter(prefix="/api/keys", tags=["API Keys"])


# Pydantic models
class APIKeyCreate(BaseModel):
    """Model for creating an API key"""
    name: str = Field(..., min_length=3, max_length=100, description="Friendly name for the API key")
    email: EmailStr = Field(..., description="Your email address")
    company: Optional[str] = Field(None, max_length=100, description="Company name (optional)")
    rate_limit: int = Field(1000, ge=100, le=10000, description="Requests per day limit")
    expires_in_days: Optional[int] = Field(None, ge=1, le=365, description="Expiration in days (optional)")

class APIKeyResponse(BaseModel):
    """Model for API key response"""
    id: int
    name: str
    email: str
    company: Optional[str]
    key: Optional[str] = None  # Only shown on creation
    key_preview: Optional[str] = None
    is_active: bool
    usage_count: int
    rate_limit: int
    created_at: str
    last_used_at: Optional[str]
    expires_at: Optional[str]

    class Config:
        from_attributes = True

class APIKeyUpdate(BaseModel):
    """Model for updating an API key"""
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    is_active: Optional[bool] = None
    rate_limit: Optional[int] = Field(None, ge=100, le=10000)


# Endpoints
@router.post("/", response_model=APIKeyResponse, status_code=201)
async def create_api_key(
    key_data: APIKeyCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new API key
    
    **Important:** The full API key is only shown once during creation.
    Save it securely - you won't be able to see it again!
    
    **Rate Limits:**
    - Default: 1000 requests per day
    - Maximum: 10000 requests per day
    
    **Usage:**
    Include the API key in your requests using the `X-API-Key` header:
    ```
    curl -H "X-API-Key: your_api_key_here" https://api.example.com/endpoint
    ```
    """
    try:
        # Create API key
        api_key = crud_api_keys.create_api_key(
            db=db,
            name=key_data.name,
            email=key_data.email,
            company=key_data.company,
            rate_limit=key_data.rate_limit,
            expires_in_days=key_data.expires_in_days
        )
        
        # Return with full key (only time it's shown)
        return api_key.to_dict(include_key=True)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating API key: {str(e)}")


@router.get("/my-keys", response_model=List[APIKeyResponse])
async def get_my_api_keys(
    email: EmailStr,
    db: Session = Depends(get_db)
):
    """
    Get all API keys for a specific email
    
    **Note:** Full API keys are never shown after creation.
    Only the last 8 characters are displayed for security.
    """
    api_keys = crud_api_keys.get_api_keys_by_email(db, email)
    return [key.to_dict(include_key=False) for key in api_keys]


@router.get("/{key_id}", response_model=APIKeyResponse)
async def get_api_key(
    key_id: int,
    db: Session = Depends(get_db)
):
    """
    Get details of a specific API key by ID
    """
    api_key = crud_api_keys.get_api_key_by_id(db, key_id)
    
    if not api_key:
        raise HTTPException(status_code=404, detail="API key not found")
    
    return api_key.to_dict(include_key=False)


@router.get("/{key_id}/stats")
async def get_api_key_stats(
    key_id: int,
    db: Session = Depends(get_db)
):
    """
    Get usage statistics for an API key
    
    Returns:
    - Total requests made
    - Remaining requests for today
    - Last used timestamp
    - Rate limit information
    """
    stats = crud_api_keys.get_api_key_stats(db, key_id)
    
    if not stats:
        raise HTTPException(status_code=404, detail="API key not found")
    
    return stats


@router.put("/{key_id}", response_model=APIKeyResponse)
async def update_api_key(
    key_id: int,
    key_update: APIKeyUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an API key
    
    You can update:
    - Name (friendly name)
    - Active status (enable/disable)
    - Rate limit
    """
    # Prepare update data
    update_data = {k: v for k, v in key_update.dict().items() if v is not None}
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    # Convert is_active boolean to integer for database
    if 'is_active' in update_data:
        update_data['is_active'] = 1 if update_data['is_active'] else 0
    
    api_key = crud_api_keys.update_api_key(db, key_id, **update_data)
    
    if not api_key:
        raise HTTPException(status_code=404, detail="API key not found")
    
    return api_key.to_dict(include_key=False)


@router.post("/{key_id}/deactivate")
async def deactivate_api_key(
    key_id: int,
    db: Session = Depends(get_db)
):
    """
    Deactivate an API key
    
    The key will no longer work for authentication but remains in the database.
    You can reactivate it later using the update endpoint.
    """
    success = crud_api_keys.deactivate_api_key(db, key_id)
    
    if not success:
        raise HTTPException(status_code=404, detail="API key not found")
    
    return {"message": "API key deactivated successfully", "key_id": key_id}


@router.delete("/{key_id}")
async def delete_api_key(
    key_id: int,
    db: Session = Depends(get_db)
):
    """
    Permanently delete an API key
    
    **Warning:** This action cannot be undone!
    The key will be permanently removed from the database.
    """
    success = crud_api_keys.delete_api_key(db, key_id)
    
    if not success:
        raise HTTPException(status_code=404, detail="API key not found")
    
    return {"message": "API key deleted successfully", "key_id": key_id}


@router.post("/validate")
async def validate_api_key(
    api_key: str,
    db: Session = Depends(get_db)
):
    """
    Validate an API key without incrementing usage
    
    Useful for testing if a key is valid before making actual API calls.
    """
    is_valid, error_message, key_obj = crud_api_keys.validate_api_key(db, api_key)
    
    if not is_valid:
        return {
            "valid": False,
            "error": error_message
        }
    
    return {
        "valid": True,
        "key_id": key_obj.id,
        "name": key_obj.name,
        "email": key_obj.email,
        "rate_limit": key_obj.rate_limit,
        "usage_count": key_obj.usage_count,
        "remaining_requests": max(0, key_obj.rate_limit - key_obj.usage_count)
    }
