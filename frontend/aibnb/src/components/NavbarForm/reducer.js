import { handleActions } from "redux-actions";
import {
    setNavbarStates,
    setNavbarNeighborhoods,
    setListings,
    setErrorMessage
} from "./actions";

const defaultState = {
    states: [],
    neighborhoods: [],
    listings: [],
    errorMessage: ""
};

export const navbar = handleActions(
    {
        [setNavbarStates]: (state, { payload }) => ({
            ...state,
            states: payload
        }),
        [setNavbarNeighborhoods]: (state, { payload }) => ({
            ...state,
            neighborhoods: payload
        }),
        [setListings]: (state, { payload }) => ({
            ...state,
            listings: payload
        }),
        [setErrorMessage]: (state, { payload }) => ({
            ...state,
            errorMessage: payload
        })
    },
    defaultState
);
