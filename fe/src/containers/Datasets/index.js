import React from 'react';
import { Switch, Route } from 'react-router-dom';
import { connect } from 'react-redux';


import List from './List';
import Detail from './Detail';


export const DatasetRoutes = ({ match }) => (
  <Switch>
    <Route exact path={`${match.url}/page/:pageId`} component={List} />
    <Route exact path={`${match.url}/:id`} component={Detail} />
  </Switch>
);


const mapStateToProps = () => ({});

const ConnectDatasetRoutes = connect(mapStateToProps)(DatasetRoutes);

export default ConnectDatasetRoutes;
