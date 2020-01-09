import React from "react";
import "./index.scss";
import App from "./App";
import createHistory from "history/createBrowserHistory";
import { hydrate } from "react-dom";
import * as serviceWorker from "./serviceWorker";
import configureStore from "./store/configureStore";
import "mapbox-gl/dist/mapbox-gl.css";

const initialState = window.__INITIAL_STATE__;
const history = createHistory();
const store = configureStore(initialState, history);
hydrate(
    <App history={history} store={store} />,
    document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
