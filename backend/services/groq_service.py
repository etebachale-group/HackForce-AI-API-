"""
Groq AI Service for Bug Classification
Uses Groq's LLM API to intelligently classify bug severity
"""

import os
import json
from typing import Dict, Optional

# Try to import Groq, but don't fail if it's not available
try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False
    print("⚠️  Groq package not available. Using fallback mode.")

class GroqService:
    """
    Service for AI-powered bug classification using Groq
    """
    
    def __init__(self):
        """Initialize Groq client"""
        if not GROQ_AVAILABLE:
            print("⚠️  Groq not installed. Using fallback classification.")
            self.client = None
            return
            
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            print("⚠️  Warning: GROQ_API_KEY not found. Using fallback classification.")
            self.client = None
        else:
            try:
                self.client = Groq(api_key=api_key)
                print("✅ Groq client initialized successfully")
            except Exception as e:
                print(f"⚠️  Failed to initialize Groq client: {e}")
                self.client = None
        
        # Use Mixtral model (fast and accurate)
        self.model = "mixtral-8x7b-32768"
    
    def classify_bug_severity(self, title: str, description: str) -> Dict[str, any]:
        """
        Classify bug severity using Groq AI
        
        Args:
            title: Bug title
            description: Bug description
            
        Returns:
            Dict with severity, confidence, and reasoning
        """
        if not self.client:
            return self._fallback_classification(title, description)
        
        try:
            # Create prompt for Groq
            prompt = self._create_classification_prompt(title, description)
            
            # Call Groq API
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert software bug triaging system. Analyze bugs and classify their severity accurately."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=self.model,
                temperature=0.3,  # Lower temperature for more consistent results
                max_tokens=500,
                response_format={"type": "json_object"}  # Request JSON response
            )
            
            # Parse response
            result_text = response.choices[0].message.content
            result = json.loads(result_text)
            
            # Validate and normalize result
            return self._normalize_result(result)
            
        except Exception as e:
            print(f"❌ Groq API error: {e}")
            return self._fallback_classification(title, description)
    
    def suggest_developer(self, bug_description: str, severity: str, developers: list) -> Dict[str, any]:
        """
        Suggest best developer for the bug using AI
        
        Args:
            bug_description: Full bug description
            severity: Bug severity level
            developers: List of available developers with skills
            
        Returns:
            Dict with suggested developer and reasoning
        """
        if not self.client or not developers:
            return self._fallback_developer_suggestion(developers)
        
        try:
            prompt = self._create_developer_prompt(bug_description, severity, developers)
            
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert at matching bugs to developers based on their skills and workload."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=self.model,
                temperature=0.3,
                max_tokens=300,
                response_format={"type": "json_object"}
            )
            
            result_text = response.choices[0].message.content
            result = json.loads(result_text)
            
            return result
            
        except Exception as e:
            print(f"❌ Groq API error in developer suggestion: {e}")
            return self._fallback_developer_suggestion(developers)
    
    def _create_classification_prompt(self, title: str, description: str) -> str:
        """Create prompt for bug classification"""
        return f"""Analyze this bug report and classify its severity.

Bug Title: {title}

Bug Description: {description}

Consider these factors:
1. Impact on users (how many users affected?)
2. System stability (does it crash the system?)
3. Security implications (is there a security risk?)
4. Data integrity (can it cause data loss?)
5. Urgency (how quickly must it be fixed?)

Severity Levels:
- Critical: System crashes, security vulnerabilities, data loss, affects all users
- High: Major functionality broken, affects many users, no workaround
- Medium: Functionality impaired, affects some users, workaround exists
- Low: Minor issues, cosmetic problems, affects few users

Respond in JSON format:
{{
    "severity": "Critical|High|Medium|Low",
    "confidence": 0.0-1.0,
    "reasoning": "brief explanation of why this severity was chosen",
    "impact_areas": ["list", "of", "affected", "areas"]
}}"""
    
    def _create_developer_prompt(self, bug_description: str, severity: str, developers: list) -> str:
        """Create prompt for developer suggestion"""
        dev_list = "\n".join([
            f"- {dev['name']}: Skills: {', '.join(dev.get('skills', []))}, Current workload: {dev.get('workload', 0)} bugs"
            for dev in developers
        ])
        
        return f"""Given this bug and list of developers, suggest the best developer to assign.

Bug Description: {bug_description}
Severity: {severity}

Available Developers:
{dev_list}

Consider:
1. Developer skills matching the bug type
2. Current workload (prefer less busy developers)
3. Severity (critical bugs need experienced developers)

Respond in JSON format:
{{
    "developer_name": "name of suggested developer",
    "confidence": 0.0-1.0,
    "reasoning": "why this developer is the best match"
}}"""
    
    def _normalize_result(self, result: Dict) -> Dict[str, any]:
        """Normalize and validate AI result"""
        severity = result.get("severity", "Medium")
        
        # Ensure severity is valid
        valid_severities = ["Critical", "High", "Medium", "Low"]
        if severity not in valid_severities:
            severity = "Medium"
        
        # Ensure confidence is between 0 and 1
        confidence = float(result.get("confidence", 0.7))
        confidence = max(0.0, min(1.0, confidence))
        
        return {
            "severity": severity,
            "confidence": confidence,
            "reasoning": result.get("reasoning", "AI classification"),
            "impact_areas": result.get("impact_areas", [])
        }
    
    def _fallback_classification(self, title: str, description: str) -> Dict[str, any]:
        """
        Simple rule-based classification when Groq is unavailable
        """
        text = f"{title} {description}".lower()
        
        # Critical keywords
        critical_keywords = [
            "crash", "security", "data loss", "critical", "urgent",
            "vulnerability", "exploit", "breach", "sql injection",
            "authentication bypass", "production down"
        ]
        
        # High severity keywords
        high_keywords = [
            "error", "bug", "broken", "not working", "fails", "failure",
            "cannot", "unable", "doesn't work", "500 error", "timeout",
            "database", "api down", "login failed"
        ]
        
        # Low severity keywords
        low_keywords = [
            "typo", "cosmetic", "minor", "suggestion", "improvement",
            "enhancement", "ui", "text", "color", "spacing", "alignment"
        ]
        
        # Check for keywords
        if any(keyword in text for keyword in critical_keywords):
            return {
                "severity": "Critical",
                "confidence": 0.75,
                "reasoning": "Keyword-based classification (fallback mode)",
                "impact_areas": ["system"]
            }
        elif any(keyword in text for keyword in high_keywords):
            return {
                "severity": "High",
                "confidence": 0.70,
                "reasoning": "Keyword-based classification (fallback mode)",
                "impact_areas": ["functionality"]
            }
        elif any(keyword in text for keyword in low_keywords):
            return {
                "severity": "Low",
                "confidence": 0.65,
                "reasoning": "Keyword-based classification (fallback mode)",
                "impact_areas": ["ui"]
            }
        else:
            return {
                "severity": "Medium",
                "confidence": 0.60,
                "reasoning": "Default classification (fallback mode)",
                "impact_areas": ["general"]
            }
    
    def _fallback_developer_suggestion(self, developers: list) -> Dict[str, any]:
        """Fallback developer suggestion based on workload"""
        if not developers:
            return {
                "developer_name": "Unassigned",
                "confidence": 0.0,
                "reasoning": "No developers available"
            }
        
        # Find developer with lowest workload
        best_dev = min(developers, key=lambda d: d.get('workload', 0))
        
        return {
            "developer_name": best_dev['name'],
            "confidence": 0.5,
            "reasoning": f"Assigned to developer with lowest workload ({best_dev.get('workload', 0)} bugs)"
        }


# Singleton instance - will be created on first use to avoid import-time errors
groq_service = None

def get_groq_service():
    """Get or create the Groq service singleton (lazy initialization)"""
    global groq_service
    if groq_service is None:
        groq_service = GroqService()
    return groq_service
