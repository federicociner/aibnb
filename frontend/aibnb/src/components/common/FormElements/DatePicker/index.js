import DatePickerView from "./DatePicker";
import { connect } from "react-redux";
import { change } from "redux-form";
import { compose, withState, withProps } from "recompose";
import moment from "moment";
const withDateValues = withState("startDate", "setStartDate", moment());

const withDateMethods = withProps(
    ({ setStartDate, input: { onChange } = {} }) => ({
        handleChange: date => {
            setStartDate(date);
            onChange(date);
        }
    })
);

export default compose(
    connect(
        null,
        change
    ),
    withDateValues,
    withDateMethods
)(DatePickerView);
