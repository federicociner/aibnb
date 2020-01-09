import React from "react";
import PropTypes from "prop-types";
import styled from "styled-components";
import "react-datepicker/dist/react-datepicker.css";
import Select from "react-select";
const SelectView = ({
    className,
    defaultValue,
    input: { onChange },
    isDisabled,
    name,
    options,
    value
}) => (
    <Wrapper className={className}>
        <Select
            name={name}
            isDisabled={isDisabled}
            options={options}
            onChange={onChange}
            value={value}
            defaultValue={defaultValue}
            onBlurResetsInput={false}
        />
    </Wrapper>
);

SelectView.propTypes = {
    className: PropTypes.string,
    defaultValue: PropTypes.string,
    handleChange: PropTypes.func,
    isDisabled: PropTypes.bool,
    input: PropTypes.shape({}),
    name: PropTypes.string,
    onChange: PropTypes.func,
    onCustomChange: PropTypes.func,
    options: PropTypes.shape({}),
    value: PropTypes.string
};

const Wrapper = styled.div``;

export default SelectView;
