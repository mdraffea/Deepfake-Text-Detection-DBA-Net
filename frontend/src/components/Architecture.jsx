import {
  FileText,
  Eraser,
  Database,
  ScanSearch,
  BrainCircuit,
  GitMerge,
  BadgeCheck,
  ArrowRight,
} from "lucide-react";

const pipeline = [
  {
    icon: FileText,
    title: "Input Text",
    subtitle: "User Input",
    color: "text-cyan-400",
    bg: "bg-cyan-500/10",
  },
  {
    icon: Eraser,
    title: "Preprocessing",
    subtitle: "Cleaning & Tokenization",
    color: "text-green-400",
    bg: "bg-green-500/10",
  },
  {
    icon: Database,
    title: "FastText",
    subtitle: "Word Embeddings",
    color: "text-orange-400",
    bg: "bg-orange-500/10",
  },
  {
    icon: ScanSearch,
    title: "CNN",
    subtitle: "Feature Extraction",
    color: "text-violet-400",
    bg: "bg-violet-500/10",
  },
  {
    icon: BrainCircuit,
    title: "BiLSTM + Attention",
    subtitle: "Context Learning",
    color: "text-pink-400",
    bg: "bg-pink-500/10",
  },
  {
    icon: GitMerge,
    title: "Feature Fusion",
    subtitle: "DBA Fusion",
    color: "text-yellow-400",
    bg: "bg-yellow-500/10",
  },
  {
    icon: BadgeCheck,
    title: "Prediction",
    subtitle: "AI / Human",
    color: "text-emerald-400",
    bg: "bg-emerald-500/10",
  },
];

export default function Architecture() {
  return (
    <section
      id="architecture"
      className="max-w-7xl mx-auto px-8 py-24"
    >
      <div className="text-center">

        <h2 className="text-4xl font-bold">
          DBA-Net Architecture
        </h2>

        <p className="text-slate-400 mt-4 max-w-3xl mx-auto">
          The prediction pipeline combines FastText embeddings,
          CNN feature extraction, BiLSTM contextual learning,
          Multi-Head Attention, and feature fusion for accurate
          deepfake text detection.
        </p>

      </div>

      <div className="mt-20 flex flex-wrap justify-center items-center gap-5">

        {pipeline.map((step, index) => {

          const Icon = step.icon;

          return (
            <div
              key={index}
              className="flex items-center"
            >
              <div className="w-52 rounded-3xl border border-slate-800 bg-slate-900/60 backdrop-blur-xl p-6 hover:border-cyan-500 transition-all duration-300 hover:-translate-y-2">

                <div
                  className={`w-14 h-14 rounded-2xl ${step.bg} flex items-center justify-center`}
                >
                  <Icon
                    size={28}
                    className={step.color}
                  />
                </div>

                <h3 className="mt-6 text-lg font-bold">
                  {step.title}
                </h3>

                <p className="mt-2 text-sm text-slate-400">
                  {step.subtitle}
                </p>

              </div>

              {index < pipeline.length - 1 && (
                <ArrowRight
                  size={28}
                  className="mx-4 text-slate-600 hidden lg:block"
                />
              )}
            </div>
          );
        })}

      </div>

      <div className="mt-20 rounded-3xl border border-cyan-500/20 bg-cyan-500/5 p-8">

        <h3 className="text-2xl font-bold mb-5">
          Why DBA-Net?
        </h3>

        <div className="grid md:grid-cols-2 gap-8 text-slate-300">

          <ul className="space-y-3 list-disc list-inside">

            <li>FastText captures semantic word relationships.</li>

            <li>CNN extracts local textual patterns.</li>

            <li>BiLSTM learns long-range context.</li>

            <li>Multi-Head Attention highlights important tokens.</li>

          </ul>

          <ul className="space-y-3 list-disc list-inside">

            <li>Feature Fusion improves representation quality.</li>

            <li>Balanced dataset of 49,990 samples.</li>

            <li>92.36% Test Accuracy.</li>

            <li>Designed specifically for AI-generated text detection.</li>

          </ul>

        </div>

      </div>

    </section>
  );
}