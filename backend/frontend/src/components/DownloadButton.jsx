export default function DownloadButton({ blog }) {

    if (!blog)
        return null;

    return (

        <div className="download">

            <a
                href={`http://127.0.0.1:8000${blog.path}`}
                target="_blank"
                rel="noreferrer"
            >

                <button>

                    Download Markdown

                </button>

            </a>

        </div>

    );

}