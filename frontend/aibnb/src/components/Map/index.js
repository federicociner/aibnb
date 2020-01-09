import Map from "./Map";
import { compose, withProps, withState, lifecycle } from "recompose";
import { connect } from "react-redux";
import { getListings } from "../NavbarForm/selectors";
import { formatListings } from "./helpers";
import isEqual from "lodash/isEqual";

const initialViewPort = {
    height: "100vh",
    latitude: 37.78,
    longitude: -122.41,
    width: "100%",
    zoom: 8
};

const withViewPort = withState("viewport", "setViewPort", initialViewPort);

const withPopUp = withState("popupInfo", "setPopUp");

const withLocationChanges = lifecycle({
    componentDidUpdate({ locations: prevLocations }) {
        const {
            locations: [{ latitude, longitude } = {}] = [],
            locations,
            setViewPort
        } = this.props;
        console.log(locations, prevLocations);
        if (locations && !isEqual(locations, prevLocations)) {
            setViewPort({
                height: "100vh",
                latitude: Number(latitude),
                longitude: Number(longitude),
                width: "100%",
                zoom: 8
            });
        }
    }
});

const withLocations = withProps(({ setPopUp }) => ({
    closePopUpClickHandler: () => {
        setPopUp("");
    },
    popUpClickHandler: popUp => {
        setPopUp(popUp);
    }
}));

const mapStateToProps = state => ({
    locations: formatListings(getListings(state))
});

export default compose(
    connect(mapStateToProps),
    withViewPort,
    withPopUp,
    withLocations,
    withLocationChanges
)(Map);
