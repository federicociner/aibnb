import { applyMiddleware, compose, createStore } from "redux";
import thunk from "redux-thunk";
import reduxImmutableStateInvariant from "redux-immutable-state-invariant";
import { routerMiddleware } from "react-router-redux";
import rootReducer from "../reducers";

export default function configureStore(predefinedState = {}, history) {
    const composeEnhancers =
        typeof window === "object" &&
        window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
            ? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__({})
            : compose;

    const middleware = [thunk, routerMiddleware(history)];

    if (process.env.NODE_ENV !== "production") {
        middleware.push(reduxImmutableStateInvariant());
    }

    const enhancer = composeEnhancers(applyMiddleware(...middleware));

    return createStore(rootReducer, predefinedState, enhancer);
}
