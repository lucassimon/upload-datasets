import React from 'react';
import { Switch, Route } from 'react-router-dom';
import { connect } from 'react-redux';

import ConnectDatasets from './Datasets';

export const Main = ({ match }) => (
  <Switch>
    <Route path={`${match.url}`} component={ConnectDatasets} />
  </Switch>
);


const mapStateToProps = () => ({});

const ConnectMain = connect(mapStateToProps)(Main);

export default ConnectMain;
