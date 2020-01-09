import React from "react";
import styled from "styled-components";

const Pin = ({ ...props }) => <StyledPin {...props} />;

const StyledPin = styled.div`
    background-color: rgba(156, 255, 87, 0.75);
    border-radius: 50%;
    border: 1px solid #fff;
    width: 15px;
    height: 15px;
    margin-left: -7.5px;
    :hover {
        cursor: pointer;
    }
`;

export default Pin;
