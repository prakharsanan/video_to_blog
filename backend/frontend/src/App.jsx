import { useState } from "react";

import api from "./services/api";

import Navbar from "./components/Navbar";
import VideoInput from "./components/VideoInput";
import Progress from "./components/Progress";
import HeroImage from "./components/HeroImage";
import BlogViewer from "./components/BlogViewer";
import ImageGallery from "./components/ImageGallery";
import DownloadButton from "./components/DownloadButton";

import "./App.css";

function App() {
    const [url, setUrl] = useState("");

    const [currentStep, setCurrentStep] = useState(-1);

    const [blog, setBlog] = useState(null);

    const [images, setImages] = useState(null);

    async function generateBlog() {

        if (!url.trim()) {
            alert("Please enter a YouTube URL.");
            return;
        }

        try {

            // Reset previous output
            setBlog(null);
            setImages(null);

            // Demo progress animation
            setCurrentStep(0);
            await new Promise(resolve => setTimeout(resolve, 500));

            setCurrentStep(1);
            await new Promise(resolve => setTimeout(resolve, 500));

            setCurrentStep(2);
            await new Promise(resolve => setTimeout(resolve, 500));

            setCurrentStep(3);

            // Backend call
            const response = await api.post("/generate", {
                url,
            });

            setCurrentStep(4);

            // Save backend response
            setBlog(response.data.blog);
            setImages(response.data.images);

            await new Promise(resolve => setTimeout(resolve, 500));

            // Hide progress
            setCurrentStep(5);

        } catch (err) {

            console.error(err);

            alert("Failed to generate blog. Please try again.");

            setCurrentStep(-1);

        }
    }

    return (
        <div className="app">

            <Navbar />

            <VideoInput
                url={url}
                setUrl={setUrl}
                onGenerate={generateBlog}
            />

            <Progress currentStep={currentStep} />

            <HeroImage images={images} />

            <BlogViewer blog={blog} />

            <ImageGallery images={images} />

            <DownloadButton blog={blog} />

        </div>
    );
}

export default App;