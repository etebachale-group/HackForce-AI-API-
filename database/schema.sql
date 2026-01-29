-- AI Bug Classification API - Database Schema
-- PostgreSQL Database Schema

-- Drop tables if they exist (for clean setup)
DROP TABLE IF EXISTS predictions_log CASCADE;
DROP TABLE IF EXISTS bugs CASCADE;
DROP TABLE IF EXISTS developers CASCADE;

-- ============================================================================
-- Developers Table
-- ============================================================================
CREATE TABLE developers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    skills TEXT[],
    workload INT DEFAULT 0,
    status VARCHAR(20) DEFAULT 'Active' CHECK (status IN ('Active', 'Inactive', 'On Leave')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- Bugs Table
-- ============================================================================
CREATE TABLE bugs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    severity VARCHAR(20) NOT NULL CHECK (severity IN ('Low', 'Medium', 'High', 'Critical')),
    predicted_severity VARCHAR(20) CHECK (predicted_severity IN ('Low', 'Medium', 'High', 'Critical')),
    confidence_score FLOAT CHECK (confidence_score >= 0 AND confidence_score <= 1),
    status VARCHAR(20) DEFAULT 'Open' CHECK (status IN ('Open', 'In Progress', 'Resolved', 'Closed')),
    source VARCHAR(100) DEFAULT 'Manual',
    assigned_developer_id INT REFERENCES developers(id) ON DELETE SET NULL,
    assigned_developer VARCHAR(100),
    notion_page_id VARCHAR(100),
    jira_issue_key VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- Predictions Log Table
-- ============================================================================
CREATE TABLE predictions_log (
    id SERIAL PRIMARY KEY,
    bug_id INT REFERENCES bugs(id) ON DELETE CASCADE,
    model_version VARCHAR(50),
    predicted_severity VARCHAR(20) NOT NULL,
    confidence FLOAT NOT NULL,
    features_used TEXT,
    prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- Indexes for Performance
-- ============================================================================
CREATE INDEX idx_bugs_severity ON bugs(severity);
CREATE INDEX idx_bugs_status ON bugs(status);
CREATE INDEX idx_bugs_source ON bugs(source);
CREATE INDEX idx_bugs_created_at ON bugs(created_at DESC);
CREATE INDEX idx_bugs_assigned_developer ON bugs(assigned_developer_id);
CREATE INDEX idx_developers_email ON developers(email);
CREATE INDEX idx_predictions_bug_id ON predictions_log(bug_id);

-- ============================================================================
-- Triggers for Updated At
-- ============================================================================
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_bugs_updated_at BEFORE UPDATE ON bugs
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_developers_updated_at BEFORE UPDATE ON developers
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- Sample Data (Optional - for testing)
-- ============================================================================

-- Insert sample developers
INSERT INTO developers (name, email, skills, workload) VALUES
    ('John Doe', 'john.doe@example.com', ARRAY['Python', 'FastAPI', 'PostgreSQL'], 3),
    ('Jane Smith', 'jane.smith@example.com', ARRAY['React', 'JavaScript', 'CSS'], 2),
    ('Bob Johnson', 'bob.johnson@example.com', ARRAY['Python', 'Machine Learning', 'NLP'], 1),
    ('Alice Williams', 'alice.williams@example.com', ARRAY['DevOps', 'Docker', 'Kubernetes'], 2);

-- Insert sample bugs
INSERT INTO bugs (title, description, severity, predicted_severity, confidence_score, status, source, assigned_developer) VALUES
    ('Login button not responding', 'When users click the login button, nothing happens. Console shows no errors.', 'High', 'High', 0.85, 'Open', 'Manual', 'Jane Smith'),
    ('Database connection timeout', 'Application crashes when trying to connect to database after 30 seconds.', 'Critical', 'Critical', 0.92, 'In Progress', 'GitHub Issues', 'John Doe'),
    ('Typo in welcome message', 'The welcome message has a spelling error: "Wellcome" instead of "Welcome".', 'Low', 'Low', 0.78, 'Open', 'Manual', 'Jane Smith'),
    ('Slow API response time', 'API endpoints are taking 5+ seconds to respond during peak hours.', 'Medium', 'Medium', 0.73, 'Open', 'Groq', 'John Doe'),
    ('Security vulnerability in authentication', 'JWT tokens are not being validated properly, allowing unauthorized access.', 'Critical', 'Critical', 0.95, 'In Progress', 'Security Audit', 'Bob Johnson');

-- ============================================================================
-- Views for Analytics
-- ============================================================================

-- View: Bug statistics by severity
CREATE OR REPLACE VIEW bug_stats_by_severity AS
SELECT 
    severity,
    COUNT(*) as count,
    ROUND(AVG(confidence_score)::numeric, 2) as avg_confidence
FROM bugs
GROUP BY severity
ORDER BY 
    CASE severity
        WHEN 'Critical' THEN 1
        WHEN 'High' THEN 2
        WHEN 'Medium' THEN 3
        WHEN 'Low' THEN 4
    END;

-- View: Developer workload
CREATE OR REPLACE VIEW developer_workload AS
SELECT 
    d.id,
    d.name,
    d.email,
    COUNT(b.id) as assigned_bugs,
    COUNT(CASE WHEN b.status = 'Open' THEN 1 END) as open_bugs,
    COUNT(CASE WHEN b.status = 'In Progress' THEN 1 END) as in_progress_bugs,
    COUNT(CASE WHEN b.status = 'Resolved' THEN 1 END) as resolved_bugs
FROM developers d
LEFT JOIN bugs b ON d.id = b.assigned_developer_id
GROUP BY d.id, d.name, d.email
ORDER BY assigned_bugs DESC;

-- View: Recent bugs
CREATE OR REPLACE VIEW recent_bugs AS
SELECT 
    b.id,
    b.title,
    b.severity,
    b.status,
    b.source,
    b.assigned_developer,
    b.created_at
FROM bugs b
ORDER BY b.created_at DESC
LIMIT 50;

-- ============================================================================
-- Functions
-- ============================================================================

-- Function: Get bugs by severity
CREATE OR REPLACE FUNCTION get_bugs_by_severity(sev VARCHAR)
RETURNS TABLE (
    id INT,
    title VARCHAR,
    description TEXT,
    severity VARCHAR,
    status VARCHAR,
    created_at TIMESTAMP
) AS $$
BEGIN
    RETURN QUERY
    SELECT b.id, b.title, b.description, b.severity, b.status, b.created_at
    FROM bugs b
    WHERE b.severity = sev
    ORDER BY b.created_at DESC;
END;
$$ LANGUAGE plpgsql;

-- ============================================================================
-- Grants (adjust based on your user)
-- ============================================================================
-- GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO your_user;
-- GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO your_user;
