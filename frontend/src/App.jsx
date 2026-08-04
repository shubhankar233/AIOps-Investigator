import { useState } from "react";
import "./App.css";

const API_URL =
  "https://jjrslzffp7.execute-api.us-east-1.amazonaws.com/Prod/api/v1";

function App() {
  const [logs, setLogs] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const investigate = async () => {
    setError("");
    setResult(null);

    const logLines = logs
      .split("\n")
      .map((line) => line.trim())
      .filter(Boolean);

    if (logLines.length === 0) {
      setError("Please enter at least one log line.");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch(`${API_URL}/analyze`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          logs: logLines,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.message || "Investigation failed.");
      }

      setResult(data);
    } catch (err) {
      setError(err.message || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="header">
        <div>
          <h1>AIOps Investigator</h1>
          <p>AI-powered cloud incident investigation</p>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          Backend Online
        </div>
      </header>

      <main className="container">
        <section className="investigation-panel">
          <div className="section-header">
            <div>
              <h2>Investigate Incident</h2>
              <p>
                Paste application or cloud logs below and let the investigation
                engine analyze the incident.
              </p>
            </div>
          </div>

          <textarea
            value={logs}
            onChange={(event) => setLogs(event.target.value)}
            placeholder={`Example:
Lambda timeout after 30 seconds
Database connection refused
API Gateway returned 502`}
          />

          {error && <div className="error">{error}</div>}

          <button
            className="investigate-button"
            onClick={investigate}
            disabled={loading}
          >
            {loading ? "Investigating..." : "Investigate Incident"}
          </button>
        </section>

        {result && (
          <section className="results">
            <div className="result-header">
              <div>
                <p className="eyebrow">INVESTIGATION RESULT</p>
                <h2>{result.incident_id}</h2>
              </div>

              <span
                className={`severity ${result.severity?.toLowerCase()}`}
              >
                {result.severity}
              </span>
            </div>

            <div className="summary-grid">
              <div className="card">
                <span className="label">Summary</span>
                <strong>{result.summary}</strong>
              </div>

              <div className="card">
                <span className="label">Similar Incidents</span>
                <strong>{result.similar_incidents_found}</strong>
              </div>

              <div className="card">
                <span className="label">Confidence</span>
                <strong>
                  {result.ai_result?.confidence || "N/A"}
                </strong>
              </div>
            </div>

            <div className="card">
              <span className="label">Detected Root Causes</span>

              <div className="tags">
                {result.root_cause?.map((cause) => (
                  <span className="tag" key={cause}>
                    {cause}
                  </span>
                ))}
              </div>
            </div>

            <div className="card">
              <span className="label">Probable Root Cause</span>
              <h3>
                {result.ai_result?.probable_root_cause ||
                  "Unable to determine"}
              </h3>
            </div>

            <div className="card">
              <span className="label">AI Reasoning</span>
              <p className="reasoning">
                {result.ai_result?.reasoning ||
                  "No reasoning available."}
              </p>
            </div>

            <div className="card">
              <span className="label">Recommended Remediation</span>

              <ol className="remediation">
                {result.ai_result?.remediation_steps?.map(
                  (step, index) => (
                    <li key={index}>{step}</li>
                  )
                )}
              </ol>
            </div>
          </section>
        )}
      </main>
    </div>
  );
}

export default App;