import React, { Component } from "react";
import Project from "./Project";
import './Projects.css';

class Projects extends Component {
    state = {
        projects: [],
        project_name: '',
        project_manager: ''
    };

    componentDidMount() {
        this.fetchWithDelay();
    }

    fetchWithDelay = () => {
        const delay = ms => new Promise(resolve => setTimeout(resolve, ms));
        Promise.all([delay(3000), this.handleData()]);
    };

    handleData = () => {
        fetch(`http://localhost:5000/api/db/projects`,{
            method: 'GET',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(function(response) {
            console.log(response.status);
            if (!response.ok) {
                throw new Error("HTTP status " + response.status);
            }
            return response.json();})
        .then(json => {
            this.setState({ projects: json.projects});
        })
        .catch(err => console.log(err));
    }

    handleChangePage = (event) => {
        this.setState( this.fetchWithDelay);
    };

    addProject = () => {

        fetch(`http://localhost:5000/api/db/projects`, 
          {
            method: 'POST',
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            }, 
            body: JSON.stringify({ 
                project_name: this.state.project_name,
                project_manager: this.state.project_manager
            })
          }).then(res => res.json()).then(res => {
                this.handleData();
          })
        }
    
    handleProjectNameChange = e => {
            this.setState({
                project_name: e.target.value
            });
     };

     handleProjectManagerChange = e => {
            this.setState({
                project_manager: e.target.value
            });
    };

    render() {
        return (
            <React.Fragment>
                 <div className="Title">
                 <h1>Project List</h1>
                 </div>
                 <div className="AddProject">
                   <input type="text" placeholder="Project" value={this.state.project_name} onChange={this.handleProjectNameChange}/>
                   <input type="text" placeholder="Manager" value={this.state.project_manager} onChange={this.handleProjectManagerChange}/>
                   <button className="btn" onClick={this.addProject}>Add new project</button>
                   
               </div>
                <div className="Posts">
                    {
                        
                        this.state.projects.map((project, i) => (
                        <Project key={i} {...project} />))    
                    }
                </div>   
            
            </React.Fragment>
        )
    }
}

export default Projects;