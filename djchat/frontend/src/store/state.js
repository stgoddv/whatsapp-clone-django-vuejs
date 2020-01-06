const state = {
  selectedRoom: null,
  rooms: {},
  users: {},
  room_messages: {},
  sendingStatus: new Map(),
  unreadMessages: new Map(),
  unreadByRoom: new Map()
};

export default state;
