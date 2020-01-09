import React from "react";
import styled from "styled-components";
import PropTypes from "prop-types";

const Card = ({ children, title }) => (
    <Container>
        {title && (
            <Header>
                <Title>{title}</Title>
            </Header>
        )}
        <Body>{children}</Body>
    </Container>
);

Card.propTypes = {
    children: PropTypes.node,
    title: PropTypes.string
};

export default Card;

const Container = styled.div`
    position: relative;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-direction: column;
    flex-direction: column;
    min-width: 0;
    word-wrap: break-word;
    background-color: #fff;
    background-clip: border-box;
    border: 1px solid rgba(0, 0, 0, 0.125);
    border-radius: 0.25rem;
`;
const Title = styled.h2`
    margin: 2px;
`;

const Body = styled.div`
    -ms-flex: 1 1 auto;
    flex: 1 1 auto;
    padding: 1.25rem;
`;

const Header = styled.div`
    padding: 0.75rem 1.25rem;
    margin-bottom: 0;
    border-bottom: 1px solid rgba(0, 0, 0, 0.125);
`;
