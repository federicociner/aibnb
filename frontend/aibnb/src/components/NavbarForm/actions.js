import { createAction } from "redux-actions";

export const setNavbarStates = createAction("NAVBAR/SET_STATES");
export const setNavbarNeighborhoods = createAction("NAVBAR/SET_NEIGHBORHOODS");
export const setListings = createAction("MAP/SET_ACTIONS");
export const setErrorMessage = createAction("NAVBAR/SET_ERROR_MESSAGE");
