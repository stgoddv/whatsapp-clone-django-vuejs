
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
  },
  SET_SELECTED_ROOM(state, roomId) {
    state.selectedRoom = roomId;
  }
};

export default mutations;
