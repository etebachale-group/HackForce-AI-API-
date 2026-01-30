import { useState, useEffect } from 'react';
import { bugAPI, statsAPI } from './services/api';
import './App.css';

// Font Awesome icons via CDN (added in index.html)
function App() {
  // State
  const [bugs, setBugs] = useState([]);
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [creating, setCreating] = useState(false);
  
  // Filters
  const [filterSeverity, setFilterSeverity] = useState('');
  const [filterStatus, setFilterStatus] = useState('');
  
  // Form
  const [formData, setFormData] = useState({
    title: '',
    description: '',
  });

  // Load data on mount and when filters change
  useEffect(() => {
    loadData();
  }, [filterSeverity, filterStatus]);

  // Load bugs and stats
  const loadData = async () => {
    try {
      setLoading(true);
      setError(null);
      
      // Build filter params
      const params = {};
      if (filterSeverity) params.severity = filterSeverity;
      if (filterStatus) params.status = filterStatus;
      
      // Fetch data
      const [bugsResponse, statsResponse] = await Promise.all([
        bugAPI.getAll(params),
        statsAPI.get()
      ]);
      
      setBugs(bugsResponse.data);
      setStats(statsResponse.data);
    } catch (err) {
      console.error('Error loading data:', err);
      setError(err.response?.data?.detail || 'Failed to load data. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  // Handle form input change
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  // Handle form submit
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!formData.title || !formData.description) {
      alert('Please fill in all fields');
      return;
    }
    
    try {
      setCreating(true);
      setError(null);
      
      await bugAPI.create({
        title: formData.title,
        description: formData.description,
        source: 'Dashboard'
      });
      
      // Reset form
      setFormData({ title: '', description: '' });
      
      // Reload data
      await loadData();
      
      alert('✅ Bug created successfully with AI classification!');
    } catch (err) {
      console.error('Error creating bug:', err);
      setError(err.response?.data?.detail || 'Failed to create bug. Please try again.');
    } finally {
      setCreating(false);
    }
  };

  // Handle bug deletion
  const handleDelete = async (id) => {
    if (!confirm('Are you sure you want to delete this bug?')) {
      return;
    }
    
    try {
      await bugAPI.delete(id);
      await loadData();
      alert('Bug deleted successfully');
    } catch (err) {
      console.error('Error deleting bug:', err);
      alert('Failed to delete bug');
    }
  };

  // Get severity color
  const getSeverityColor = (severity) => {
    const colors = {
      'Critical': '#dc2626',
      'High': '#ea580c',
      'Medium': '#f59e0b',
      'Low': '#10b981'
    };
    return colors[severity] || '#6b7280';
  };

  // Get status color
  const getStatusColor = (status) => {
    const colors = {
      'Open': '#3b82f6',
      'In Progress': '#f59e0b',
      'Resolved': '#10b981',
      'Closed': '#6b7280'
    };
    return colors[status] || '#6b7280';
  };

  // Loading state
  if (loading && bugs.length === 0) {
    return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
        <p>Loading HackForce AI...</p>
      </div>
    );
  }

  return (
    <div className="app">
      {/* Header */}
      <header className="header">
        <div className="header-content">
          <h1><i className="fas fa-robot"></i> HackForce AI</h1>
          <p>AI-Powered Bug Classification & Developer Assignment</p>
        </div>
      </header>

      {/* Error Banner */}
      {error && (
        <div className="error-banner">
          <span><i className="fas fa-exclamation-triangle"></i> {error}</span>
          <button onClick={() => setError(null)}><i className="fas fa-times"></i></button>
        </div>
      )}

      {/* Stats Cards */}
      <div className="stats-grid">
        <div className="stat-card">
          <div className="stat-icon"><i className="fas fa-chart-bar"></i></div>
          <div className="stat-content">
            <h3>Total Bugs</h3>
            <p className="stat-value">{stats?.total_bugs || 0}</p>
          </div>
        </div>
        
        <div className="stat-card critical">
          <div className="stat-icon"><i className="fas fa-exclamation-circle"></i></div>
          <div className="stat-content">
            <h3>Critical</h3>
            <p className="stat-value">{stats?.by_severity?.Critical || 0}</p>
          </div>
        </div>
        
        <div className="stat-card high">
          <div className="stat-icon"><i className="fas fa-fire"></i></div>
          <div className="stat-content">
            <h3>High</h3>
            <p className="stat-value">{stats?.by_severity?.High || 0}</p>
          </div>
        </div>
        
        <div className="stat-card medium">
          <div className="stat-icon"><i className="fas fa-exclamation"></i></div>
          <div className="stat-content">
            <h3>Medium</h3>
            <p className="stat-value">{stats?.by_severity?.Medium || 0}</p>
          </div>
        </div>
        
        <div className="stat-card low">
          <div className="stat-icon"><i className="fas fa-check-circle"></i></div>
          <div className="stat-content">
            <h3>Low</h3>
            <p className="stat-value">{stats?.by_severity?.Low || 0}</p>
          </div>
        </div>
      </div>

      <div className="main-content">
        {/* Create Bug Form */}
        <div className="card">
          <h2><i className="fas fa-bug"></i> Report New Bug</h2>
          <form onSubmit={handleSubmit} className="bug-form">
            <div className="form-group">
              <label htmlFor="title">Bug Title *</label>
              <input
                type="text"
                id="title"
                name="title"
                value={formData.title}
                onChange={handleInputChange}
                placeholder="Brief description of the bug"
                required
                minLength="5"
                disabled={creating}
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="description">Description *</label>
              <textarea
                id="description"
                name="description"
                value={formData.description}
                onChange={handleInputChange}
                placeholder="Detailed description: steps to reproduce, expected vs actual behavior..."
                rows="5"
                required
                minLength="10"
                disabled={creating}
              />
            </div>
            
            <button 
              type="submit" 
              className="btn btn-primary"
              disabled={creating}
            >
              {creating ? (
                <><i className="fas fa-spinner fa-spin"></i> AI is analyzing...</>
              ) : (
                <><i className="fas fa-rocket"></i> Submit Bug Report</>
              )}
            </button>
            
            <p className="form-hint">
              <i className="fas fa-lightbulb"></i> Our AI will automatically classify severity and assign a developer
            </p>
          </form>
        </div>

        {/* Bug List */}
        <div className="card">
          <div className="card-header">
            <h2><i className="fas fa-list"></i> Bug Reports</h2>
            <div className="filters">
              <select 
                value={filterSeverity} 
                onChange={(e) => setFilterSeverity(e.target.value)}
                className="filter-select"
              >
                <option value="">All Severities</option>
                <option value="Critical">Critical</option>
                <option value="High">High</option>
                <option value="Medium">Medium</option>
                <option value="Low">Low</option>
              </select>
              
              <select 
                value={filterStatus} 
                onChange={(e) => setFilterStatus(e.target.value)}
                className="filter-select"
              >
                <option value="">All Statuses</option>
                <option value="Open">Open</option>
                <option value="In Progress">In Progress</option>
                <option value="Resolved">Resolved</option>
                <option value="Closed">Closed</option>
              </select>
              
              <button onClick={loadData} className="btn btn-secondary">
                <i className="fas fa-sync-alt"></i> Refresh
              </button>
            </div>
          </div>

          {bugs.length === 0 ? (
            <div className="empty-state">
              <p><i className="fas fa-inbox"></i></p>
              <p className="empty-hint">No bugs found. Create your first bug report above!</p>
            </div>
          ) : (
            <div className="bug-list">
              {bugs.map(bug => (
                <div key={bug.id} className="bug-item">
                  <div className="bug-header">
                    <div className="bug-title-row">
                      <h3>{bug.title}</h3>
                      <span 
                        className="badge severity-badge"
                        style={{ backgroundColor: getSeverityColor(bug.severity) }}
                      >
                        {bug.severity}
                      </span>
                    </div>
                    <span 
                      className="badge status-badge"
                      style={{ backgroundColor: getStatusColor(bug.status) }}
                    >
                      {bug.status}
                    </span>
                  </div>
                  
                  <p className="bug-description">{bug.description}</p>
                  
                  <div className="bug-meta">
                    <span className="meta-item">
                      <strong><i className="fas fa-hashtag"></i> ID:</strong> {bug.id}
                    </span>
                    {bug.assigned_developer && (
                      <span className="meta-item">
                        <strong><i className="fas fa-user"></i> Assigned:</strong> {bug.assigned_developer}
                      </span>
                    )}
                    {bug.confidence_score && (
                      <span className="meta-item">
                        <strong><i className="fas fa-bullseye"></i> AI Confidence:</strong> {(bug.confidence_score * 100).toFixed(0)}%
                      </span>
                    )}
                    <span className="meta-item">
                      <strong><i className="fas fa-map-marker-alt"></i> Source:</strong> {bug.source}
                    </span>
                  </div>
                  
                  <div className="bug-actions">
                    <button 
                      onClick={() => handleDelete(bug.id)}
                      className="btn btn-danger btn-sm"
                    >
                      <i className="fas fa-trash"></i> Delete
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* Footer */}
      <footer className="footer">
        <p>
          Powered by <strong>Groq AI</strong> (Mixtral-8x7b) | 
          <a href="/docs" target="_blank"><i className="fas fa-book"></i> API Docs</a> | 
          <a href="https://github.com/etebachale-group/HackForce-AI-API-" target="_blank"><i className="fab fa-github"></i> GitHub</a>
        </p>
      </footer>
    </div>
  );
}

export default App;
