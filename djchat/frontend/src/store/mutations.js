
import Vue from 'vue';

const mutations = {
  SET_ROOMS(state, rooms) {
    rooms.forEach(element => {
      Vue.set(state.rooms, element.id, element);
    });
  },
  SET_USERS(state, users) {
    users.forEach(element => {
      Vue.set(state.users, element.id, element);
    });
  },
  SET_MESSAGES(state, messages) {
    messages.forEach(element => {
      Vue.set(state.messages, element.id, element);
    });
  },
  LINK_MESSAGES_TO_ROOM(state, messages) {
    messages.forEach(element => {
      if (element.room in state.room_messages) {
        state.room_messages[element.room].push(element);
      } else {
        state.room_messages[element.room] = [element];
      }
    });
  }
  // PUSH_MESSAGES(state, messages) {
  //   state.messages = [...state.messages, ...messages];
  // },
  // ADD_MESSAGES_TO_ROOM(state, { messageId, roomId }) {
  //   const room = state.rooms.find(el => el.id === roomId);
  //   room.messages.push(messageId);
  // },
  // REORDER_ROOM_TO_TOP(state, { roomId }) {
  //   const oldPosition = state.rooms.findIndex(el => el.id === roomId);
  //   const tmp = state.rooms[oldPosition];
  //   state.rooms.splice(oldPosition, 1);
  //   state.rooms.splice(0, 0, tmp);
  // }
};

export default mutations;
