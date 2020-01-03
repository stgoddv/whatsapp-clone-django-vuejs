<template>
  <div
    ref="messages"
    class="messages-section border rounded-lg border-teal-500 py-2 chat scrollbar overflow-y-auto"
    style="min-height: 20rem; max-height: 25rem;"
  >
    <received-message />
    <sent-message />
    <received-message />
    <sent-message />
    <received-message />
    <sent-message />
    <received-message />
    <sent-message />
    <received-message />
    <sent-message />
  </div>
</template>

<script>
import SentMessage from "./SentMessage.vue";
import ReceivedMessage from "./ReceivedMessage.vue";

export default {
  components: {
    SentMessage,
    ReceivedMessage
  },
  mounted() {
    let sc = this.$refs["messages"];
    sc.scrollTo(0, sc.scrollHeight);
  }
};
</script>

<style scoped>
.chat {
  background-image: url("~@/assets/imgs/main-bg.jpg");
  background-repeat: no-repeat;
  background-size: cover;
}

/* Scrollbar */
/* width */
.scrollbar::-webkit-scrollbar {
  width: 5px;
}

/* Track */
.scrollbar::-webkit-scrollbar-track {
  background: #f1f1f1;
}

/* Handle */
.scrollbar::-webkit-scrollbar-thumb {
  background: #888;
}

/* Handle on hover */
.scrollbar::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>