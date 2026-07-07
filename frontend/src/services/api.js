import axios from "axios";

const api = axios.create({
  baseURL: "https://deepfake-text-detection-dba-net.onrender.com",
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;