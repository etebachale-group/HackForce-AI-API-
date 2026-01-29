import { useState, useEffect } from 'react';
import { api } from './services/api';
import './App.css';

function App() {
  const [bugs, setBugs] = useState([]);
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filterSeverity, setFilterSeverity] = useState('');
  const [filterStatus, setFilterStatus] = useState('');

  useEffect(() => {
    loadData();
  }, [filterSeverity, filterStatus]);

  const loadData = async () => {
    try {
      setLoading(true);
      setError(null);
      
      const filters = {};
      if (filterSeverity) filters.severity = filterSeverity;
      if (filterStatus) filters.status = filterStatus;
      
      const [bugsRes, statsRes] = await Promise.all([
        api.getBugs(filters),
        api.getStats()
      ]);
      
      setBugs(bugsRes.data);
      setStats(statsRes.data);
    } catch (err) {
      console.error('Error loading data:', err);
      setError('Failed to load data. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleCreateBug = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    
    try {
      await api.createBug({
        title: formData.get('title'),
        description: formData.get('description'),
        source: 'Manual'
      });
      
      loadData();
      e.target.reset();
      alert('Bug created successfully!');
    } catch (err) {
      console.error('Error creating bug:', err);
      alert('Failed to create bug. Please try again.');
    }
  };

  const getSeverityColor = (severity) => {
    const colors = {
      'Critical': '#7c3aed',
      'High': '#ef4444',
      'Medium': '#f59e0b',
      'Low': '#10b981'
    };
    return colors[severity] || '#6b7280';
  };

  if (loading && bugs.length === 0) {
    return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
        <p>Loading...</p>
      </div>
    );
  }

  return (
    <div className="App">
      <header className="app-header">
        <h1>🐛 AI Bug Classification Dashboard</h1>
        <p>Automated bug classification and developer assignment</p>
      </header>

      {error && (
        <div className="error-banner">
          {error}
        </div>
      )}

      {/* Statistics Cards */}
      <div className="stats-container">
        <div className="stat-card">
          <h3>Total Bugs</h3>
          <p className="stat-number">{stats?.total_bugs || 0}</p>
        </div>
        <div className="stat-card critical">
          <h3>Critical</h3>
          <p className="stat-number">{stats?.by_severity?.Critical || 0}</p>
        </div>
        <div className="stat-card high">
          <h3>High</h3>
          <p className="stat-number">{stats?.by_severity?.High || 0}</p>
        </div>
        <div className="stat-card medium">
          <h3>Medium</h3>
          <p className="stat-number">{stats?.by_severity?.Medium || 0}</p>
        </div>
        <div className="stat-card low">
          <h3>Low</h3>
          <p className="stat-number">{stats?.by_severity?.Low || 0}</p>
        </div>
      </div>

      <div className="content-container">
        {/* Create Bug Form */}
        <div className="create-bug-section">
          <h2>Report New Bug</h2>
          <form onSubmit={handleCreateBug} className="bug-form">
            <div className="form-group">
              <label htmlFor="title">Bug Title *</label>
              <input
                type="text"
                id="title"
                name="title"
                placeholder="Brief description of the bug"
                required
                minLength="5"
              />
            </div>
            <div className="form-group">
              <label htmlFor="description">Description *</label>
              <textarea
                id="description"
                name="description"
                placeholder="Detailed description of the bug, steps to reproduce, expected vs actual behavior..."
                rows="6"
                required
                minLength="10"
              />
            </div>
            <button type="submit" className="submit-button">
              Submit Bug Report
            </button>
          </form>
        </div>

        {/* Bug List */}
        <div className="bug-list-section">
          <div className="bug-list-header">
            <h2>Bug Reports</h2>
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
            </div>
          </div>

          {bugs.length === 0 ? (
            <div className="empty-state">
              <p>No bugs found. Create your first bug report!</p>
            </div>
          ) : (
            <div className="bug-list">
              {bugs.map(bug => (
                <div 
                  key={bug.id} 
                  className="bug-card"
                  style={{ borderLeftColor: getSeverityColor(bug.severity) }}
                >
                  <div className="bug-header">
                    <h3>{bug.title}</h3>
                    <span 
                      className="severity-badge"
                      style={{ backgroundColor: getSeverityColor(bug.severity) }}
                    >
                      {bug.severity}
                    </span>
                  </div>
                  <p className="bug-description">{bug.description}</p>
                  <div className="bug-meta">
                    <span className="meta-item">
                      <strong>ID:</strong> {bug.id}
                    </span>
                    <span className="meta-item">
                      <strong>Status:</strong> {bug.status}
                    </span>
                    <span className="meta-item">
                      <strong>Source:</strong> {bug.source}
                    </span>
                    {bug.assigned_developer && (
                      <span className="meta-item">
                        <strong>Assigned:</strong> {bug.assigned_developer}
                      </span>
                    )}
                    {bug.confidence_score && (
                      <span className="meta-item">
                        <strong>Confidence:</strong> {(bug.confidence_score * 100).toFixed(0)}%
                      </span>
                    )}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
