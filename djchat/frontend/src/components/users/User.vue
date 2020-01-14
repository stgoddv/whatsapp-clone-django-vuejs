<template>
  <div
    class="user-row border-b px-3 py-3 select-none
    cursor-pointer hover:shadow hover:bg-green-200"
    style="transition: box-shadow 0.3s, background-color 0.3s;"
    :class="{ 'bg-green-200': isSelected }"
  >
    <div class="flex items-center">
      <!-- <img
        class="w-10 h-10 rounded-full mr-4 mr-5 ml-2"
        src="@/assets/avatars/jonathan.jpg"
        alt="Avatar of Jonathan Reinink"
      /> -->
      <div
        class="avatar-circle flex-none mr-3"
        :style="
          `background-color: rgb(${getColor.red},${getColor.green},${getColor.blue});`
        "
      >
        {{ room.group_name.charAt(0).toUpperCase() }}
      </div>
      <div class="text-sm w-full">
        <div class="flex justify-between">
          <p class="text-gray-900 text-left">{{ room.group_name }}</p>
          <p class="text-gray-600 text-xs text-left">{{ lastActivity }}</p>
        </div>

        <div class="body-section flex items-center">
          <!-- Last message -->
          <div class="flex-1" v-if="lastMessage">
            <p
              v-if="whosWriting"
              class="text-gray-600 text-md text-left italic"
            >
              {{ whosWriting }} is writing...
            </p>
            <p v-else class="text-gray-600 text-md text-left">
              {{ truncateString(lastMessage.body, 35) }}
            </p>
          </div>

          <!-- Unread messages -->
          <div class="flex-none ml-2">
            <p
              v-if="unreadMessages && unreadMessages != 0 && !isSelected"
              class="circle mx-1"
            >
              {{ unreadMessages }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import dateFormat from "dateformat";

import { colorOffsets, getHash } from "@/global/variables.js";
import { EventBus } from "@/eventBus";

export default {
  data() {
    return {
      whosWriting: ""
    };
  },
  methods: {
    truncateString(str, num) {
      if (str.length <= num) {
        return str;
      }
      return str.slice(0, num) + "...";
    }
  },
  computed: {
    getColor() {
      let username = this.room.group_name;
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
    lastActivity() {
      let last_activity = dateFormat(
        new Date(this.room.last_activity),
        "hh:MM"
      );
      return last_activity;
    },
    lastMessage() {
      let roomMessages = this.$store.state.roomMessages[this.room.id];
      let lastMessage = null;
      if (roomMessages && roomMessages.length) {
        lastMessage = roomMessages[roomMessages.length - 1];
      }
      return lastMessage;
    },
    unreadMessages() {
      let unreadMessages = Object.values(this.$store.state.unreadMessages);
      return unreadMessages.filter(el => el === this.room.id).length;
    }
  },
  created() {
    EventBus.$on("writing", data => {
      if (this.room.id === data.room_id) {
        let user = this.$store.state.users[data.user_id];
        this.whosWriting = user.username;
        setTimeout(() => {
          this.whosWriting = "";
        }, 10000);
      }
    });
  },
  watch: {
    lastMessage() {
      this.whosWriting = "";
    },
    whosWriting(value) {
      this.$emit("whosWriting", { value, room: this.room.id });
    }
  },
  props: {
    isSelected: {
      type: Boolean,
      default: false
    },
    room: {
      type: Object,
      required: true
    }
  }
};
</script>

<style scoped>
.circle {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  font-size: 12px;
  color: #fff;
  line-height: 20px;
  text-align: center;
  background: #38b2ac;
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
</style>
