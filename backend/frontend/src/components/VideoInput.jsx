export default function VideoInput({ url, setUrl, onGenerate }) {

    return (

        <div className="video-input">

            <input
                type="text"
                placeholder="Paste a YouTube URL..."
                value={url}
                onChange={(e) => setUrl(e.target.value)}
            />

            <button onClick={onGenerate}>
                Generate Blog
            </button>

        </div>

    );
}