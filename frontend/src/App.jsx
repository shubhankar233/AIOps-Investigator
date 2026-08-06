import { useEffect, useState } from "react";
import "./App.css";

const API_URL =
  import.meta.env.VITE_API_URL;

const normalizeInvestigation = (payload) => {
  const item = payload?.data || payload;

  if (!item) {
    return null;
  }

  // Historical API response:
  // {
  //   incident_id,
  //   logs,
  //   analysis: {...}
  // }

  if (item.analysis) {
    return {
      ...item,
      ...item.analysis,
      received_logs:
        item.received_logs ??
        item.logs?.length ??
        0,
    };
  }

  // Current investigation response is already flattened
  return {
    ...item,
    received_logs:
      item.received_logs ??
      item.logs?.length ??
      0,
  };
};

function App() {
  const [logs, setLogs] = useState("");
  const [result, setResult] = useState(null);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [historyLoading, setHistoryLoading] = useState(false);
  const [error, setError] = useState("");

  const loadHistory = async () => {
    setHistoryLoading(true);

    try {
      const response = await fetch(
        `${API_URL}/investigations`
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.message ||
            "Failed to load investigation history."
        );
      }

      setHistory(data.data || data || []);
    } catch (err) {
      console.error(
        "History loading failed:",
        err
      );
    } finally {
      setHistoryLoading(false);
    }
  };

  useEffect(() => {
    loadHistory();
  }, []);

  const investigate = async () => {
    setError("");
    setResult(null);

    const logLines = logs
      .split("\n")
      .map((line) => line.trim())
      .filter(Boolean);

    if (logLines.length === 0) {
      setError(
        "Please enter at least one log line."
      );
      return;
    }

    setLoading(true);

    try {
      const response = await fetch(
        `${API_URL}/analyze`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            logs: logLines,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.message ||
            "Investigation failed."
        );
      }

      setResult(
        normalizeInvestigation(data)
      );

      await loadHistory();
    } catch (err) {
      setError(
        err.message ||
          "Something went wrong."
      );
    } finally {
      setLoading(false);
    }
  };

  const viewInvestigation = async (
    incidentId
  ) => {
    setError("");

    try {
      const response = await fetch(
        `${API_URL}/investigations/${incidentId}`
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.message ||
            "Failed to load investigation."
        );
      }

      setResult(
        normalizeInvestigation(data)
      );
    } catch (err) {
      setError(
        err.message ||
          "Failed to load investigation."
      );
    }
  };

  return (
    <div className="app">

      {/* ================================
          HEADER
      ================================= */}

      <header className="header">
        <div>
          <h1>AIOps Investigator</h1>

          <p>
            AI-powered cloud incident
            investigation
          </p>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          Backend Online
        </div>
      </header>

      <main className="container">

        {/* ================================
            INVESTIGATION INPUT
        ================================= */}

        <section className="investigation-panel">

          <div className="section-header">

            <div>
              <h2>
                Investigate Incident
              </h2>

              <p>
                Paste application or cloud
                logs below and let the
                investigation engine analyze
                the incident.
              </p>
            </div>

          </div>

          <textarea
            value={logs}
            onChange={(event) =>
              setLogs(event.target.value)
            }
            placeholder={`Example:
Lambda timeout after 30 seconds
Database connection refused
API Gateway returned 502`}
          />

          {error && (
            <div className="error">
              {error}
            </div>
          )}

          <button
            className="investigate-button"
            onClick={investigate}
            disabled={loading}
          >
            {loading
              ? "Investigating..."
              : "Investigate Incident"}
          </button>

        </section>

        {/* ================================
            INVESTIGATION RESULT
        ================================= */}

        {result && (
          <section className="results">

            <div className="result-header">

              <div>
                <p className="eyebrow">
                  INVESTIGATION RESULT
                </p>

                <h2>
                  {result.incident_id}
                </h2>
              </div>

              <span
                className={`severity ${
                  result.severity?.toLowerCase() ||
                  ""
                }`}
              >
                {result.severity ||
                  "UNKNOWN"}
              </span>

            </div>

            {/* Summary */}

            <div className="summary-grid">

                <div className="card">
                  <span className="label">
                    Summary
                  </span>

                  <strong>
                    {result.summary ||
                      "No summary available."}
                  </strong>
                </div>

                <div className="card">
                  <span className="label">
                    Incident Category
                  </span>

                  <strong>
                    {result.incident_category ||
                      "Unknown"}
                  </strong>
                </div>

                <div className="card">
                  <span className="label">
                    Similar Incidents
                  </span>

                  <strong>
                    {result.similar_incidents_found ??
                      0}
                  </strong>
                </div>

                <div className="card">
                  <span className="label">
                    AI Confidence
                  </span>

                  <strong>
                    {result.confidence ||
                      result.ai_result?.confidence ||
                      "N/A"}
                  </strong>
                </div>

              </div>

            {/* Log Processing */}

          <div className="card log-processing">

            <span className="label">
              Log Processing
            </span>

            <div className="log-processing-grid">

              <div>
                <span className="processing-label">
                  Total Logs
                </span>

                <strong>
                  {result.log_classification
                    ?.total_logs ?? 0}
                </strong>
              </div>

              <div>
                <span className="processing-label">
                  Important Logs
                </span>

                <strong>
                  {result.log_classification
                    ?.important_logs ?? 0}
                </strong>
              </div>

              <div>
                <span className="processing-label">
                  Ignored Logs
                </span>

                <strong>
                  {result.log_classification
                    ?.ignored_logs ?? 0}
                </strong>
              </div>

            </div>

          </div>

          {/* Log Classification */}

          <div className="card">

            <span className="label">
              Log Classification
            </span>

            <div className="classification-summary">

              <div>
                <strong>
                  {result.log_classification?.total_logs ?? 0}
                </strong>

                <span>
                  Total Logs
                </span>
              </div>

              <div>
                <strong>
                  {result.log_classification?.important_logs ?? 0}
                </strong>

                <span>
                  Important Logs
                </span>
              </div>

              <div>
                <strong>
                  {result.log_classification?.ignored_logs ?? 0}
                </strong>

                <span>
                  Ignored Logs
                </span>
              </div>

            </div>

            <div className="classified-logs">

              <div>
                <span className="label">
                  Important Logs
                </span>

                {result.important_logs?.length > 0 ? (

                  <ul>
                    {result.important_logs.map(
                      (log, index) => (
                        <li key={index}>
                          {log}
                        </li>
                      )
                    )}
                  </ul>

                ) : (
                  <p className="empty-state">
                    No important logs detected.
                  </p>
                )}

              </div>

              <div>
                <span className="label">
                  Ignored Logs
                </span>

                {result.ignored_logs?.length > 0 ? (

                  <ul>
                    {result.ignored_logs.map(
                      (log, index) => (
                        <li key={index}>
                          {log}
                        </li>
                      )
                    )}
                  </ul>

                ) : (
                  <p className="empty-state">
                    No ignored logs.
                  </p>
                )}

              </div>

            </div>

          </div>

            {/* Detected Issues */}

            <div className="card">

              <span className="label">
                Detected Issues
              </span>

              {result.root_cause?.length >
              0 ? (
                <div className="tags">

                  {result.root_cause.map(
                    (cause) => (
                      <span
                        className="tag"
                        key={cause}
                      >
                        {cause}
                      </span>
                    )
                  )}

                </div>
              ) : (
                <p>
                  No known issues detected.
                </p>
              )}

            </div>

            {/* Issue Analysis */}

            <div className="card">

              <span className="label">
                Issue Analysis
              </span>

              {result.ai_result?.issue_analysis?.length > 0 ? (

                <div className="issue-analysis">

                  {result.ai_result.issue_analysis.map(
                    (item, index) => (

                      <div
                        className="issue-analysis-item"
                        key={`${item.issue}-${index}`}
                      >

                        <div className="issue-analysis-header">

                          <strong>
                            {item.issue}
                          </strong>

                          <span
                            className={`issue-role ${item.role}`}
                          >
                            {item.role
                              ?.replaceAll("_", " ")
                              .toUpperCase()}
                          </span>

                        </div>

                        {item.evidence?.length > 0 && (

                          <div className="issue-evidence">

                            <span className="processing-label">
                              Evidence
                            </span>

                            <ul>
                              {item.evidence.map(
                                (evidence, evidenceIndex) => (
                                  <li key={evidenceIndex}>
                                    {evidence}
                                  </li>
                                )
                              )}
                            </ul>

                          </div>

                        )}

                      </div>

                    )
                  )}

                </div>

              ) : (

                <p className="empty-state">
                  No per-issue analysis available.
                </p>

              )}

            </div>

            {/* Evidence */}
            <div className="result-card">
              <div className="result-card-header">
                <h3>Evidence</h3>
              </div>

              {result.evidence && result.evidence.length > 0 ? (
                <ul className="evidence-list">
                  {result.evidence.map((item, index) => (
                    <li key={index}>
                      {item}
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="empty-state">
                  No evidence was returned by the AI investigation.
                </p>
              )}
            </div>

            {/* Probable Root Cause */}

            <div className="card">

              <span className="label">
                Probable Root Cause
              </span>

              <h3>
                {result.ai_result
                  ?.probable_root_cause ||
                  "AI analysis unavailable"}
              </h3>

            </div>

            {/* AI Reasoning */}

            <div className="card">

              <span className="label">
                AI Reasoning
              </span>

              <p className="reasoning">
                {result.ai_result
                  ?.reasoning ||
                  "No AI reasoning available."}
              </p>

            </div>

            {/* Remediation */}

            <div className="card">

              <span className="label">
                Recommended Remediation
              </span>

              {result.ai_result
                ?.remediation_steps
                ?.length > 0 ? (

                <ol className="remediation">

                  {result.ai_result.remediation_steps.map(
                    (step, index) => (
                      <li key={index}>
                        {step}
                      </li>
                    )
                  )}

                </ol>

              ) : (
                <p>
                  No remediation steps
                  available.
                </p>
              )}

            </div>

            {/* Metadata */}

            <div className="analysis-meta">

                <span>
                    <strong>Analysis mode:</strong>{" "}
                    {result.analysis_mode || "Unknown"}
                </span>

                <span>
                    <strong>Logs received:</strong>{" "}
                    {result.received_logs ?? "Unknown"}
                </span>

                <span>
                    <strong>Logs processed:</strong>{" "}
                    {result.processed_logs ?? "Unknown"}
                </span>

            </div>

            {/* ================================
                HISTORICAL CONTEXT
            ================================= */}

            <div className="card historical-context">

              <span className="label">
                Historical Context
              </span>

              <div className="historical-summary">

                <strong>
                  {result.similar_incidents_found ??
                    0}
                </strong>

                <span>
                  similar previous incidents
                  found
                </span>

              </div>

              {result.similar_incidents
                ?.length > 0 ? (

                <div className="similar-incidents">

                  {result.similar_incidents.map(
                    (incident) => (

                      <div
                        className="similar-incident"
                        key={
                          incident.incident_id
                        }
                      >

                        <div className="similar-incident-header">

                          <strong>
                            {incident.incident_id}
                          </strong>

                          <span
                            className={`severity ${
                              incident.severity?.toLowerCase() ||
                              ""
                            }`}
                          >
                            {incident.severity ||
                              "UNKNOWN"}
                          </span>

                        </div>

                        <p>
                          {incident.summary ||
                            "Previous investigation"}
                        </p>

                        <div className="similar-incident-details">

                            <span>
                              Similarity:{" "}
                              <strong>
                                {incident.similarity_score ?? 0}%
                              </strong>
                            </span>

                            <span>
                              Matching issues:{" "}
                              <strong>
                                {incident.matching_issues?.join(
                                  ", "
                                ) || "None"}
                              </strong>
                            </span>

                            <span>
                              Previous root cause:{" "}
                              <strong>
                                {incident.root_cause?.join(
                                  ", "
                                ) || "Unknown"}
                              </strong>
                            </span>

                          </div>

                      </div>

                    )
                  )}

                </div>

              ) : (

                <p className="empty-state">
                  No similar historical
                  incidents found.
                </p>

              )}

            </div>

          </section>
        )}

        {/* ================================
            INVESTIGATION HISTORY
        ================================= */}

        <section className="history">

          <div className="history-header">

            <div>
              <p className="eyebrow">
                HISTORY
              </p>

              <h2>
                Previous Investigations
              </h2>
            </div>

            <button
              className="refresh-button"
              onClick={loadHistory}
              disabled={historyLoading}
            >
              {historyLoading
                ? "Refreshing..."
                : "Refresh"}
            </button>

          </div>

          {historyLoading &&
          history.length === 0 ? (

            <p className="empty-state">
              Loading investigation
              history...
            </p>

          ) : history.length === 0 ? (

            <p className="empty-state">
              No previous investigations
              found.
            </p>

          ) : (

            <div className="history-list">

              {history.map((item) => {

                const analysis =
                  item.analysis || {};

                return (

                  <button
                    className="history-item"
                    key={
                      item.incident_id
                    }
                    onClick={() =>
                      viewInvestigation(
                        item.incident_id
                      )
                    }
                  >

                    <div>

                      <strong>
                        {item.incident_id}
                      </strong>

                      <span>
                        {analysis.summary ||
                          "Investigation completed"}
                      </span>
                      <small>
                          {item.created_at
                              ? new Date(item.created_at).toLocaleString()
                              : ""}
                      </small>

                    </div>

                    <div className="history-meta">

                      <span
                        className={`severity ${
                          analysis.severity?.toLowerCase() ||
                          ""
                        }`}
                      >
                        {analysis.severity ||
                          "UNKNOWN"}
                      </span>

                      <span>
                        {analysis.similar_incidents_found ??
                          0}{" "}
                        similar
                      </span>

                    </div>

                  </button>

                );
              })}

            </div>

          )}

        </section>

      </main>

    </div>
  );
}

export default App;