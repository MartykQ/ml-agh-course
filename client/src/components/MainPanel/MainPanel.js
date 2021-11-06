import TextField from "@mui/material/TextField";
import { useState } from "react";
import "./MainPanel.css";
import LoadingButton from "@mui/lab/LoadingButton";
import MyModal from "../MyModal/MyModal";

import SendIcon from "@mui/icons-material/Send";

const MainPanel = () => {
    const [inputText, setInputText] = useState("");

    const [modal, setModal] = useState(false);
    const ToggleModdle = () => setModal(!modal);

    const handleTyping = (e) => {
        setInputText(e.target.value);
    };

    const openModal = () => {
        setModal(true);
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
                            onClick={openModal}
                        >
                            Send
                        </LoadingButton>
                    </div>
                </div>
            </div>
            <MyModal show={modal} close={ToggleModdle}>
                Tutaj bedzie ocenka opinii
            </MyModal>
        </div>
    );
};

export default MainPanel;
