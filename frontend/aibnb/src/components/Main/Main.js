import React, { Fragment } from "react";
import Map from "../Map";
import Navbar from "../Navbar";
import "./globalStyles";
import configureStore from "../../store/configureStore";
import { Provider } from "react-redux";

const store = configureStore();

const Main = () => (
    <Provider store={store}>
        <Fragment>
            <Navbar />
            <Map />
        </Fragment>
    </Provider>
);

export default Main;
