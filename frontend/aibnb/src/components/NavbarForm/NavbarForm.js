import React from "react";
import PropTypes from "prop-types";
import { Field } from "redux-form";
import styled from "styled-components";
import { Row, Col } from "../common/Grid";
import Theme from "../common/Theme";
import DatePicker from "../common/FormElements/DatePicker";
import Select from "../common/FormElements/Select";
import "react-datepicker/dist/react-datepicker.css";

const required = value => (value ? undefined : "Required");
const NavbarForm = ({
    countryChange,
    errorMessage,
    handleSubmit,
    model,
    stateChange,
    valid
}) => (
    <form onSubmit={values => handleSubmit(values)}>
        <Row>
            <Col>
                <FormLabel>Country</FormLabel>
                <SelectField
                    {...model.country}
                    onChange={countryChange}
                    name="country"
                    component={Select}
                    type="text"
                />
            </Col>
        </Row>
        <Row>
            <Col>
                <FormLabel>State</FormLabel>
                <SelectField
                    {...model.state}
                    onChange={stateChange}
                    name="state"
                    component={Select}
                    type="text"
                    validate={required}
                />
            </Col>
        </Row>
        <Row>
            <Col>
                <FormLabel>Neighborhood</FormLabel>
                <SelectField
                    {...model.neighborhood}
                    name="neighborhood"
                    component={Select}
                    type="text"
                    validate={required}
                />
            </Col>
        </Row>
        <Row>
            <Col>
                <FormLabel>Date</FormLabel>
                <Field
                    {...model.date}
                    name="date"
                    component={DatePicker}
                    type="text"
                />
            </Col>
        </Row>
        <Row>
            <Col>
                <FormLabel>Beds</FormLabel>
                <Field
                    {...model.beds}
                    type="number"
                    name="beds"
                    component="input"
                />
            </Col>
            <Col>
                <FormLabel>Baths</FormLabel>
                <Field
                    {...model.baths}
                    name="baths"
                    component="input"
                    type="number"
                />
            </Col>
        </Row>
        <Row>
            <Col>
                <StyledButton type="submit" active={valid}>
                    Submit
                </StyledButton>
                <ErrorContainer>{errorMessage}</ErrorContainer>
            </Col>
        </Row>
    </form>
);

NavbarForm.propTypes = {
    countryChange: PropTypes.func,
    errorMessage: PropTypes.string,
    handleSubmit: PropTypes.func,
    stateChange: PropTypes.func
};

export default NavbarForm;

const FormLabel = styled.label``;
const SelectField = styled(Field)`
    text-transform: capitalize;
`;
const ErrorContainer = styled.div`
    width: 100%;
    color: red;
`;
const StyledButton = styled.button.attrs({
    disabled: props => !props.active
})`
    background-color: ${props =>
        props.active ? Theme.colors.darkblue : Theme.colors.lightgrey};
    color: ${props => (props.active ? Theme.colors.white : Theme.colors.black)}
    display: inline-block;
    min-width: 50%;
    font-weight: 400;
    text-align: center;
    white-space: nowrap;
    vertical-align: middle;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    border: 1px solid transparent;
    padding: 0.375rem 0.75rem;
    font-size: 1rem;
    line-height: 1.5;
    border-radius: 0.25rem;
`;
