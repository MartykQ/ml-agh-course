import { chainPropTypes } from "@mui/utils";
import axios from "../../constants";
import { useState } from "react";
import MyModal from "../MyModal/MyModal";
import LoadingButton from "@mui/lab/LoadingButton";
import TextField from "@mui/material/TextField";
import SendIcon from "@mui/icons-material/Send";
import "./TwitterSource.css";

import PredictedComment from "../PredictedComment/PredictedComment";
import StatsSummary from "../StatsSummary/StatsSummary";

const TwitterSource = (props) => {
    const [comments, setComments] = useState([]);
    const [inputText, setInputText] = useState("");
    const [modal, setModal] = useState(false);
    const ToggleModdle = () => setModal(!modal);
    const [isLoading, setisLoading] = useState(false);

    const handleClick = () => {
        setisLoading(true);
        let _url = props.ibmModel ? "/ibm_tweets" : "/tweets";
        console.log(_url);
        axios
            .post(_url, {
                url: inputText,
            })
            .then((res) => {
                setComments(res["data"]);
                setisLoading(false);
                setModal(true);
            })
            .catch(() => {
                alert("blad");
                setisLoading(false);
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
                <TextField label="Twitter url" fullWidth={true} onChange={handleTyping} />
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

export default TwitterSource;
