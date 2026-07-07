import { useRef } from "react";

import Hero from "../components/Hero";
import Detector from "../components/Detector";

export default function Home() {

  const detectorRef = useRef(null);

  const scrollToDetector = () => {

    detectorRef.current?.scrollIntoView({

      behavior: "smooth"

    });

  };

  return (
    <>

      <Hero onStart={scrollToDetector} />

      <div ref={detectorRef}>

        <Detector />

      </div>

    </>
  );
}