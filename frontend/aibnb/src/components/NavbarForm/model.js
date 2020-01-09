import isEmpty from "lodash/isEmpty";

export const navFormModel = ({ neighborhoods, states }) => ({
    baths: {
        min: "1"
    },
    beds: {
        min: "1"
    },
    country: {
        options: [
            {
                label: "andorra",
                value: "andorra"
            },
            {
                label: "argentina",
                value: "argentina"
            },
            {
                label: "australia",
                value: "australia"
            },
            {
                label: "austria",
                value: "austria"
            },
            {
                label: "belgium",
                value: "belgium"
            },
            {
                label: "bermuda",
                value: "bermuda"
            },
            {
                label: "brazil",
                value: "brazil"
            },
            {
                label: "canada",
                value: "canada"
            },
            {
                label: "colombia",
                value: "colombia"
            },
            {
                label: "denmark",
                value: "denmark"
            },
            {
                label: "france",
                value: "france"
            },
            {
                label: "germany",
                value: "germany"
            },
            {
                label: "ireland",
                value: "ireland"
            },
            {
                label: "italy",
                value: "italy"
            },
            {
                label: "japan",
                value: "japan"
            },
            {
                label: "mauritius",
                value: "mauritius"
            },
            {
                label: "mexico",
                value: "mexico"
            },
            {
                label: "myanmar [burma]",
                value: "myanmar [burma]"
            },
            {
                label: "netherlands",
                value: "netherlands"
            },
            {
                label: "norway",
                value: "norway"
            },
            {
                label: "other",
                value: "other"
            },
            {
                label: "peru",
                value: "peru"
            },
            {
                label: "poland",
                value: "poland"
            },
            {
                label: "portugal",
                value: "portugal"
            },
            {
                label: "south africa",
                value: "south africa"
            },
            {
                label: "spain",
                value: "spain"
            },
            {
                label: "sweden",
                value: "sweden"
            },
            {
                label: "switzerland",
                value: "switzerland"
            },
            {
                label: "united kingdom",
                value: "united kingdom"
            },
            {
                label: "united states",
                value: "united states"
            },
            {
                label: "uruguay",
                value: "uruguay"
            },
            {
                label: "vanuatu",
                value: "vanuatu"
            },
            {
                label: "vatican city",
                value: "vatican city"
            }
        ]
    },
    neighborhood: {
        defaultValue: !isEmpty(neighborhoods) && neighborhoods[0],
        options: neighborhoods,
        isDisabled: isEmpty(neighborhoods)
    },
    state: {
        defaultValue: !isEmpty(states) && states[0],
        options: states,
        isDisabled: isEmpty(states)
    }
});
