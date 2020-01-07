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
  LINK_MESSAGES_TO_ROOM(state, messages) {
    messages.forEach(element => {
      let front_key = element.front_key;
      if (state.sendingStatus.has(front_key)) {
        // Pending sending status
        let message = state.sendingStatus.get(front_key);
        state.sendingStatus.delete(front_key);
        delete message.sending;
        Object.assign(message, element);
      } else {
        if (element.room in state.room_messages) {
          Vue.set(state.room_messages, element.room, [
            ...state.room_messages[element.room],
            element
          ]);
        } else {
          Vue.set(state.room_messages, element.room, [element]);
        }
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
  },
  ADD_MESSAGE_TO_SENDING(state, message) {
    state.sendingStatus.set(message.front_key, message);
  },
  ADD_UNREAD_MESSAGES(state, messages) {
    state.unreadMessages = {};
    messages.forEach(element => {
      Vue.set(state.unreadMessages, element.id, element.room);
    });
  },
  REMOVE_MESSAGE_FROM_UNREAD(state, message_id) {
    if (message_id in state.unreadMessages) {
      Vue.delete(state.unreadMessages, message_id);
    }
  }
};

export default mutations;
