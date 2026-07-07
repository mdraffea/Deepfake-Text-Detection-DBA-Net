import Navbar from "./components/Navbar";
import Detector from "./components/Detector";
import StatsCards from "./components/StatsCards";
import Architecture from "./components/Architecture";
import Footer from "./components/Footer";

export default function App() {
  return (
    <>
      <Navbar />
      <Detector />
      <StatsCards />
      <Architecture />
      <Footer />
    </>
  );
}