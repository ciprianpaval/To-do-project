import React, { Component} from 'react'
import { Navbar, Nav} from 'react-bootstrap'
import { NavLink } from 'react-router-dom'
import './Navbars.css'

class Navbars extends Component {
    
    render() { 
            return (
                <Navbar className ="navbar" bg="light" expand="lg">
                    
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="mr-auto"></Nav>
                        <NavLink className="links" to="/">SignUp</NavLink>
                        <NavLink className="links" to="/signin">SignIn</NavLink>
                    </Navbar.Collapse>
                </Navbar>
            );
        }
}
 
export default Navbars;