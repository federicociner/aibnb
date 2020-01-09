import React from "react";
import PropTypes from "prop-types";
import styled from "styled-components";
import { Row, Col, Container } from "../common/Grid";
import Theme from "../common/Theme";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Rating from "react-rating";

const InfoWindow = ({
    accommodates = "8",
    availability_365 = "80",
    bathrooms = "2",
    bedrooms = "2",
    compound,
    city,
    number_of_reviews = "535",
    property_type = "Single Family",
    price = "1500",
    review_scores_rating = 4.5,
    state,
    zipcode
}) => (
    <Wrapper>
        <PropertyRow>
            <Col>
                <PropertyBadge>{property_type}</PropertyBadge>
            </Col>
            <PropertyInfoCol>
                <PropertyInfoContainer>
                    <PropertyInfoRow>
                        <IconTile>
                            {bedrooms}
                            <FontAwesomeIcon icon="bed" pull="right" />
                        </IconTile>
                        <IconTile>
                            {bathrooms}
                            <FontAwesomeIcon icon="bath" pull="right" />
                        </IconTile>
                        <IconTile>
                            {accommodates}
                            <FontAwesomeIcon icon="users" pull="right" />
                        </IconTile>
                    </PropertyInfoRow>
                    <RatingRow>
                        <Rating
                            initialRating={review_scores_rating}
                            readonly
                            emptySymbol={
                                <FontAwesomeIcon
                                    icon="star"
                                    color={Theme.colors.lightgrey}
                                />
                            }
                            fullSymbol={
                                <FontAwesomeIcon icon="star" color="#ffd800" />
                            }
                        />
                        <RatingText>
                            {compound} ({number_of_reviews})
                        </RatingText>
                    </RatingRow>
                </PropertyInfoContainer>
            </PropertyInfoCol>
        </PropertyRow>
        <AddressContainer>
            {city}, {state}, {zipcode}
        </AddressContainer>
        <StatTileContainer>
            <Row>
                <StatCol>
                    <StatTile>
                        <Stat>${price}</Stat>
                        <StatTitle>Predicted Price</StatTitle>
                    </StatTile>
                </StatCol>
                <StatCol>
                    <StatTile>
                        <Stat>{availability_365}%</Stat>
                        <StatTitle>Availability</StatTitle>
                    </StatTile>
                </StatCol>
                {compound && (
                    <StatCol>
                        <StatTile>
                            <Stat>
                                {compound}
                                /10
                            </Stat>
                            <StatTitle>Sentiment</StatTitle>
                        </StatTile>
                    </StatCol>
                )}
            </Row>
        </StatTileContainer>
    </Wrapper>
);

InfoWindow.propTypes = {
    accommodates: PropTypes.string,
    availability_365: PropTypes.string,
    bathrooms: PropTypes.string,
    bedrooms: PropTypes.string,
    city: PropTypes.string,
    compound: PropTypes.string,
    number_of_reviews: PropTypes.string,
    price: PropTypes.string,
    property_type: PropTypes.string,
    review_scores_rating: PropTypes.string,
    state: PropTypes.string,
    zipcode: PropTypes.string
};

export default InfoWindow;

const Wrapper = styled.div`
    min-width: 300px;
    min-height: 100px;
    padding: 10px;
`;

const PropertyRow = styled(Row)`
    border-bottom: 1px solid ${Theme.colors.grey};
`;

const PropertyBadge = styled(Container)`
    background-color: ${Theme.colors.lightblue};
    color: ${Theme.colors.white};
    padding: 15px 5px;
    position: absolute;
    width: 150px;
    left: -25px;
    text-transform: capitalize;

    &::after {
        content: "";
        background-color: ${Theme.colors.darkblue};
        width: 25px;
        height: 25px;
        position: absolute;
        left: 0;
        bottom: -25px;
        transform: skewY(223deg) translateY(-14px);
        z-index: -1;
    }
`;
const PropertyInfoContainer = styled(Container)`
    text-align: left;
    font-weight: bold;
    font-size: 20px;
    padding: 5px 0;
`;
const PropertyInfoRow = styled(Row)`
    padding: 0 10px;
`;
const RatingRow = styled(Row)`
    padding: 0 10px;
`;
const PropertyInfoCol = styled(Col)`
    flex-grow: 2;
    padding-left: 20px;
`;

const IconTile = styled(Col)`
    text-align: left;
    font-weight: bold;
    font-size: 20px;
    padding: 10px 5px;
`;

const AddressContainer = styled(Container)`
    text-align: left;
    font-weight: bold;
    padding: 20px 0;
    text-transform: uppercase;
`;
const StatCol = styled(Col)`
    padding: 2px;
`;

const StatTile = styled.div`
    background-color: ${Theme.colors.lightgrey};
    border: 1px solid ${Theme.colors.grey};
    width: 100%;
    min-height: 50px;
`;

const StatTileContainer = styled(Container)`
    bottom: 0px;
`;
const RatingText = styled.h3`
    margin: 0px;
    font-size: 15px;
    line-height: 23px;
    text-align: left;
    color: ${Theme.colors.black};
`;

const StatTitle = styled.h4`
    margin: 0px;
    font-size: 12px;
    text-align: center;
    color: ${Theme.colors.black};
`;

const Stat = styled.h5`
    margin: 0px;
    font-size: 24px;
    font-weight: 400;
    text-align: center;
    color: ${Theme.colors.black};
`;
