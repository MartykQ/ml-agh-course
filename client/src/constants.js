import axios from "axios";

// const host_url = "https://prod-ml-agh.herokuapp.com";
const host_url = "http://localhost:5000";

const _axios = axios.create({
    baseURL: host_url,
});

export default _axios;
