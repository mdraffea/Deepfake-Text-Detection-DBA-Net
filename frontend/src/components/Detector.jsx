import { useState } from "react";
import { WandSparkles } from "lucide-react";
import ResultCard from "./ResultCard";
import api from "../services/api";
import TextToolbar from "./TextToolbar";

export default function Detector() {
  const [text, setText] = useState("");

  const [prediction, setPrediction] = useState("Waiting...");
  const [confidence, setConfidence] = useState(0);
  const [loading, setLoading] = useState(false);
  const [processingTime, setProcessingTime] = useState("-- ms");

  const words =
    text.trim() === ""
      ? 0
      : text.trim().split(/\s+/).length;

  const characters = text.length;

  const reading = Math.max(
    1,
    Math.ceil(words / 200)
  );

  const analyzeText = async () => {
    if (!text.trim()) {
      alert("Please enter some text.");
      return;
    }

    try {
      setLoading(true);

      const start = performance.now();

      const response = await api.post("/predict", {
        text: text,
      });

      const end = performance.now();

      setPrediction(response.data.prediction);
      setConfidence(response.data.confidence);
      setProcessingTime(`${Math.round(end - start)} ms`);
    } catch (error) {
      console.error(error);
      alert("Cannot connect to FastAPI backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="max-w-7xl mx-auto px-8 py-16">

      <div className="grid lg:grid-cols-3 gap-8">

        {/* LEFT PANEL */}

        <div className="lg:col-span-2 rounded-3xl border border-slate-800 bg-slate-900/60 backdrop-blur-xl p-8">

          <h2 className="text-4xl font-bold">
            Detect AI Generated Text
          </h2>

          <p className="text-slate-400 mt-3">
            Paste any paragraph below and let DBA-Net analyze it.
          </p>

          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Paste text here..."
            className="mt-8 w-full h-80 rounded-2xl bg-slate-950 border border-slate-700 p-6 text-lg resize-none outline-none focus:border-blue-500 transition"
          />

          <TextToolbar
    setText={setText}
    setPrediction={setPrediction}
    setConfidence={setConfidence}
    setProcessingTime={setProcessingTime}
/>

          <div className="grid grid-cols-3 gap-4 mt-6">

            <div className="rounded-xl bg-slate-800 p-4">
              <p className="text-slate-400 text-sm">
                Words
              </p>

              <h3 className="text-2xl font-bold">
                {words}
              </h3>
            </div>

            <div className="rounded-xl bg-slate-800 p-4">
              <p className="text-slate-400 text-sm">
                Characters
              </p>

              <h3 className="text-2xl font-bold">
                {characters}
              </h3>
            </div>

            <div className="rounded-xl bg-slate-800 p-4">
              <p className="text-slate-400 text-sm">
                Reading Time
              </p>

              <h3 className="text-2xl font-bold">
                {reading} min
              </h3>
            </div>

          </div>

          <button
            onClick={analyzeText}
            disabled={loading}
            className="mt-8 w-full h-16 rounded-2xl bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 transition-all duration-300 font-bold text-lg flex items-center justify-center gap-3 disabled:opacity-60"
          >
            {loading ? (
              <>
                Analyzing...
              </>
            ) : (
              <>
                <WandSparkles size={22} />
                Analyze with DBA-Net
              </>
            )}
          </button>

        </div>

        {/* RIGHT PANEL */}

        <ResultCard
          prediction={prediction}
          confidence={confidence}
          processingTime={processingTime}
          loading={loading}
        />

      </div>

    </section>
  );
}