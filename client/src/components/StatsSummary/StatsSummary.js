const StatsSummary = (props) => {
    const calculatePositive = (commets) => {
        return commets.filter((c) => {
            return c["label"].toUpperCase() == "POSITIVE";
        }).length;
    };

    const calculateNegative = (commets) => {
        return commets.filter((c) => {
            console.log(c["text"].toUpperCase());
            return c["label"].toUpperCase() == "NEGATIVE";
        }).length;
    };

    const calculateNeutral = (commets) => {
        return commets.filter((c) => {
            return c["label"].toUpperCase() == "NEUTRAL";
        }).length;
    };
    console.log(props.comments);
    return (
        <div>
            <div>Postive: {calculatePositive(props.comments)}</div>
            <div>Negative: {calculateNegative(props.comments)}</div>
            <div>Neutral: {calculateNeutral(props.comments)}</div>
        </div>
    );
};

export default StatsSummary;
