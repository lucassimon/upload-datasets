import React from 'react';
import { Switch, Route } from 'react-router-dom';

import ConnectNavbar from './components/Navbar';
import ConnectMain from './containers/Main';
import Upload from './containers/Uploads';

const App = () => (
  <div>
    <ConnectNavbar />
    <Switch>
      <Route exact path="/" component={Upload} />
      <Route path="/datasets" component={ConnectMain} />
    </Switch>
  </div>
);

export default App;
