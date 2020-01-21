import axios from "@/backend";

const actions = {
  syncDB({ commit }, { rooms, users, messages }) {
    commit("SET_ROOMS", rooms);
    commit("SET_USERS", users);
    commit("LINK_MESSAGES_TO_ROOM", messages);
  },
  fetchRooms({ dispatch }) {
    return new Promise((resolve, reject) => {
      axios
        .get("/api/v1/rooms/")
        .then(response => {
          dispatch("syncDB", {
            rooms: response.data.rooms,
            messages: response.data.messages,
            users: response.data.users
          });
          resolve(response);
        })
        .catch(error => reject(error));
    });
  },
  fetchRecentActivity({ dispatch }) {
    return new Promise((resolve, reject) => {
      axios
        .get("/api/v1/rooms/recents")
        .then(response => {
          dispatch("syncDB", {
            rooms: response.data.rooms,
            messages: response.data.messages,
            users: response.data.users
          });
          resolve(response);
        })
        .catch(error => reject(error));
    });
  },
  fetchMessages({ dispatch }) {
    return new Promise((resolve, reject) => {
      axios
        .get("/api/v1/messages/")
        .then(response => {
          dispatch("syncDB", {
            rooms: response.data.rooms,
            messages: response.data.messages,
            users: response.data.users
          });
          resolve(response);
        })
        .catch(error => reject(error));
    });
  },
  fetchPastMessages({ commit }, { firstMessageId, roomId }) {
    let endpoint = firstMessageId
      ? `/api/v1/messages/${roomId}?offset=${firstMessageId}`
      : `/api/v1/messages/${roomId}`;
    return new Promise((resolve, reject) => {
      axios
        .get(endpoint)
        .then(response => {
          commit("SET_USERS", response.data.users);
          commit("LINK_PAST_MESSAGES_TO_ROOM", {
            pastMessages: response.data.messages,
            roomId
          });
          resolve(response);
        })
        .catch(error => reject(error));
    });
  },
  sendMessage(none, { room, body, front_key }) {
    let payload = {
      room,
      body,
      ...(front_key ? { front_key } : {})
    };
    return new Promise((resolve, reject) => {
      axios
        .post("/api/v1/messages/", payload)
        .then(response => {
          resolve(response);
        })
        .catch(error => reject(error));
    });
  },
  markMessageAsRead({ commit }, message_id) {
    return new Promise((resolve, reject) => {
      axios
        .post(`/api/v1/messages/unread?message_id=${message_id}`)
        .then(response => {
          commit("REMOVE_MESSAGE_FROM_UNREAD", message_id);
          resolve(response);
        })
        .catch(error => reject(error));
    });
  },
  fetchUnreadMessages({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .get("/api/v1/messages/unread")
        .then(response => {
          commit("ADD_UNREAD_MESSAGES", response.data.messages);
          resolve(response);
        })
        .catch(error => reject(error));
    });
  },
  postWriting(none, room_id) {
    return new Promise((resolve, reject) => {
      axios
        .post(`api/v1/rooms/${room_id}/writing`)
        .then(response => {
          resolve(response);
        })
        .catch(error => reject(error));
    });
  },
  markRoomAsRead({ commit }, room_id) {
    return new Promise((resolve, reject) => {
      axios
        .post(`/api/v1/rooms/${room_id}/read`)
        .then(response => {
          commit("REMOVE_ROOM_MESSAGES_FROM_UNREAD", room_id);
          resolve(response);
        })
        .catch(error => reject(error));
    });
  },
  fetchSentInvitations({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .get("/api/v1/friends/requests/sent")
        .then(response => {
          commit("SET_SENT_INVITATIONS", response.data);
          resolve(response);
        })
        .catch(error => reject(error));
    });
  },
  getUserIdFromEmail(none, email) {
    return new Promise((resolve, reject) => {
      axios
        .get(`/api/v1/users?email=${email}`)
        .then(response => {
          resolve(response);
        })
        .catch(error => reject(error));
    });
  },
  addFriend({ commit }, userId) {
    return new Promise((resolve, reject) => {
      axios
        .post(`/api/v1/friends/add/${userId}`)
        .then(response => {
          commit("SET_SENT_INVITATIONS", response.data);
          resolve(response);
        })
        .catch(error => reject(error));
    });
  },
  cancelFriendRequest({ commit }, invitationId) {
    return new Promise((resolve, reject) => {
      axios
        .post(`/api/v1/friends/requests/cancel/${invitationId}`)
        .then(response => {
          commit("SET_SENT_INVITATIONS", response.data);
          resolve(response);
        })
        .catch(error => reject(error));
    });
  },
  fetchReceivedInvitations({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .get("/api/v1/friends/requests/received")
        .then(response => {
          commit("SET_RECEIVED_INVITATIONS", response.data);
          resolve(response);
        })
        .catch(error => reject(error));
    });
  },
  rejectFriendRequest({ commit }, invitationId) {
    return new Promise((resolve, reject) => {
      axios
        .post(`/api/v1/friends/requests/reject/${invitationId}`)
        .then(response => {
          commit("SET_RECEIVED_INVITATIONS", response.data);
          resolve(response);
        })
        .catch(error => reject(error));
    });
  },
  acceptFriendRequest({ commit }, invitationId) {
    return new Promise((resolve, reject) => {
      axios
        .post(`/api/v1/friends/requests/accept/${invitationId}`)
        .then(response => {
          commit("SET_RECEIVED_INVITATIONS", response.data);
          resolve(response);
        })
        .catch(error => reject(error));
    });
  },
  deleteRoom(none, roomId) {
    return new Promise((resolve, reject) => {
      axios
        .post(`/api/v1/rooms/${roomId}/delete`)
        .then(response => {
          resolve(response);
        })
        .catch(error => reject(error));
    });
  },
  fetchUserProfile({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .get("/api/v1/me")
        .then(response => {
          commit("SET_USER_PROFILE", response.data);
          resolve(response);
        })
        .catch(error => reject(error));
    });
  },
  patchUserProfile({ commit }, payload) {
    return new Promise((resolve, reject) => {
      axios
        .patch("/api/v1/me", payload)
        .then(response => {
          commit("SET_USER_PROFILE", response.data);
          resolve(response);
        })
        .catch(error => reject(error));
    });
  }
};

export default actions;
