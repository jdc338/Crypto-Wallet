import React from 'react';
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';
import Login from './Login';
import Register from './Register';

function App() {
  return (
    <Router>
      <div className="App">
        <h1>Crypto Wallet Application</h1>
        <Switch>
          <Route exact path="/" component={Login} />
          <Route path="/register" component={Register} />
        </Switch>
        <p>
          Don't have an account? <Link to="/register">Sign up now!</Link>
        </p>
      </div>
    </Router>
  );
}

export default App;
