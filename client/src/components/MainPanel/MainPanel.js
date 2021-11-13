import TextField from "@mui/material/TextField";
import { useState } from "react";
import "./MainPanel.css";
import LoadingButton from "@mui/lab/LoadingButton";
import MyModal from "../MyModal/MyModal";
import axios from "../../constants";
import SendIcon from "@mui/icons-material/Send";
import PredictedComment from "../PredictedComment/PredictedComment";

const MainPanel = (props) => {
    const [inputText, setInputText] = useState("");

    const [modal, setModal] = useState(false);
    const ToggleModdle = () => setModal(!modal);

    const handleTyping = (e) => {
        setInputText(e.target.value);
    };

    const openModal = () => {
        setModal(true);
    };

    const [comments, setComments] = useState([]);
    const [isLoading, setisLoading] = useState(false);

    const handleClick = () => {
        setisLoading(true);

        let _url = props.ibmModel ? "/ibm_single" : "/single";
        console.log(_url);
        axios
            .post(_url, {
                text: inputText,
            })
            .then((res) => {
                console.log(res);
                setComments(res["data"]);
                setisLoading(false);
                setModal(true);
            });
    };

    return (
        <div>
            <div>
                <div className="mainPanelWrapper">
                    <div className="inputWrapper">
                        <TextField
                            id="outlined-basic"
                            label="Wpisz opinię"
                            variant="filled"
                            multiline
                            onChange={handleTyping}
                            placeholder={"Wpisz swoją opinie"}
                            fullWidth={true}
                            rows={5}
                        />
                    </div>
                    <div className="buttonWrapper">
                        <LoadingButton
                            endIcon={<SendIcon />}
                            loading={false}
                            loadingPosition="end"
                            variant="contained"
                            onClick={handleClick}
                        >
                            Send
                        </LoadingButton>
                    </div>
                </div>
            </div>
            <MyModal show={modal} close={ToggleModdle}>
                <PredictedComment text={comments.text} label={comments.label} />
            </MyModal>
        </div>
    );
};

export default MainPanel;
