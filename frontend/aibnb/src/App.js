import React from "react";
import { Provider } from "react-redux";
import { Router, Route } from "react-router";
import Main from "./components/Main";
import "mapbox-gl/dist/mapbox-gl.css";
import { library } from "@fortawesome/fontawesome-svg-core";
import {
    faBath,
    faBed,
    faUsers,
    faStar
} from "@fortawesome/free-solid-svg-icons";
library.add(faBath);
library.add(faBed);
library.add(faUsers);
library.add(faStar);
/* eslint-disable react/prop-types */
const App = ({ store, history }) => (
    <Provider store={store}>
        <Router history={history}>
            <Route path="/" component={Main} />
        </Router>
    </Provider>
);

export default App;
