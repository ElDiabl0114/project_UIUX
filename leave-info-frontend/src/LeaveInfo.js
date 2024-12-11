import React, { useState } from 'react';
import axios from 'axios';

const LeaveInfo = () => {
  const [employeeId, setEmployeeId] = useState('');
  const [leaveInfo, setLeaveInfo] = useState(null);

  const handleInputChange = (e) => {
    setEmployeeId(e.target.value);
  };

  const handleFindLeaves = async () => {
    try {
      const response = await axios.get(`http://localhost:5000/leave-info/${employeeId}`);
      setLeaveInfo(response.data);
    } catch (error) {
      setLeaveInfo(null);
      alert(error.response?.data?.error || 'An error occurred');
    }
  };

  return (
    <div>
      <h1>Leave Information</h1>
      <input
        type="number"
        placeholder="Enter Employee ID"
        value={employeeId}
        onChange={handleInputChange}
      />
      <button onClick={handleFindLeaves}>Find Leaves</button>

      {leaveInfo && (
        <div>
          <h2>Employee Info</h2>
          <p>Position: {leaveInfo.position}</p>
          <p>Total Leaves: {leaveInfo.totalLeaves}</p>
          <p>Used Leaves: {leaveInfo.usedLeaves}</p>
          <p>Remaining Leaves: {leaveInfo.remainingLeaves}</p>
        </div>
      )}
    </div>
  );
};

export default LeaveInfo;
