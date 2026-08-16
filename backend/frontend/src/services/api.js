import axios from "axios";

const api = axios.create({
    baseURL: "https://video-to-blog-md7i.onrender.com",
    headers: {
        "Content-Type": "application/json",
    },
});

export default api;