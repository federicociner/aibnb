import { reduxForm } from "redux-form";
import NavbarFormView from "./NavbarForm";
import { navFormModel } from "./model";

import { compose } from "redux";
import { connect } from "react-redux";
import moment from "moment";
import { withProps } from "recompose";
import restService from "../../services/rest/rest";
import { endpoints } from "../../services/rest/endpoints";
import {
    setNavbarStates,
    setNavbarNeighborhoods,
    setListings,
    setErrorMessage
} from "./actions";
import { getNeighborhoods, getStates, getErrorMessage } from "./selectors";
import { getOptionsFromStates, getOptionsFromNeighborhoods } from "./helpers";
import isEmpty from "lodash/isEmpty";

const handleSubmission = (values, dispatch) => {
    const {
        country: { value: country } = {},
        state: { value: state } = {},
        neighborhood: { value: neighborhood } = {},
        beds,
        baths,
        date
    } = values;

    restService
        .get({
            url: endpoints.getAllListings,
            options: {
                params: {
                    country,
                    state,
                    neighborhood,
                    beds,
                    baths,
                    date: moment.unix(date).format("X")
                }
            }
        })
        .then(({ data: { data } = {} }) => {
            if (!data || isEmpty(data)) {
                dispatch(
                    setErrorMessage(
                        "No Results Were Found. Please Try Different Parameters."
                    )
                );
            } else {
                dispatch(setErrorMessage(""));
            }
            dispatch(setListings(data));
        })
        .catch(error => {
            console.log(error);
            return [];
        });

    return values;
};

const withChangeHandlers = withProps(
    ({ setNavbarStates, setNavbarNeighborhoods }) => ({
        countryChange: ({ value }) => {
            restService
                .get({
                    url: endpoints.getAllStates,
                    options: { params: { country: value } }
                })
                .then(({ data: { data } = {} }) => {
                    setNavbarStates(getOptionsFromStates(data));
                })
                .catch(error => {
                    console.log(error);
                    return [];
                });
        },
        stateChange: ({ value }) => {
            restService
                .get({
                    url: endpoints.getAllNeighborhoods,
                    options: { params: { state: value } }
                })
                .then(({ data: { data } = {} }) => {
                    setNavbarNeighborhoods(getOptionsFromNeighborhoods(data));
                })
                .catch(error => {
                    console.log(error);
                    return [];
                });
        }
    })
);

const createViewModel = withProps(({ states, neighborhoods }) => ({
    model: navFormModel({ states, neighborhoods })
}));

const mapStateToProps = state => ({
    initialValues: {
        baths: "2",
        beds: "2",
        country: {
            label: "United States",
            value: "US"
        },
        date: moment()
    },
    errorMessage: getErrorMessage(state),
    states: getStates(state),
    neighborhoods: getNeighborhoods(state)
});

const NavbarForm = reduxForm({
    form: "contact",
    onSubmit: handleSubmission
})(NavbarFormView);

export default compose(
    connect(
        mapStateToProps,
        {
            setNavbarStates,
            setNavbarNeighborhoods,
            setListings,
            setErrorMessage
        }
    ),
    withChangeHandlers,
    createViewModel
)(NavbarForm);
