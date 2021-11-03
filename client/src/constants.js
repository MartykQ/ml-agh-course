import axios from "axios";

const host_url = "https://prod-ml-agh.herokuapp.com";

const _axios = axios.create({
    baseURL: host_url,
});

export default _axios;
