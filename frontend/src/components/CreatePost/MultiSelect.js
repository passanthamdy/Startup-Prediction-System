import * as React from "react";
import * as ReactDOM from "react-dom";
import { MultiSelect } from "@progress/kendo-react-dropdowns";

const Cat = [
  "Baseball",
  "Basketball",
  "Cricket",
  "Field Hockey",
  "Football",
  "Table Tennis",
  "Tennis",
  "Volleyball",
];

class Multiselect extends React.Component {
  state = { value: [] };

  onChange = (event) => {
    this.setState({
      value: [...event.target.value],
    });
  };

  render() {
    return (
      <div className="example-wrapper">
        <div>
          <div>Favorite sports:</div>
          <MultiSelect
            data={Cat}
            onChange={this.onChange}
            value={this.state.value}
          />
        </div>
      </div>
    );
  }
}

export default Multiselect