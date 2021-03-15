import React, { Component } from 'react';
import { connect } from 'react-redux';
import { addEvent } from '../../actions/events';
import PropTypes from 'prop-types';

export class Forms extends Component {
  state = {
    title: '';
    description: '';
    seat_limit: 0;
  }

  static propTypes (){
    addEvent: PropTypes.func.isRequired;
  }

  // onChange = (e) => this.setState({ [e.target.name]: e.target.value });

  // onSubmit = (e) => {
  //   e.preventDefault();
  //   const { title, description, seat_limit } = this.state;
  //   const event = { title, description, seat_limit };
  //   this.props.addEvent(event);
  //   this.setState({
  //     title: '',
  //     description: '',
  //     seat_limit: 0,
  //   });
  // };

  render() {
    const { title, description, seat_limit } = this.state;

    return (
      <div className="card card-body mt-4 mb-4">
        <h2>Add Event</h2>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>Title</label>
            <input
              className="form-control"
              type="text"
              name="title"
              onChange={this.onChange}
              value={title}
            />
          </div>
          <div className="form-group">
            <label>Description</label>
            <input
              className="form-control"
              type="text"
              name="description"
              onChange={this.onChange}
              value={description}
            />
          </div>
          <div className="form-group">
            <label>seat_limit</label>
            <textarea
              className="form-control"
              type="number"
              name="seat_limit"
              onChange={this.onChange}
              value={seat_limit}
            />
          </div>
          <div className="form-group">
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </div>
        </form>
      </div>
      
    )
  }
}

//export default Forms;
export default connect(null, { addEvent })(Forms);

