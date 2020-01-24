<template>
  <div class="relative">
    <div
      class="flex items-center justify-between profile-panel border-b"
      style="height: 10vh;"
    >
      <!-- Group Avatar -->
      <div class="avatar-container flex">
        <!-- Optional slot -->
        <slot></slot>

        <div
          v-if="selectedRoom"
          class="flex items-center"
          @click="$emit('profile-sidenav')"
        >
          <!-- Avatar -->
          <div
            class="avatar-circle flex-none mx-3 select-none cursor-pointer hover:shadow-md"
            :style="
              `background-color: rgb(${getColor.red},${getColor.green},${getColor.blue}); transition: box-shadow 0.3s;`
            "
          >
            {{
              $store.state.rooms[selectedRoom].group_name
                .charAt(0)
                .toUpperCase()
            }}
          </div>

          <!-- Profile Name -->
          <p class="cursor-pointer">
            {{ $store.state.rooms[selectedRoom].group_name }}
          </p>
        </div>
      </div>

      <!-- Menu Icon -->
      <Menu />
    </div>

    <!-- Fallback when no room is selected yet -->
    <div v-if="!$store.state.selectedRoom" class="alert">
      <div class="select-none mt-6">
        <!-- Chat Icon -->
        <i
          class="material-icons mb-4 bg-white p-6 
        shadow-lg rounded-full"
          style="font-size: 48px;"
          >chat_bubble_outline</i
        >

        <!-- Message -->
        <p class=" py-2 px-4 bg-white shadow-lg rounded-full">
          Talk to a Friend!
        </p>
      </div>
    </div>

    <!-- Messages window -->
    <div
      ref="messages"
      class="messages-section chat scrollbar overflow-y-auto overflow-x-hidden border-b"
      style="height: 75vh;"
      @scroll="onScroll"
    >
      <div v-if="$store.state.selectedRoom">
        <!-- Fetching older messages alert -->
        <div
          v-if="fetchingMessages"
          class="py-1"
          style="background-color: rgba(255,255,255,0.7);"
        >
          <p class="text-sm">Loading older messages.</p>
        </div>

        <!-- Messages section -->
        <div class="mx-auto max-w-3xl mb-3 px-1">
          <div v-for="message in messages" :key="message.id">
            <!-- Sent or received -->
            <sent-message :message="message" v-if="message.is_owner" />
            <received-message :message="message" v-else />
          </div>
        </div>

        <!-- Fetching older messages alert -->
        <div
          v-if="newMessagesReceived"
          class="py-1 sticky flex justify-center select-none"
          style="background-color: rgba(255,255,255,0.7);"
        >
          <p class="text-sm mx-1">New messages received</p>
          <p
            @click="scrollToBottom()"
            class="text-sm mx-1 text-blue-500 
            cursor-pointer font-medium hover:font-semibold"
          >
            (go to bottom)
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Menu from "@/components/Menu.vue";
import SentMessage from "./SentMessage.vue";
import ReceivedMessage from "./ReceivedMessage.vue";

import { colorOffsets, getHash } from "@/global/variables.js";

export default {
  data() {
    return {
      fetchingMessages: false,
      fixScrollToBottom: true,
      noMoreMessages: false,
      newMessagesReceived: false,
      showContext: false
    };
  },
  components: {
    SentMessage,
    ReceivedMessage,
    Menu
  },
  methods: {
    scrollToBottom() {
      let sc = this.$refs["messages"];
      sc.scrollTo(0, sc.scrollHeight);
    },
    onScroll({ target: { scrollTop, clientHeight, scrollHeight } }) {
      if (scrollTop + clientHeight >= scrollHeight) {
        this.fixScrollToBottom = true;
        this.newMessagesReceived = false;
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
    },
    hasUnreadMessagesInRoom() {
      return Object.values(this.$store.state.unreadMessages).includes(
        this.selectedRoom
      );
    }
  },
  mounted() {
    this.scrollToBottom();
  },
  computed: {
    getColor() {
      let username = this.$store.state.rooms[this.selectedRoom].group_name;
      let { red, green, blue } = colorOffsets;
      red = (getHash(username) + red) ** 2 % 256;
      green = (getHash(username) + green) ** 2 % 256;
      blue = (getHash(username) + blue) ** 2 % 256;
      return {
        red,
        green,
        blue
      };
    },
    selectedRoom() {
      return this.$store.state.selectedRoom;
    },
    messages() {
      let selectedRoom = this.$store.state.selectedRoom;
      return this.$store.state.roomMessages[selectedRoom];
    }
  },
  watch: {
    selectedRoom() {
      setTimeout(() => this.scrollToBottom(), 10);
      this.fetchingMessages = false;
      this.noMoreMessages = false;
      if (!this.messages || this.messages.length < 8) {
        this.fetchPastMessages();
      }
      if (this.hasUnreadMessagesInRoom()) {
        this.$store.dispatch("markRoomAsRead", this.selectedRoom);
      }
    },
    messages() {
      this.$nextTick(() => {
        if (this.fixScrollToBottom) {
          this.scrollToBottom();
        }
      });
      if (!this.fixScrollToBottom && !this.fetchingMessages) {
        this.newMessagesReceived = true;
      }
    }
  }
};
</script>

<style scoped>
div.sticky {
  position: -webkit-sticky; /* Safari */
  position: sticky;
  bottom: 0;
}

.chat {
  background-image: url("~@/assets/imgs/main-bg.png");
  background-repeat: repeat;
}

.alert {
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -50%);
  -moz-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  position: absolute;
}

.avatar-circle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  font-size: 25px;
  color: #fff;
  line-height: 40px;
  text-align: center;
  font-weight: 600;
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
