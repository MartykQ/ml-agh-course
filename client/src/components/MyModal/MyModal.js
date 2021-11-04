import ReactDOM from "react-dom";
import "./MyModal.scss";

const Modal = ({ show, close, title, children }) => {
    return ReactDOM.createPortal(
        <div>
            {show ? (
                <div className="modalContainer" onClick={() => close()}>
                    <div className="modal" onClick={(e) => e.stopPropagation()}>
                        <header className="modal_header">
                            <h2 className="modal_header-title"> {title} </h2>
                            <button className="close" onClick={() => close()}>
                                zamykaj
                            </button>
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
