import React, { Component } from 'react';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'
import SignIn from './components/SignIn'
import SignUp from './components/SignUp'
import Task from './components/tasks'
import Projects from './components/Projects';


class App extends Component {
    render() { 
        return (
            <Router>
                <Switch>
                    <Route exact path = '/signin' component = { SignIn }/>
                    <Route exact path = '/' component = { SignUp }/>
                    <Route exact path = '/projects' component = { Projects }/>
                    <Route exact path = '/tasks/:projectID' component = { Task }/>
                </Switch>
            </Router>
        );
    }
}

export default App;