import SelectView from "./Select";
import { connect } from "react-redux";
import { change } from "redux-form";
import { compose } from "recompose";

export default compose(
    connect(
        null,
        change
    )
)(SelectView);
