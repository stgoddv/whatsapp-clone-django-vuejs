import axios from "@/backend";

const actions = {
  syncDB({ commit }, { rooms, users, messages }) {
    commit('SET_ROOMS', rooms);
    commit('SET_MESSAGES', messages);
    commit('SET_USERS', users);
    commit('LINK_MESSAGES_TO_ROOM', messages);
  },
  fetchRecentActivity({ dispatch }) {
    return new Promise((resolve, reject) => {
      axios.get("/api/v1/rooms/recents").then(response => {
        dispatch('syncDB', {
          rooms: response.data.rooms,
          messages: response.data.messages,
          users: response.data.users
        });
        resolve(response);
      }).catch(error => reject(error));
    });
  },
  fetchMessages({ dispatch }) {
    return new Promise((resolve, reject) => {
      axios.get("/api/v1/messages/").then(response => {
        dispatch('syncDB', {
          rooms: response.data.rooms,
          messages: response.data.messages,
          users: response.data.users
        });
        resolve(response);
      }).catch(error => reject(error));
    });
  }
};

export default actions;
