import "./PredictedComment.css";

const PredictedComment = (props) => {
    return (
        <div className="predictedCommentWrapper">
            <div>{props.text}</div>
            <div>{props.label}</div>
        </div>
    );
};

export default PredictedComment;
