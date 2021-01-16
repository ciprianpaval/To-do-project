import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom'
import './Project.css';

const Project = props => {

    const { project_manager, project_name, projectID} = props;
    return (
        <React.Fragment>
            <div className="post-wrapper">
                <div className="Post">
                    <Link to={{ 
                        pathname: `/tasks/${encodeURI(projectID)}`, 
                        state: { projectID: projectID}
                    }}>
                    <h2 className="post_title">{ project_name }</h2>
                    </Link>
                    <small>Project Manager: { project_manager }</small>
                </div>
                <br/>
                <br/>
            </div>
        </React.Fragment>
    );
};

Project.propTypes = {
    project_manager: PropTypes.string.isRequired,
    project_name: PropTypes.string.isRequired,
    projectID: PropTypes.number.isRequired
};

export default Project;