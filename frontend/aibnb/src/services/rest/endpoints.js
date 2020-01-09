// const baseUrl = "http://127.0.0.1:5000"; // for development
const baseUrl = ""; // for production

export const endpoints = {
    getAllStates: `${baseUrl}/listing/getAllStates`,
    getAllNeighborhoods: `${baseUrl}/listing/getAllNeighborhoods`,
    getAllListings: `${baseUrl}/listing/getAllListings`,
    getListingById: `${baseUrl}/listing/getListingsById`
};
