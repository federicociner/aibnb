import { combineReducers } from "redux";
import reducer from "./reducer";
import visibilityFilter from "./map";
import { reducer as form } from "redux-form";
import { navbar } from "../components/NavbarForm/reducer";

export default combineReducers({
    form,
    reducer,
    navbar,
    visibilityFilter
    // Other reducers here
});
