import { CSRF_TOKEN } from "./csrf_token.js";

import axios from "axios";

const API_URL = "http://127.0.0.1:8000/";

const axiosInstance = axios.create({
  baseURL: API_URL,
  headers: {
    "content-type": "application/json",
    "X-CSRFTOKEN": CSRF_TOKEN
  }
});

export default axiosInstance;
