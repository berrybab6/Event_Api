import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getEvents } from '../../actions/events';

export class Events extends Component {
  static propTypes () {
    events: PropTypes.array.isRequired;
  }

  // static propTypes = {
  //   events: PropTypes.array.isRequired,
  // };

  componentDidMount(){
    this.props.getEvents();
  }

  render() {
    return (
      <Fragment>
       <h1>Events</h1>
       {/* <div> {this.props.events[0]}</div> */}
       <table className= "table table-striped">
         <thead>
          <tr>
              <th>Title</th>
              <th>Description</th>
              <th>Seat Limit</th>
              <th>Begins_on</th>
              <th>ends_on</th>
              <th>Deadline</th>
              <th  />
          </tr>
         </thead>

         <tbody>
          <tr >
             <td>NAme</td>
               <td>{ this.props.events}</td>  
                <td>description</td>
               
              <td>event.seat_limit</td>
              <td>event.begins_on</td>
              <td>event.ends_on</td>
              <td>event.deadline</td>
              <td><button className="btn btn-danger btn-sm">
                Delete
              </button></td>
              </tr>   
            {/* { this.props.events.map((event) => (
              <tr key={event.id}>
              <td>{event.id}</td>
              <td>{event.description}</td>
              <td>{event.seat_limit}</td>
              <td>{event.begins_on}</td>
              <td>{event.ends_on}</td>
              <td>{event.deadline}</td>
              <td><button className="btn btn-danger btn-sm">
                Delete
              </button></td>
              </tr>
            ))} */}
         </tbody>
       </table>
        </Fragment>
    )
  }
}
//  Events.propTypes = {
//   events: PropTypes.array(PropTypes.object).isRequired
// };
const mapStateToProps = state =>({
  events: state.events.events
});

export default connect(mapStateToProps, {getEvents})(Events);
