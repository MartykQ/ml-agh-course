import "./App.css";
import Button from "@mui/material/Button";
import IntegratedSources from "./components/IntegratedSources/IntegratedSources";
import MyModal from "./components/MyModal/MyModal";
import MainPanel from "./components/MainPanel/MainPanel";
import { useState } from "react";

function App() {
    const [modal, setModal] = useState(false);
    const ToggleModdle = () => setModal(!modal);

    return (
        <div className="gradient-background">
            <div className="main-box">
                <div>
                    <MainPanel />
                </div>
                <IntegratedSources />
            </div>
            <MyModal show={modal} close={ToggleModdle} />
        </div>
    );
}

export default App;
