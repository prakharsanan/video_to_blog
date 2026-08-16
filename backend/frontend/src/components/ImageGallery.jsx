export default function ImageGallery({ images }) {

    if (!images?.images?.length || images.images.length <= 1)
        return null;

    const gallery = images.images.slice(1);

    return (

        <section className="gallery">

            <h2>Video Frames</h2>

            <div className="gallery-grid">

                {gallery.map((img, index) => (

                    <img
                        key={index}
                        src={`http://127.0.0.1:8000${img}`}
                        alt={`Frame ${index + 2}`}
                    />

                ))}

            </div>

        </section>

    );

}