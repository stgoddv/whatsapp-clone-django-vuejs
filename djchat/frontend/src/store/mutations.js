import Vue from "vue";

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
        Vue.set(state.room_messages, element.room, [
          ...state.room_messages[element.room],
          element
        ]);
      } else {
        Vue.set(state.room_messages, element.room, [element]);
      }
    });
  },
  LINK_PAST_MESSAGES_TO_ROOM(state, { pastMessages, roomId }) {
    Vue.set(state.room_messages, roomId, [
      ...pastMessages,
      ...state.room_messages[roomId]
    ]);
  },
  SET_SELECTED_ROOM(state, roomId) {
    state.selectedRoom = roomId;
  }
};

export default mutations;
