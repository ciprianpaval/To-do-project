import React, {useState, useEffect} from 'react';
import './App.css';
import {DragDropContext, Droppable, Draggable} from "react-beautiful-dnd";
import _ from "lodash";
import { useParams } from "react-router-dom";

function Task() {
  const {projectID } = useParams()
  const [text, setText] = useState("")
  const [state, setState] = useState({
    "todo": {
      title: "Todo",
      items: []
    }, 
    "in-progress": {
      title: "In Progress",
      items: []
    },
    "done": {
      title: "Completed",
      items: []
    }
  })

  useEffect(() => {
  	fetch(`http://localhost:5000/api/db/tasks/${projectID}`).then(res => res.json()).then(res => {
  		const newstate = {
  			...state,
  			todo: {
  				...state.todo,
  				items: [...state.todo.items, ...res.tasks]
  			}
  		}
  		setState(newstate)
  	})
  }, []);

  const handleDragEnd = ({destination, source}) => {
    if (!destination) {
      return
    }

    if (destination.index === source.index && destination.droppableId === source.droppableId) {
      return
    }

    // Creating a copy of item before removing it from state
    const itemCopy = {...state[source.droppableId].items[source.index]}

    setState(prev => {
      prev = {...prev}
      // Remove from previous items array
      prev[source.droppableId].items.splice(source.index, 1)


      // Adding to new items array location
      prev[destination.droppableId].items.splice(destination.index, 0, itemCopy)

      return prev
    })
    console.log(source, destination, itemCopy);
    console.log(destination.droppableId)
    setTimeout(() => {
      fetch(`http://localhost:5000/api/db/tasks/${projectID}/${itemCopy.taskID}`, 
      {
        method: 'PUT',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        }, 
        body: JSON.stringify({ 
          status: destination.droppableId
        })
      })
    }, 200);
   }

   const addItem = () => {

    fetch(`http://localhost:5000/api/db/tasks/${projectID}`, 
      {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        }, 
        body: JSON.stringify({ 
          task_description: text,
          projectID: projectID
        })
      }).then(res => res.json()).then(res => {
        const newState = {
          ...state,
          todo: {
            ...state.todo,
            items: [...state.todo.items, res]
          }
        }
        setState(newState);
      });

    setText("")
  }

  return (
    
    <div className="App">
      <div className="Title">
                 <h1>Tasks</h1>
      </div>
     <div className="formular">
    <input type="text" value={text} onChange={(e) => setText(e.target.value)}/>
    <button onClick={addItem}>Add</button>
    </div>
    <div className="columns">
      <DragDropContext onDragEnd={handleDragEnd}>
        {_.map(state, (data, key) => {
          return(
            <div key={key} className={"column"}>
              <h3>{data.title}</h3>
              <Droppable droppableId={key}>
                {(provided, snapshot) => {
                  return(
                    <div
                      ref={provided.innerRef}
                      {...provided.droppableProps}
                      className={"droppable-col"}
                    >
                      {data.items.map((el, index) => {
                        return(
                          <Draggable key={el.taskID} index={index} draggableId={`${el.taskID}`}>
                            {(provided, snapshot) => {
                              console.log(snapshot)
                              return(
                                <div
                                  className={`item ${snapshot.isDragging && "dragging"}`}
                                  ref={provided.innerRef}
                                  {...provided.draggableProps}
                                  {...provided.dragHandleProps}
                                >
                                  {el.task_description}
                                </div>
                              )
                            }}
                          </Draggable>
                        )
                      })}
                      {provided.placeholder}
                    </div>
                  )
                }}
              </Droppable>
            </div>
          )
        })}
      </DragDropContext>
      </div>
     
    </div>
    
  );
}

export default Task;