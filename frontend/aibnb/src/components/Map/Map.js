import React from "react";
import PropTypes from "prop-types";
import ReactMapGL, { Marker, Popup, NavigationControl } from "react-map-gl";
import styled from "styled-components";
import { MAP_BOX_API_KEY } from "./constants";
import Pin from "./Pin";
import InfoWindow from "./InfoWindow";

const navStyle = {
    padding: "10px",
    position: "absolute",
    right: "30px",
    top: 0
};

const MapWrapper = ({
    closePopUpClickHandler,
    viewport = {
        height: "100vh",
        latitude: 37.78,
        longitude: -122.41,
        width: "100%",
        zoom: 8
    },
    popupInfo,
    locations = [],
    setViewPort,
    popUpClickHandler
}) => (
    <Wrapper>
        <ReactMapGL
            mapboxApiAccessToken={MAP_BOX_API_KEY}
            mapStyle="mapbox://styles/mapbox/light-v9"
            onViewportChange={vp => setViewPort(vp)}
            {...viewport}
        >
            {locations &&
                locations.map((location, index) => (
                    <Marker key={index} {...location}>
                        <Pin
                            label={"test"}
                            onClick={() => popUpClickHandler(location)}
                            onMouseEnter={() => popUpClickHandler(location)}
                        />
                    </Marker>
                ))}
            {popupInfo && (
                <Popup
                    tipSize={5}
                    anchor="bottom"
                    {...popupInfo}
                    onClose={closePopUpClickHandler}
                >
                    <InfoWindow {...popupInfo} />
                </Popup>
            )}
            <div className="nav" style={navStyle}>
                <NavigationControl onViewportChange={vp => setViewPort(vp)} />
            </div>
        </ReactMapGL>
    </Wrapper>
);

MapWrapper.propTypes = {
    google: PropTypes.any,
    initialCenter: PropTypes.shape({}),
    locations: PropTypes.shape([]),
    zoom: PropTypes.number
};

const Wrapper = styled.div`
    position: absolute;
    top: 0;
    bottom: 0;
    width: 100%;
`;

export default MapWrapper;
