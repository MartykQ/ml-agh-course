import React, { useState } from "react";
import "./IntegratedSources.css";
import YoutubeSource from "../YoutubeSource/YoutubeSource";
import YouTubeIcon from "@mui/icons-material/YouTube";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import TwitterIcon from "@mui/icons-material/Twitter";
import TwitterSource from "../TwitterSource/TwitterSource";

const IntegratedSources = (props) => {
    const [activeName, setActiveName] = useState("YT");

    const chooseActive = (option) => {
        setActiveName(option);
    };

    const [value, setValue] = React.useState(0);

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    const activeComponent = () => {
        console.log(activeName);
        switch (value) {
            case 0:
                return <YoutubeSource ibmModel={props.ibmModel} />;
            case 1:
                return <TwitterSource ibmModel={props.ibmModel} />;
        }
    };

    console.log("render");
    return (
        <div className="box">
            <div className="header">
                <Box sx={{ borderBottom: 1, borderColor: "divider" }}>
                    <Tabs value={value} onChange={handleChange} aria-label="basic tabs example">
                        <Tab icon={<YouTubeIcon />} iconPosition="start" label="Youtube" />
                        <Tab icon={<TwitterIcon ibmModel={props.ibmModel} />} iconPosition="start" label="Twitter" />
                    </Tabs>
                </Box>
            </div>
            <div className="modal">{activeComponent()}</div>
        </div>
    );
};

export default IntegratedSources;
