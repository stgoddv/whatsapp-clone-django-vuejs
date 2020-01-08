const state = {
  // Frontend selected room
  selectedRoom: null,

  // Db sync
  rooms: {},
  users: {},
  roomMessages: {},

  // Messages pool
  receivedMessages: {},
  unreadMessages: {},

  // Update signals
  allReceived: {},
  allRead: {},

  // Sending messages pool
  sendingPool: new Map()
};

export default state;
