import { chainPropTypes } from "@mui/utils";
import axios from "../../constants";
import { useState } from "react";
import MyModal from "../MyModal/MyModal";

const YoutubeSource = () => {
    const [comments, setComments] = useState([]);

    const [modal, setModal] = useState(false);
    const ToggleModdle = () => setModal(!modal);

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
            <MyModal show={modal} close={ToggleModdle}></MyModal>
            <div>YT Source</div>
            <div onClick={() => handleClick()}>click me!</div>
            {comments.map((comment, index) => {
                return <div key={index}>{comment}</div>;
            })}
        </>
    );
};

export default YoutubeSource;
