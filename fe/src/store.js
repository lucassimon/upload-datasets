import { all } from 'redux-saga/effects';
import { createBrowserHistory } from 'history';
import { createStore, applyMiddleware, combineReducers } from 'redux';
import { connectRouter, routerMiddleware } from 'connected-react-router';
import { composeWithDevTools } from 'redux-devtools-extension';
import createSagaMiddleware from 'redux-saga';

// CONTAINERS

// Create a history of your choosing (we're using a browser history in this case)
const history = createBrowserHistory();
// Build the middleware for intercepting and dispatching navigation actions

const rootReducer = combineReducers({
  router: connectRouter(history),
});

const sagaMiddleware = createSagaMiddleware();

const store = createStore(
  rootReducer,
  composeWithDevTools(
    applyMiddleware(
      routerMiddleware(history),
      sagaMiddleware,
    ),
  ),
);


function* rootSaga() { yield all([]); }

sagaMiddleware.run(rootSaga);

export { store, history };
