import { useState } from "react";

const API = "http://127.0.0.1:8000";

export default function App() {
  const [text, setText] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState("");

const summarize = async () => {
  if (!text.trim()) {
    alert("Please paste a long paragraph 😊");
    return;
  }

  setLoading(true);
  setStatus("AI is analyzing your text… 🤖");
  setSummary("");

  try {
    const res = await fetch(`${API}/summarize`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    if (!res.ok) {
      throw new Error("Backend failed");
    }

    const data = await res.json();

    setSummary(data.summary);
    setStatus("Summary ready ✨");
  } catch (err) {
    setStatus(
      "Text was too long or server had an issue. Please try again after a few seconds."
    );
  }

  setLoading(false);
};

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-100 to-purple-100 flex items-center justify-center px-4">
      <div className="bg-white w-full max-w-4xl rounded-2xl shadow-xl p-8 space-y-6">

        <h1 className="text-3xl font-bold text-center">
          🤖 AI Text Summarizer
        </h1>

        <textarea
          rows={8}
          className="w-full border rounded-xl p-4 focus:ring-2 focus:ring-indigo-400"
          placeholder="Paste a long article or paragraph here..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />

        <div className="flex justify-center">
          <button
            onClick={summarize}
            disabled={loading}
            className={`px-8 py-3 rounded-xl text-white transition
              ${loading
                ? "bg-gray-400 cursor-not-allowed"
                : "bg-indigo-600 hover:bg-indigo-700"}`}
          >
            {loading ? "Summarizing…" : "Summarize"}
          </button>
        </div>

        {status && (
          <p className="text-center text-sm text-gray-500">
            {status}
          </p>
        )}

        {summary && (
          <div className="bg-indigo-50 p-5 rounded-xl">
            <h2 className="font-semibold mb-2">✨ Summary</h2>
            <p className="leading-relaxed">{summary}</p>
          </div>
        )}

      </div>
    </div>
  );
}
