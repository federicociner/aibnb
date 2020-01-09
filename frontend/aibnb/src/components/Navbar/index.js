import Navbar from "./Navbar";
import { compose, withProps } from "recompose";

const withCards = withProps(() => ({
    cards: [
        {
            title: "Room Type"
        },
        {
            title: "Activity"
        }
    ]
}));

export default compose(withCards)(Navbar);
