import React from 'react'
import { Link } from 'react-router-dom'

export default function ProjectRender({globalclasses, localclasses, projects, url}) {
  return (
    <div>
        {projects.map( project => 
        <div className={`${localclasses.project}`}>
            <div className={` ${localclasses.projectText}`}>{project.title}</div>
            <div className={``}>{project.discription}</div>
            <div className={`${localclasses.participants}`}>
                {project.participants.map( participant =>{ 
                    return <span key={participant.id} className={`${localclasses.renderItem} `}>{participant.name}</span> })}
            </div>
            <div className="project-status">{project.status===2 ? "Compliting" : "Complited"}</div>
            <Link to={`/${url}/${project.id}`}><button className={globalclasses.btnNormal}>View detail</button></Link>
        </div>
        )}
    </div>
  )
}
