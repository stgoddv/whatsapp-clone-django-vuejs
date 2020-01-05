import axios from "@/backend";

const actions = {
  fetchRecentActivity({ commit }) {
    return new Promise((resolve, reject) => {
      axios.get("/api/v1/rooms/recents").then(response => {
        // Rooms pre formatting
        response.data.rooms = response.data.rooms.map(element => {
          const { last_message, ...rest } = element;
          return { ...rest, messages: [last_message] };
        });
        // Commits
        commit('SET_MESSAGES', response.data.messages);
        commit('SET_USERS', response.data.users);
        commit('SET_ROOMS', response.data.rooms);
        resolve(response);
      }).catch(error => reject(error));
    });
  },
  fetchMessages({ commit }) {
    return new Promise((resolve, reject) => {
      axios.get("/api/v1/messages/").then(response => {
        const messages = response.data;
        commit('PUSH_MESSAGES', messages);
        messages.forEach(msg => {
          // get or create room
          // por ahora get DEBUG
          commit('ADD_MESSAGES_TO_ROOM', {
            messageId: msg.id,
            roomId: msg.room
          });
          // counter no leidos -> el gran tema no resuelto 
          // es que esto deberia estar en el back.
          // que suba en panel de conversaciones a primer puesto
          commit('REORDER_ROOM_TO_TOP', {
            roomId: msg.room
          });
        });
        resolve(response);
      }).catch(error => reject(error));
    });
  }
};

export default actions;
