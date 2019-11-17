import React,{Component} from 'react';
import logo from './logo.svg';
import './App.css';
import Person from './Person/Person';
class App extends Component {

    state ={ 
      person:[
        {age:30},
        {age:50},
        {age:70}
      ]
    }

   switchNameHandler = (newAge) => {
    console.log("was clicked");
     var tmp = this.state.person[0].age
    //DON'T DO THIS :state.person[0].age=state.person[1].age
    //state.person[1].age = tmp      
    this.setState({
      person:[
        {age:newAge},
        {age:30},
        {age:70}
      ]
    }) 
  }
  render () {
  return (
    <div className="App">
     <h1>Hi i'm a react app</h1>
     <button onClick={this.switchNameHandler.bind(this,"erere")}>Switch Name </button>
     <Person age={this.state.person[0].age}/>
     <Person age={this.state.person[1].age } click={this.switchNameHandler.bind(this,33)}>My Hobbies is racing !!!</Person>
      <Person age={this.state.person[2].age} click={this.switchNameHandler}/>
    </div>     
  );}
  // The code on the comment down bellow this what js compile in the top the code 
  //return React.createElement('div',{className :'App'},React.createElement('input',null,'i \'m the child'));
}

export default App;
