<template>
  <div class="relative">
    <div v-if="!$store.state.selectedRoom" class="alert">
      <div
        class="select-none mt-6 border 
        border-teal-500 shadow rounded-lg py-3"
        style="background-color: rgba(255,255,255,0.6);"
      >
        <p class="px-3">Selecciona una conversación para empezar!</p>
      </div>
    </div>

    <div
      ref="messages"
      class="messages-section border rounded-lg border-teal-500 pb-2 chat scrollbar overflow-y-auto"
      style="min-height: 20rem; max-height: 25rem;"
      @scroll="onScroll"
    >
      <div v-if="$store.state.selectedRoom">
        <div
          v-if="fetchingMessages"
          class="py-1"
          style="background-color: rgba(255,255,255,0.7);"
        >
          <p class="text-sm">Loading older messages.</p>
        </div>
        <div v-for="message in messages" :key="message.id">
          <sent-message :message="message" v-if="message.is_owner" />
          <received-message :message="message" v-else />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SentMessage from "./SentMessage.vue";
import ReceivedMessage from "./ReceivedMessage.vue";

export default {
  data() {
    return {
      fetchingMessages: false,
      fixScrollToBottom: true,
      noMoreMessages: false
    };
  },
  components: {
    SentMessage,
    ReceivedMessage
  },
  methods: {
    scrollToBottom() {
      let sc = this.$refs["messages"];
      sc.scrollTo(0, sc.scrollHeight);
    },
    onScroll({ target: { scrollTop, clientHeight, scrollHeight } }) {
      if (scrollTop + clientHeight >= scrollHeight) {
        this.fixScrollToBottom = true;
      } else {
        this.fixScrollToBottom = false;
      }
      if (scrollTop < 50 && !this.fetchingMessages) {
        this.fetchPastMessages();
      }
    },
    fetchPastMessages() {
      if (!this.fetchingMessages && !this.noMoreMessages) {
        this.fetchingMessages = true;
        let roomId = this.$store.state.selectedRoom;
        let firstMessageId = this.messages ? this.messages[0].id : null;
        this.$store
          .dispatch("fetchPastMessages", {
            firstMessageId,
            roomId
          })
          .then(response => {
            this.fetchingMessages = false;
            if (!response.data.messages.length) {
              this.noMoreMessages = true;
            }
          })
          .catch(() => {
            this.fetchingMessages = false;
          });
      }
    }
  },
  mounted() {
    this.scrollToBottom();
  },
  computed: {
    selectedRoom() {
      return this.$store.state.selectedRoom;
    },
    messages() {
      let selectedRoom = this.$store.state.selectedRoom;
      return this.$store.state.room_messages[selectedRoom];
    }
  },
  watch: {
    selectedRoom() {
      this.fetchingMessages = false;
      this.noMoreMessages = false;
      if (!this.messages || this.messages.length < 3) {
        this.fetchPastMessages();
      }
      setTimeout(() => this.scrollToBottom(), 10);
    },
    messages() {
      this.$nextTick(() => {
        if (this.fixScrollToBottom) {
          this.scrollToBottom();
        }
      });
    }
  }
};
</script>

<style scoped>
.chat {
  background-image: url("~@/assets/imgs/main-bg.jpg");
  background-repeat: no-repeat;
  background-size: cover;
}

.alert {
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -50%);
  -moz-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  position: absolute;
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
