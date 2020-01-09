import React from "react";
import PropTypes from "prop-types";
import styled from "styled-components";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

const DatePickerView = ({ handleChange, startDate }) => (
    <Wrapper>
        <StyledDatePicker selected={startDate} onChange={handleChange} />
    </Wrapper>
);

DatePickerView.propTypes = {
    handleChange: PropTypes.func,
    input: PropTypes.shape({}),
    onCustomChange: PropTypes.func,
    startDate: PropTypes.shape({})
};

const Wrapper = styled.div``;
const StyledDatePicker = styled(DatePicker)`
    input {
        width: 100%;
    }
`;

export default DatePickerView;
