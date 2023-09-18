import React from 'react';

import './App.css';
// import ReactDOM from "react-dom";
class App extends React.Component {
  constructor() {
    super();
    this.state = {
      data: "",
      inputValue: "",
      responseMessage: "",
    };
  }

  async componentDidMount() {
    try {
      const response = await fetch(`http://localhost:3000/api/hello`);
      const json = await response.json();
      this.setState({ data: json });
    } catch (error) {
      console.log(error);
    }

  }

  handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://localhost:3000/api/world", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ input: this.state.inputValue }),
      });

      if (response.ok) {
        const data = await response.json();
        this.setState({ responseMessage: data.message });

      } else {
        console.error("Failed to send POST request.");
      }
    } catch (error) {
      console.error("Error sending POST request:", error);
    }
  };

  handleInputChange = (e) => {
    this.setState({ inputValue: e.target.value });
  };

  render() {
    return (
      <div>
        <h1>
          {this.state.data.toString()}
        </h1>
        <h1>POST Request Example</h1>
        <form onSubmit={this.handleSubmit}>
          <label>
            Enter something:
            <input
              type="text"
              value={this.state.inputValue}
              onChange={this.handleInputChange}
            />
          </label>
          <button type="submit">Submit</button>
        </form>
        {this.state.responseMessage && (
          <div>
            <p>Response from server:</p>
            <p>{this.state.responseMessage}</p>

          </div>

        )}
      </div>
    );
  }
}


export default App;

