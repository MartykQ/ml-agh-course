import React, { useState } from "react";
import "./IntegratedSources.css";
import YoutubeSource from "../YoutubeSource/YoutubeSource";

const IntegratedSources = () => {
    const [activeName, setActiveName] = useState("YT");

    const chooseActive = (option) => {
        setActiveName(option);
    };

    const activeComponent = () => {
        console.log(activeName);
        switch (activeName) {
            case "YT":
                return <YoutubeSource />;
            case "Placeholder":
                return <div>Placeholder 1</div>;
            case "Placeholder2":
                return <div>Placeholder 2</div>;
        }
    };

    console.log("render");
    return (
        <div className="box">
            <div className="header">
                <div
                    className={"headerOption " + (activeName == "YT" ? "active" : "inactive")}
                    onClick={() => setActiveName("YT")}
                >
                    YT
                </div>
                <div
                    className={"headerOption " + (activeName == "Placeholder" ? "active" : "inactive")}
                    onClick={() => setActiveName("Placeholder")}
                >
                    Placeholder
                </div>
                <div
                    className={"headerOption " + (activeName == "Placeholder2" ? "active" : "inactive")}
                    onClick={() => setActiveName("Placeholder2")}
                >
                    Placeholder2
                </div>
            </div>
            <div className="modal">{activeComponent()}</div>
        </div>
    );
};

export default IntegratedSources;
