import React from 'react';
import "./Login.css";
import { Button, FormGroup, FormControl, FormLabel} from "react-bootstrap";
import Navbars from './Navbars'

class SignIn extends React.Component {
    state = {
        username: '',
        password: ''
    };

    handleSignIn = e => {
        e.preventDefault();
        fetch('http://localhost:5000/login', {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
        },
        body: JSON.stringify({
                user_name: this.state.username,
                user_password: this.state.password,
            })
        })
        .then(function(response) {
            console.log(response.status);
            if (!response.ok) {
                throw new Error("HTTP status " + response.status);
            }
            return response.json();
        })
        .then(json => {
            this.props.history.push("/projects");
        })
        .catch(error => {
            alert('Wrong!');
        });
    };

    handleUsernameChange = e => {
        this.setState({
            username: e.target.value
        });
    };

    handlePasswordChange = e => {
        this.setState({
            password: e.target.value
        });
    };

  
    render() {
        return (
            <React.Fragment>
                <Navbars/>  
                <div className="Login">
                    <form  className="form" onSubmit={this.handleSubmit}>
                        <h1>Log In</h1>
                        <FormGroup controlId="username">
                        <FormLabel>Username</FormLabel>
                        <FormControl
                            autoFocus
                            type="text"
                            value={this.state.username}
                            onChange={this.handleUsernameChange}
                        />
                        </FormGroup>
                        <FormGroup controlId="password">
                        <FormLabel>Password</FormLabel>
                        <FormControl
                            value={this.state.password}
                            onChange={this.handlePasswordChange}
                            type="password"
                        />
                        </FormGroup>
                        <Button className="button1"  id="mybutton" block type="submmit" onClick={this.handleSignIn}>Sign In</Button>
                    </form>
                </div>
            </React.Fragment>
        );
    }
}

export default SignIn;