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
      if (state.sendingPool.has(front_key)) {
        // Pending sending status
        let message = state.sendingPool.get(front_key);
        state.sendingPool.delete(front_key);
        delete message.sending;
        Object.assign(message, element);
      } else {
        if (element.room in state.roomMessages) {
          Vue.set(state.roomMessages, element.room, [
            ...state.roomMessages[element.room],
            element
          ]);
        } else {
          Vue.set(state.roomMessages, element.room, [element]);
        }
      }
    });
  },
  LINK_PAST_MESSAGES_TO_ROOM(state, { pastMessages, roomId }) {
    Vue.set(state.roomMessages, roomId, [
      ...pastMessages,
      ...state.roomMessages[roomId]
    ]);
  },
  SET_SELECTED_ROOM(state, roomId) {
    state.selectedRoom = roomId;
  },
  ADD_MESSAGE_TO_SENDING(state, message) {
    state.sendingPool.set(message.front_key, message);
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
  },
  REMOVE_ROOM_MESSAGES_FROM_UNREAD(state, room_id) {
    for (let message_id in state.unreadMessages) {
      if (state.unreadMessages[message_id] === room_id) {
        Vue.delete(state.unreadMessages, message_id);
      }
    }
  },
  MARK_MESSAGE_ALL_RECEIVED(state, message_id) {
    Vue.set(state.allReceived, message_id, true);
  },
  MARK_MESSAGE_ALL_READ(state, message_id) {
    Vue.set(state.allRead, message_id, true);
  }
};

export default mutations;
