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
      }).catch(error => reject(error));
    });
  }
};

export default actions;
