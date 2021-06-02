import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { createMuiTheme, ThemeProvider } from "@material-ui/core";
const theme = createMuiTheme({
  palette: {
     primary: {
        main: "#c690e5" // This is an orange looking color
               },
     secondary: {
        main: "#ffcc80" //Another orange-ish color
                }
           },

});
ReactDOM.render(
  <React.StrictMode>
    <ThemeProvider theme={theme}><App /></ThemeProvider>
    
  </React.StrictMode>,
  document.getElementById('root')
);
