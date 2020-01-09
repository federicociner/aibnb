import axios from "axios";
const axiosInstance = axios.create({
    headers: {
        "X-Requested-By": "123",
        "X-Requested-With": "XMLHttpRequest"
    }
});
const restService = {};
// common get method
restService.get = ({ url, options = {} }) =>
    axiosInstance.get(url, options).catch(err => {
        throw new Error(err);
    });

// common post method
restService.post = ({ url, options = {}, body }) =>
    axiosInstance.post(url, body, options).catch(err => {
        throw new Error(err);
    });

export default restService;
