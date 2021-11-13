import ReactDOM from "react-dom";
import "./MyModal.scss";

import Button from "@mui/material/Button";

const Modal = ({ show, close, title, children }) => {
    return ReactDOM.createPortal(
        <div>
            {show ? (
                <div className="modalContainer" onClick={() => close()}>
                    <div className="modal" onClick={(e) => e.stopPropagation()}>
                        <header className="modal_header">
                            <h2 className="modal_header-title"> {title} </h2>
                            <Button variant="outlined" onClick={() => close()}>
                                Zamknij
                            </Button>
                        </header>

                        <main className="modal_content"> {children} </main>
                    </div>
                </div>
            ) : null}
        </div>,
        document.getElementById("modal")
    );
};

export default Modal;
