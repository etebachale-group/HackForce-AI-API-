# 🤖 Groq AI Integration

## Overview

HackForce AI now uses Groq's Mixtral-8x7b model for intelligent bug classification and developer assignment.

## Features

### 1. Bug Severity Classification
- **Model:** Mixtral-8x7b-32768
- **Input:** Bug title + description
- **Output:** Severity (Critical/High/Medium/Low), confidence score, reasoning
- **Fallback:** Rule-based classification if API unavailable

### 2. Developer Assignment
- **Model:** Mixtral-8x7b-32768
- **Input:** Bug description, severity, available developers with skills
- **Output:** Best developer match, confidence, reasoning
- **Fallback:** Assigns to developer with lowest workload

## Implementation

### Service Layer
```python
from services.groq_service import groq_service

# Classify bug severity
result = groq_service.classify_bug_severity(
    title="Bug title",
    description="Bug description"
)
# Returns: {severity, confidence, reasoning, impact_areas}

# Suggest developer
suggestion = groq_service.suggest_developer(
    bug_description="Full bug description",
    severity="High",
    developers=[{name, skills, workload}, ...]
)
# Returns: {developer_name, confidence, reasoning}
```

### API Endpoints Using Groq

#### POST /api/bugs
Creates a new bug with AI classification and developer assignment.

**Request:**
```json
{
  "title": "Database connection timeout",
  "description": "Users cannot login, database connection times out after 30s",
  "source": "User Report"
}
```

**Response:**
```json
{
  "id": 1,
  "title": "Database connection timeout",
  "severity": "Critical",
  "predicted_severity": "Critical",
  "confidence_score": 0.92,
  "assigned_developer": "Alice Johnson",
  "status": "Open",
  "created_at": "2026-01-30T10:00:00"
}
```

#### POST /api/predict
Predicts severity without saving to database.

**Request:**
```json
{
  "title": "UI button misaligned",
  "description": "Submit button is 2px off center"
}
```

**Response:**
```json
{
  "severity": "Low",
  "confidence": 0.78,
  "suggested_developer": "Bob Smith",
  "reasoning": "Minor UI issue with low user impact"
}
```

## Configuration

### Environment Variables
```bash
GROQ_API_KEY=gsk_your_api_key_here
```

### Dependencies
```txt
groq==0.11.0
```

## Testing

### Local Testing
```bash
cd backend
pip install groq
python test_groq.py
```

### Expected Output
```
🧪 Testing Groq AI Bug Classification

Test 1: Critical: Database connection failing
------------------------------------------------------------
Severity: Critical
Confidence: 0.95
Reasoning: Production database outage affecting all users
Impact Areas: system, database

✅ All tests completed successfully!
```

## Error Handling

### Fallback Mode
If Groq API is unavailable or API key is missing:
- Uses rule-based keyword matching
- Returns lower confidence scores (0.60-0.75)
- Logs warning message
- Continues to function normally

### API Errors
- Network timeouts: Falls back to rule-based
- Invalid API key: Falls back to rule-based
- Rate limits: Falls back to rule-based
- All errors logged for debugging

## Performance

- **Average Response Time:** 1-2 seconds
- **Model:** Mixtral-8x7b (fast inference)
- **Temperature:** 0.3 (consistent results)
- **Max Tokens:** 500 (classification), 300 (developer suggestion)

## Monitoring

### Prediction Logs
All AI predictions are logged in the `prediction_logs` table:
```sql
SELECT * FROM prediction_logs 
WHERE model_version = 'groq-mixtral-8x7b'
ORDER BY created_at DESC;
```

### Success Rate
```sql
SELECT 
  COUNT(*) as total_predictions,
  AVG(confidence) as avg_confidence
FROM prediction_logs
WHERE model_version = 'groq-mixtral-8x7b';
```

## Future Enhancements

- [ ] Fine-tune model on historical bug data
- [ ] Add multi-language support
- [ ] Implement A/B testing with different models
- [ ] Add caching for similar bug descriptions
- [ ] Track prediction accuracy over time
