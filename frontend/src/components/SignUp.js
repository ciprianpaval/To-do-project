import React from 'react';
import "./Login.css";
import { Button, FormGroup, FormControl, FormLabel} from "react-bootstrap";
import Navbars from './Navbars'

class SignUp extends React.Component {
    state = {
        username: '',
        password: ''
    };

    handleSignUp = e => {
        e.preventDefault();
        fetch('http://localhost:5000/signup', {
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
            this.props.history.push("/signin");
        })
        .catch(error => {
            alert('Username already exist!');
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
                    <form className="form" onSubmit={this.handleSubmit}>
                        <h1>Register</h1>
                        <FormGroup controlId="username">
                        <FormLabel className="Text">Username</FormLabel>
                        <FormControl
                            autoFocus
                            type="text"
                            value={this.state.username}
                            onChange={this.handleUsernameChange}
                        />
                        </FormGroup>
                        <FormGroup controlId="password">
                        <FormLabel className="Text">Password</FormLabel>
                        <FormControl
                            value={this.state.password}
                            onChange={this.handlePasswordChange}
                            type="password"
                        />
                        </FormGroup>
                        <Button className="button" id="mybutton" block type="submmit" onClick={this.handleSignUp}>Sign Up</Button>
                    </form>
                </div>
            </React.Fragment>
        );
    }
}

export default SignUp;