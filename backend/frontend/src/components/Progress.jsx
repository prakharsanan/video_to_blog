const steps = [
    "Downloading Video",
    "Extracting Audio",
    "Generating Transcript",
    "Generating Blog",
    "Extracting Images",
];

export default function Progress({ currentStep }) {

    if(currentStep===5)
    return null;

    if(currentStep===-1)
        return null;

    return (

        <div className="progress-card">

            <h2>Processing Pipeline</h2>

            {steps.map((step, index) => (

                <div
                    key={index}
                    className="progress-row"
                >

                    <span className="progress-icon">

                        {index < currentStep && "✅"}

                        {index === currentStep && "⏳"}

                        {index > currentStep && "⚪"}

                    </span>

                    <span>{step}</span>

                </div>

            ))}

        </div>

    );

}