import React from "react";
import styled from "styled-components";
import NavbarForm from "../NavbarForm";
import { Row, Col } from "../common/Grid";
import PropTypes from "prop-types";
import logo from "../../logo.svg";

const Navbar = () => (
    <Wrapper>
        <Row>
            <LogoCol>
                <Logo src={logo} alt="AIbnb" />
            </LogoCol>
        </Row>
        <Row>
            <Col>
                <NavbarForm />
            </Col>
        </Row>
    </Wrapper>
);

Navbar.propTypes = {
    cards: PropTypes.shape([])
};
export default Navbar;

const Wrapper = styled.div`
    padding: 30px 20px;
    height: 100%;
    width: 350px;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    background-color: rgba(250, 250, 250, 0.75);
    overflow-x: hidden;
    transition: 0.5s;
`;
const Logo = styled.img`
    width: 150px;
    margin: auto;
`;
const LogoCol = styled(Col)`
    text-align: center;
`;
