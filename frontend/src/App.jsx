import { useState, useEffect } from 'react';
import './App.css';

function App() {
  // State variables for form inputs and database itineraries
  const [destination, setDestination] = useState('');
  const [days, setDays] = useState('');
  const [itineraries, setItineraries] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  /**
   * Fetches all registered itineraries from the FastAPI backend.
   */
  const fetchItineraries = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/v1/travel/');
      if (!response.ok) {
        throw new Error('Failed to fetch itineraries');
      }
      const data = await response.json();
      setItineraries(data.data || []);
    } catch (err) {
      console.error(err);
      setError('Could not connect to the backend server. Please verify it is running.');
    }
  };

  // Fetch itineraries on component mount
  useEffect(() => {
    fetchItineraries();
  }, []);

  /**
   * Handles submission of the itinerary form.
   * Sends the destination and number of days to the backend database.
   * @param {Event} e The form submission event
   */
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!destination || !days) return;

    setLoading(true);
    setError(null);

    try {
      const response = await fetch('http://localhost:8000/api/v1/travel/itinerary', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          destination: destination,
          days: parseInt(days, 10),
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to save itinerary');
      }

      // Reset form fields
      setDestination('');
      setDays('');
      
      // Refresh list from database
      await fetchItineraries();
    } catch (err) {
      console.error(err);
      setError('Failed to submit itinerary. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <header className="header">
        <h1>AI Travel Agent</h1>
        <p className="subtitle">Plan your next adventure and save to PostgreSQL</p>
      </header>

      <main className="main-content">
        <section className="form-section">
          <h2>Create New Itinerary</h2>
          <form onSubmit={handleSubmit} className="itinerary-form">
            <div className="form-group">
              <label htmlFor="destination">Destination</label>
              <input
                id="destination"
                type="text"
                value={destination}
                onChange={(e) => setDestination(e.target.value)}
                placeholder="e.g., Paris, Tokyo, Bali"
                required
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="days">Duration (Days)</label>
              <input
                id="days"
                type="number"
                min="1"
                value={days}
                onChange={(e) => setDays(e.target.value)}
                placeholder="e.g., 5"
                required
              />
            </div>

            <button type="submit" disabled={loading} className="submit-btn">
              {loading ? 'Saving...' : 'Add Itinerary'}
            </button>
          </form>

          {error && <p className="error-message">{error}</p>}
        </section>

        <section className="list-section">
          <h2>Saved Adventures</h2>
          {itineraries.length === 0 ? (
            <p className="no-data">No itineraries saved yet. Add one above!</p>
          ) : (
            <div className="itinerary-grid">
              {itineraries.map((item) => (
                <div key={item.id} className="itinerary-card">
                  <div className="card-badge">{item.days} {item.days === 1 ? 'Day' : 'Days'}</div>
                  <h3>{item.destination}</h3>
                  <p>Ready to explore {item.destination}!</p>
                </div>
              ))}
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;
