import React from 'react';

class WeatherCard extends React.Component {

    state = {
        Temperature : 0,
        Humidity : 0
    };

    componentDidMount() {
      fetch("/data")
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              Temperature: result.Temperature,
              Humidity: result.Humidity
            });
          },
          (error) => {
            this.setState({
              error
            });
          }
        )
    }

    render() {
      return  <div>
                  <div>Temperature : {this.state.Temperature}</div>
                  <div>Humidity : {this.state.Humidity}</div>
              </div>;
    }
  }

export default WeatherCard; 