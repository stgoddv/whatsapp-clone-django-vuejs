<template>
  <div
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
  }
};
</script>