import { motion } from "framer-motion";
import { Brain, Sparkles, ArrowDown } from "lucide-react";

export default function Hero({ onStart }) {
  return (
    <section className="relative min-h-screen flex items-center justify-center px-6">

      <motion.div
        initial={{ opacity: 0, y: 60 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: .8 }}
        className="max-w-6xl mx-auto text-center"
      >

        <div className="inline-flex items-center gap-3 px-6 py-3 rounded-full bg-white/5 backdrop-blur-xl border border-cyan-500/30">

          <Sparkles className="w-5 h-5 text-cyan-400" />

          <span className="text-cyan-300">

            AI Powered Detection Platform

          </span>

        </div>

        <h1 className="mt-10 text-7xl md:text-8xl font-black leading-none">

          <span className="bg-gradient-to-r from-cyan-300 via-blue-400 to-purple-500 bg-clip-text text-transparent">

            DBA-Net

          </span>

        </h1>

        <h2 className="mt-8 text-3xl md:text-4xl font-semibold text-slate-200">

          Enterprise AI Deepfake Text Detection

        </h2>

        <p className="mt-8 max-w-3xl mx-auto text-lg leading-9 text-slate-400">

          Detect AI-generated and human-written content using
          a custom Dual Branch Attention Network combining
          FastText embeddings, CNN, BiLSTM, Multi-Head Attention,
          and Gated Feature Fusion.

        </p>

        <div className="mt-12 flex justify-center gap-5 flex-wrap">

          <button
            onClick={onStart}
            className="px-10 py-5 rounded-2xl bg-gradient-to-r from-cyan-500 to-blue-600 text-xl font-bold hover:scale-105 transition shadow-2xl shadow-cyan-500/30"
          >
            Start Detection
          </button>

          <button className="px-10 py-5 rounded-2xl border border-white/10 backdrop-blur-xl hover:bg-white/5 transition">

            Learn More

          </button>

        </div>

        <div className="mt-24 flex justify-center">

          <motion.div
            animate={{ y: [0,12,0] }}
            transition={{
              duration:2,
              repeat:Infinity
            }}
          >
            <ArrowDown
              className="w-10 h-10 text-cyan-400"
            />
          </motion.div>
        </div>

      </motion.div>

    </section>
  );
}