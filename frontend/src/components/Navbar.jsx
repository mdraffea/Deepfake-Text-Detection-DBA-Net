import { BrainCircuit } from "lucide-react";
import { FaGithub } from "react-icons/fa";

export default function Navbar() {
  return (
    <nav className="sticky top-0 z-50 backdrop-blur-xl bg-slate-950/70 border-b border-slate-800">

      <div className="max-w-7xl mx-auto h-20 px-8 flex items-center justify-between">

        <div className="flex items-center gap-4">

          <div className="w-12 h-12 rounded-2xl bg-gradient-to-r from-cyan-500 to-blue-600 flex items-center justify-center shadow-lg">

            <BrainCircuit className="text-white" />

          </div>

          <div>

            <h1 className="font-bold text-2xl">
              DBA-Net
            </h1>

            <p className="text-xs text-slate-400">
              Deepfake Text Detection
            </p>

          </div>

        </div>

        <div className="flex items-center gap-8">

          <a
            href="#"
            className="hover:text-cyan-400 transition"
          >
            Home
          </a>

          <a
            href="#architecture"
            className="hover:text-cyan-400 transition"
          >
            Architecture
          </a>

          <a
            href="#performance"
            className="hover:text-cyan-400 transition"
          >
            Performance
          </a>

          <a
            href="https://github.com/mdraffea"
            target="_blank"
            rel="noreferrer"
            className="hover:text-cyan-400 transition"
          >
            <FaGithub size={22}/>
          </a>

        </div>

      </div>

    </nav>
  );
}