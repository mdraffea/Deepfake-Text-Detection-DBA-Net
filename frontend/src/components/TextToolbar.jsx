import {
  Clipboard,
  Eraser,
  FileText,
} from "lucide-react";

export default function TextToolbar({
  setText,
  setPrediction,
  setConfidence,
  setProcessingTime,
}) {
  const sampleText = `Artificial intelligence has transformed numerous industries by improving automation, decision-making, and predictive analytics. Researchers continue developing more efficient machine learning models capable of solving increasingly complex real-world problems.`;

  const handlePaste = async () => {
    try {
      const clip = await navigator.clipboard.readText();
      setText(clip);
    } catch {
      alert("Clipboard permission denied.");
    }
  };

  const handleClear = () => {
    setText("");
    setPrediction("Waiting...");
    setConfidence(0);
    setProcessingTime("-- ms");
  };

  return (
    <div className="flex flex-wrap gap-3 mt-5">

      <button
        onClick={() => setText(sampleText)}
        className="px-5 py-3 rounded-xl border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2"
      >
        <FileText size={18} />
        Sample
      </button>

      <button
        onClick={handlePaste}
        className="px-5 py-3 rounded-xl border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2"
      >
        <Clipboard size={18} />
        Paste
      </button>

      <button
        onClick={handleClear}
        className="px-5 py-3 rounded-xl border border-red-500 text-red-400 hover:bg-red-500/10 transition flex items-center gap-2"
      >
        <Eraser size={18} />
        Clear
      </button>

    </div>
  );
}