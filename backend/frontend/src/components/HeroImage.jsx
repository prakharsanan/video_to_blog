export default function HeroImage({ images }) {

    if (!images?.images?.length)
        return null;

    return (

        <section className="hero-image">

            <img
                src={`http://127.0.0.1:8000${images.images[0]}`}
                alt="Hero"
            />

        </section>

    );

}