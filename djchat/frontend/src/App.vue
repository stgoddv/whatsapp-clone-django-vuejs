<template>
  <div id="app">
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
import { EventBus } from "@/eventBus";

export default {
  methods: {
    initializeWebSocketSupport() {
      var _this = this;
      var chatSocket = new WebSocket(
        "ws://" + window.location.host + "/ws/notifications/"
      );
      chatSocket.onmessage = function(e) {
        var data = JSON.parse(e.data);
        var message = data["message"];
        if (message === "update") {
          _this.$store.dispatch("fetchMessages");
        }
        EventBus.$emit(message);
      };
      chatSocket.onclose = function() {
        console.error("Chat socket closed unexpectedly");
      };
    }
  },
  async created() {
    // First fetch older pending messages and then the recent ones
    await this.$store.dispatch("fetchMessages");
    await this.$store.dispatch("fetchRecentActivity");
    await this.$store.dispatch("fetchUnreadMessages");
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
