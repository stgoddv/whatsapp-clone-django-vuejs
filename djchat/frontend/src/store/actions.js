import axios from "@/backend";

// Put last_message value as the first in messages field
const preFormatRoom = (room) => {
  const { last_message, ...rest } = room;
  return { ...rest, messages: [last_message] };
};

const actions = {
  // fetchRecentActivity
  fetchRecentActivity({ commit }) {
    return new Promise((resolve, reject) => {
      axios.get("/api/v1/rooms/recents").then(response => {
        // Pre formatting of rooms
        response.data.rooms = response.data.rooms.map(element => {
          return preFormatRoom(element);
        });
        // Commits
        commit('SET_ROOMS', response.data.rooms);
        commit('SET_MESSAGES', response.data.messages);
        commit('SET_USERS', response.data.users);
        resolve(response);
      }).catch(error => reject(error));
    });
  },
  fetchMessages({ commit, state }) {
    return new Promise((resolve, reject) => {
      axios.get("/api/v1/messages/").then(response => {
        const messages = response.data.messages;
        const users = response.data.users;
        let rooms = response.data.rooms;

        // get or create users
        console.log(users);
        // get or create rooms
        console.log(rooms);
        console.log(state);

        // create messages
        commit('PUSH_MESSAGES', messages);
        messages.forEach(msg => {
          commit('ADD_MESSAGES_TO_ROOM', {
            messageId: msg.id,
            roomId: msg.room
          });
          // counter no leidos -> el gran tema no resuelto 
          // es que esto deberia estar en el back.
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
