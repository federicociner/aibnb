export const getOptionsFromStates = (states = []) =>
    states.map(({ state }) => ({ label: state, value: state }));
export const getOptionsFromNeighborhoods = (neighborhoods = []) =>
    neighborhoods.map(({ neighbourhood_cleansed: hood }) => ({
        label: hood,
        value: hood
    }));
