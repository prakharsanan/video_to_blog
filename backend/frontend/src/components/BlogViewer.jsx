import ReactMarkdown from "react-markdown";

export default function BlogViewer({ blog }) {

    if (!blog) return null;

    return (
        <section className="blog">
            <ReactMarkdown>
                {blog.content}
            </ReactMarkdown>
        </section>
    );
}