import { injectGlobal } from "styled-components";
import { normalize } from "polished";

injectGlobal`
  ${normalize()};
`;

injectGlobal`
  * {
    font-family: 'Roboto', sans-serif;
    box-sizing: border-box;
  }

  body {
    font-size: 16px;
  }

  [cta] {
    cursor: pointer;
  }

  input[type="text"],
  input[type="email"],
  input[type="password"] {
    border-radius: 0;
  }

  input::-ms-clear,
  input::-ms-reveal {
    display: none;
  }

  .leaflet-container {
    height: 400px;
    width: 80%;
    margin: 0 auto;
  }
  input[type="text"],
  input[type="number"]{
    display: block;
    width: 100%;
    padding: .375rem .75rem;
    font-size: 1rem;
    line-height: 1.5;
    color: #495057;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid #ced4da;
    border-radius: .25rem;
    transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}

.react-datepicker-wrapper, .react-datepicker__input-container  {
    width: 100%;
}



`;
