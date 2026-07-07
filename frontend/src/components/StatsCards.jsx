import {
  Database,
  Target,
  BrainCircuit,
  Activity,
} from "lucide-react";

const stats = [
  {
    icon: <Target size={30} />,
    title: "Accuracy",
    value: "92.36%",
    color: "text-cyan-400",
    bg: "bg-cyan-500/10",
  },
  {
    icon: <Database size={30} />,
    title: "Dataset",
    value: "49,990",
    color: "text-green-400",
    bg: "bg-green-500/10",
  },
  {
    icon: <BrainCircuit size={30} />,
    title: "Architecture",
    value: "DBA-Net",
    color: "text-violet-400",
    bg: "bg-violet-500/10",
  },
  {
    icon: <Activity size={30} />,
    title: "F1 Score",
    value: "92.63%",
    color: "text-orange-400",
    bg: "bg-orange-500/10",
  },
];

export default function StatsCards() {
  return (
    <section
      id="performance"
      className="max-w-7xl mx-auto px-8 py-20"
    >
      <div className="text-center mb-14">

        <h2 className="text-4xl font-bold">
          Model Performance
        </h2>

        <p className="text-slate-400 mt-4 max-w-2xl mx-auto">
          DBA-Net was trained on a balanced dataset of 49,990 samples
          and evaluated using Accuracy, Precision, Recall and F1 Score.
        </p>

      </div>

      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">

        {stats.map((item, index) => (

          <div
            key={index}
            className="rounded-3xl border border-slate-800 bg-slate-900/60 backdrop-blur-xl p-8 transition-all duration-300 hover:-translate-y-2 hover:border-cyan-500 hover:shadow-2xl hover:shadow-cyan-500/10"
          >

            <div
              className={`w-14 h-14 rounded-2xl ${item.bg} flex items-center justify-center ${item.color}`}
            >
              {item.icon}
            </div>

            <h3 className="mt-6 text-slate-400 text-lg">
              {item.title}
            </h3>

            <h2 className={`mt-2 text-4xl font-bold ${item.color}`}>
              {item.value}
            </h2>

          </div>

        ))}

      </div>

      <div className="mt-14 rounded-3xl border border-slate-800 bg-slate-900/60 backdrop-blur-xl p-8">

        <h3 className="text-2xl font-bold mb-6">
          Evaluation Metrics
        </h3>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">

          <div>
            <p className="text-slate-400">Precision</p>
            <h2 className="text-3xl font-bold text-cyan-400 mt-2">
              89.45%
            </h2>
          </div>

          <div>
            <p className="text-slate-400">Recall</p>
            <h2 className="text-3xl font-bold text-green-400 mt-2">
              96.04%
            </h2>
          </div>

          <div>
            <p className="text-slate-400">Validation</p>
            <h2 className="text-3xl font-bold text-violet-400 mt-2">
              92.68%
            </h2>
          </div>

          <div>
            <p className="text-slate-400">Test</p>
            <h2 className="text-3xl font-bold text-orange-400 mt-2">
              92.36%
            </h2>
          </div>

        </div>

      </div>

    </section>
  );
}