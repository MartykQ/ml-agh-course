import { chainPropTypes } from "@mui/utils";
import axios from "../../constants";
import { useState } from "react";
import MyModal from "../MyModal/MyModal";
import LoadingButton from "@mui/lab/LoadingButton";
import TextField from "@mui/material/TextField";
import SendIcon from "@mui/icons-material/Send";
import "./YoutubeSource.css";

import PredictedComment from "../PredictedComment/PredictedComment";
import StatsSummary from "../StatsSummary/StatsSummary";

const YoutubeSource = (props) => {
    const [comments, setComments] = useState([]);
    const [inputText, setInputText] = useState("");
    const [modal, setModal] = useState(false);
    const ToggleModdle = () => setModal(!modal);
    const [isLoading, setisLoading] = useState(false);

    const handleClick = () => {
        setisLoading(true);

        let _url = props.ibmModel ? "/ibm_youtube_comments" : "/youtube_comments";
        console.log(_url);
        axios
            .post(_url, {
                url: inputText,
            })
            .then((res) => {
                console.log(res);
                setComments(res["data"]);
                setisLoading(false);
                setModal(true);
            });
    };

    const handleTyping = (e) => {
        setInputText(e.target.value);
    };

    return (
        <>
            <MyModal show={modal} close={ToggleModdle}>
                <StatsSummary comments={comments} />
                {comments.map((comment, index) => {
                    return (
                        <div key={index}>
                            <PredictedComment text={comment.text} label={comment.label} />
                        </div>
                    );
                })}
            </MyModal>
            <div className="inputButtonWrapper">
                <TextField label="Youtube url" fullWidth={true} onChange={handleTyping} />
                <LoadingButton
                    endIcon={<SendIcon />}
                    loading={isLoading}
                    loadingPosition="end"
                    variant="contained"
                    onClick={() => handleClick()}
                >
                    Get comments
                </LoadingButton>
            </div>
        </>
    );
};

export default YoutubeSource;
