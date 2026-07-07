import {
  BrainCircuit,
  Cpu,
  GaugeCircle,
  CheckCircle2,
  AlertTriangle,
} from "lucide-react";

export default function ResultCard({
  prediction = "Waiting...",
  confidence = 0,
  processingTime = "-- ms",
  loading = false,
}) {
  const percentage = Number(confidence) || 0;

  const isAI = prediction === "AI Generated";

  const badgeColor = isAI
    ? "from-red-500 to-pink-500"
    : "from-green-500 to-emerald-500";

  return (
    <div className="rounded-3xl border border-slate-800 bg-slate-900/60 backdrop-blur-xl p-8 h-full shadow-xl">

      {/* Heading */}

      <h2 className="text-2xl font-bold mb-8">
        Detection Result
      </h2>

      {/* Prediction */}

      <div className="mb-8">

        <p className="text-slate-400 mb-3">
          Prediction
        </p>

        <div
          className={`inline-flex items-center gap-3 px-5 py-3 rounded-full bg-gradient-to-r ${badgeColor} text-white font-semibold shadow-lg`}
        >
          {isAI ? (
            <AlertTriangle size={20} />
          ) : (
            <CheckCircle2 size={20} />
          )}

          {loading ? "Analyzing..." : prediction}
        </div>

      </div>

      {/* Confidence */}

      <div>

        <div className="flex justify-between items-center mb-3">

          <span className="text-slate-400">
            Confidence
          </span>

          <span className="text-xl font-bold">
            {percentage.toFixed(2)}%
          </span>

        </div>

        <div className="w-full h-4 rounded-full bg-slate-800 overflow-hidden">

          <div
            className={`h-full rounded-full bg-gradient-to-r ${badgeColor} transition-all duration-700`}
            style={{
              width: `${percentage}%`,
            }}
          />

        </div>

      </div>

      {/* Information */}

      <div className="space-y-6 mt-10">

        <div className="flex justify-between items-center">

          <div className="flex items-center gap-2">

            <Cpu size={18} />

            <span className="text-slate-400">
              Model
            </span>

          </div>

          <span className="font-medium">
            DBA-Net
          </span>

        </div>

        <div className="flex justify-between items-center">

          <div className="flex items-center gap-2">

            <GaugeCircle size={18} />

            <span className="text-slate-400">
              Processing
            </span>

          </div>

          <span className="font-medium">
            {processingTime}
          </span>

        </div>

        <div className="flex justify-between items-center">

          <div className="flex items-center gap-2">

            <BrainCircuit size={18} />

            <span className="text-slate-400">
              Dataset
            </span>

          </div>

          <span className="font-medium">
            49,990 Samples
          </span>

        </div>

        <div className="flex justify-between items-center">

          <span className="text-slate-400">
            Test Accuracy
          </span>

          <span className="font-bold text-cyan-400">
            92.36%
          </span>

        </div>

        <div className="flex justify-between items-center">

          <span className="text-slate-400">
            Precision
          </span>

          <span>
            89.45%
          </span>

        </div>

        <div className="flex justify-between items-center">

          <span className="text-slate-400">
            Recall
          </span>

          <span>
            96.04%
          </span>

        </div>

        <div className="flex justify-between items-center">

          <span className="text-slate-400">
            F1 Score
          </span>

          <span>
            92.63%
          </span>

        </div>

      </div>

    </div>
  );
}