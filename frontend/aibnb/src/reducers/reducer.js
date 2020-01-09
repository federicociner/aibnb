import { handleActions } from "redux-actions";
import { setItem } from "../actions/actions";
import { ITEM_CONSTANT } from "../components/Main/constants";

const initialState = {
    isFetching: ITEM_CONSTANT
};

const app = handleActions(
    {
        [setItem]: (state, { payload: { isFetching } }) => ({
            ...state,
            isFetching
        })
    },
    initialState
);

export default app;
