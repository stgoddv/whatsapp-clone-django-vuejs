const state = {
  selectedRoom: null,
  rooms: {},
  users: {},
  room_messages: {},
  unreadMessages: {},

  // Update signals
  allReceived: {},
  allRead: {},

  // This uses map because key is uiid4
  sendingPool: new Map()
};

export default state;
