import React from "react";

const AddTrade = (props) => {
  const addTrade = async (props) => {
    const apiRes = await fetch("localhost:8080/addtrade");

    const resJson = await apiRes.json();

    return;
  };

  return (
    <div>
      <div>Date</div>
      <input type="text" value={props.date} />
      <div>Action</div>
      <input type="text" value={props.action} />
      <div>Symbol</div>
      <input type="text" value={props.symbol} />
      <div>Company</div>
      <input type="text" value={props.company} />
      <div>Quantity</div>
      <input type="text" value={props.quantity} />
      <div>Share Price</div>
      <input type="text" value={props.sharePrice} />
      <div>Fees</div>
      <input type="text" value={props.fees} />
      <div>Total Cost</div>
      <input type="text" value={props.totalCost} />
      <button onclick={addTrade(props)}>Submit</button>
    </div>
  );
};

export default AddTrade;
