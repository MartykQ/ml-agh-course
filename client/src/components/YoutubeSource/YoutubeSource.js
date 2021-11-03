import { chainPropTypes } from "@mui/utils";
import axios from "../../constants";
import { useState } from "react";
const YoutubeSource = () => {
    const [comments, setComments] = useState([]);

    const handleClick = () => {
        console.log(process.env.ENV_VARIABLE);
        axios
            .post("/youtube_comments", {
                url: "https://www.youtube.com/watch?v=cqdVBhPp_xk",
            })
            .then((res) => {
                setComments(res["data"]);
            });
    };

    return (
        <>
            <div>YT Source</div>
            <div onClick={() => handleClick()}>click me!</div>
            {comments.map((comment, index) => {
                return <div key={index}>{comment}</div>;
            })}
        </>
    );
};

export default YoutubeSource;
