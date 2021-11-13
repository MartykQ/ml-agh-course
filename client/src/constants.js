import axios from "axios";

// const host_url = "https://prod-ml-agh.herokuapp.com";
const host_url = "http://209.250.235.144:5001";
// const host_url = "http://localhost:5000";
const _axios = axios.create({
    baseURL: host_url,
});

export default _axios;
