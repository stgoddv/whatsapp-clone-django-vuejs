
const mutations = {
  SET_ROOMS(state, rooms) {
    state.rooms = rooms;
  },
  SET_MESSAGES(state, messages) {
    state.messages = messages;
  },
  SET_USERS(state, users) {
    state.users = users;
  },
  PUSH_MESSAGES(state, messages) {
    state.messages = [...state.messages, ...messages];
  },
  ADD_MESSAGES_TO_ROOM(state, { messageId, roomId }) {
    const room = state.rooms.find(el => el.id === roomId);
    room.messages.push(messageId);
  },
  REORDER_ROOM_TO_TOP(state, { roomId }) {
    const oldPosition = state.rooms.findIndex(el => el.id === roomId);
    const tmp = state.rooms[oldPosition];
    state.rooms.splice(oldPosition, 1);
    state.rooms.splice(0, 0, tmp);
  }
};

export default mutations;
