<template>
  <div id="app">
    <window-size />
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
    <div>
      <router-view />
    </div>
  </div>
</template>

<script>
import WindowSize from "@/components/WindowSize.vue";
import { EventBus } from "@/eventBus";

export default {
  components: {
    WindowSize
  },
  methods: {
    initializeWebSocketSupport() {
      var _this = this;
      var chatSocket = new WebSocket(
        "ws://" + window.location.host + "/ws/notifications/"
      );
      chatSocket.onmessage = async function(e) {
        var data = JSON.parse(e.data);
        var message = data["message"];
        if (message === "update") {
          await _this.$store.dispatch("fetchUnreadMessages");
          await _this.$store.dispatch("fetchMessages");
          EventBus.$emit("update");
        } else if (message === "update_rooms") {
          _this.$store.dispatch("fetchRooms");
        } else if (message === "room_delete") {
          const { room_id } = data.data;
          if (_this.$store.state.selectedRoom === room_id) {
            _this.$store.commit("SET_SELECTED_ROOM", null);
          }
          _this.$store.commit("REMOVE_ROOM", room_id);
        } else if (message === "update_received") {
          _this.$store.dispatch("fetchReceivedInvitations");
        } else if (message === "update_sent") {
          _this.$store.dispatch("fetchSentInvitations");
        } else if (message === "writing") {
          EventBus.$emit("writing", data.data);
        } else if (message === "update_message") {
          const { kind, message_id } = data.data;
          if (kind === "all_received") {
            _this.$store.commit("MARK_MESSAGE_ALL_RECEIVED", message_id);
          } else if (kind === "all_read") {
            _this.$store.commit("MARK_MESSAGE_ALL_READ", message_id);
          }
        }
      };
      chatSocket.onclose = function() {
        console.error("Chat socket closed unexpectedly");
      };
    }
  },
  async created() {
    await this.$store.dispatch("fetchUserProfile");
    this.$store.dispatch("fetchSentInvitations");
    this.$store.dispatch("fetchReceivedInvitations");
    // First fetch older pending messages and then the recent ones
    await this.$store.dispatch("fetchRooms");
    await this.$store.dispatch("fetchUnreadMessages");
    await this.$store.dispatch("fetchMessages");
    await this.$store.dispatch("fetchRecentActivity");
    this.initializeWebSocketSupport();
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
