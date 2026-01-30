-- API Keys Table Schema
-- Run this in your Supabase SQL Editor to create the api_keys table

CREATE TABLE IF NOT EXISTS api_keys (
    id SERIAL PRIMARY KEY,
    key VARCHAR(64) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    company VARCHAR(100),
    is_active INTEGER DEFAULT 1,  -- 1 = active, 0 = inactive
    usage_count INTEGER DEFAULT 0,
    rate_limit INTEGER DEFAULT 1000,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_used_at TIMESTAMP WITH TIME ZONE,
    expires_at TIMESTAMP WITH TIME ZONE
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_api_keys_key ON api_keys(key);
CREATE INDEX IF NOT EXISTS idx_api_keys_email ON api_keys(email);
CREATE INDEX IF NOT EXISTS idx_api_keys_is_active ON api_keys(is_active);

-- Add comments
COMMENT ON TABLE api_keys IS 'Stores API keys for external developers';
COMMENT ON COLUMN api_keys.key IS 'Unique API key string (hf_...)';
COMMENT ON COLUMN api_keys.name IS 'Friendly name for the API key';
COMMENT ON COLUMN api_keys.email IS 'Email of the key owner';
COMMENT ON COLUMN api_keys.company IS 'Optional company name';
COMMENT ON COLUMN api_keys.is_active IS '1 = active, 0 = inactive';
COMMENT ON COLUMN api_keys.usage_count IS 'Number of API requests made';
COMMENT ON COLUMN api_keys.rate_limit IS 'Maximum requests per day';
COMMENT ON COLUMN api_keys.last_used_at IS 'Last time the key was used';
COMMENT ON COLUMN api_keys.expires_at IS 'Optional expiration date';

-- Sample query to view all active keys
-- SELECT id, name, email, key, usage_count, rate_limit, created_at 
-- FROM api_keys 
-- WHERE is_active = 1 
-- ORDER BY created_at DESC;
