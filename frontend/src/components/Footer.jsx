import {
  Mail,
  Heart,
  BrainCircuit,
} from "lucide-react";

import {
  FaGithub,
  FaLinkedin,
} from "react-icons/fa";

export default function Footer() {
  return (
    <footer className="mt-24 border-t border-slate-800 bg-slate-950">

      <div className="max-w-7xl mx-auto px-8 py-16">

        <div className="grid md:grid-cols-3 gap-12">

          {/* Brand */}

          <div>

            <div className="flex items-center gap-3">

              <BrainCircuit
                className="text-cyan-400"
                size={34}
              />

              <h2 className="text-3xl font-bold">
                DBA-Net
              </h2>

            </div>

            <p className="mt-5 text-slate-400 leading-8">

              Deepfake Text Detection using
              FastText, CNN, BiLSTM and
              Multi-Head Attention.

            </p>

          </div>

          {/* Technologies */}

          <div>

            <h3 className="text-xl font-bold mb-5">
              Technologies
            </h3>

            <div className="space-y-3 text-slate-400">

              <p>⚛ React</p>
              <p>🚀 FastAPI</p>
              <p>🔥 PyTorch</p>
              <p>🧠 DBA-Net</p>
              <p>📊 FastText</p>

            </div>

          </div>

          {/* Contact */}

          <div>

            <h3 className="text-xl font-bold mb-5">
              Connect
            </h3>

            <div className="space-y-4">

              <a
                href="https://github.com/mdraffea"
                target="_blank"
                rel="noreferrer"
                className="flex items-center gap-3 hover:text-cyan-400 transition"
              >
                <FaGithub size={20} />

                GitHub

              </a>

              <a
                href="https://linkedin.com"
                target="_blank"
                rel="noreferrer"
                className="flex items-center gap-3 hover:text-cyan-400 transition"
              >
                <FaLinkedin size={20} />

                LinkedIn

              </a>

              <a
                href="mailto:raffeachisti88@gmail.com"
                className="flex items-center gap-3 hover:text-cyan-400 transition"
              >
                <Mail size={20} />

                Email

              </a>

            </div>

          </div>

        </div>

        <div className="mt-14 border-t border-slate-800 pt-8 flex justify-between flex-wrap">

          <p className="text-slate-500">
            © 2026 Mohd Raffea Chisti
          </p>

          <p className="flex items-center gap-2 text-slate-500">

            Built with

            <Heart
              size={16}
              className="text-red-500 fill-red-500"
            />

            React & FastAPI

          </p>

        </div>

      </div>

    </footer>
  );
}