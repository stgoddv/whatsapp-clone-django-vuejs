<template>
  <div class="flex">
    <div class="received-message max-w-md">
      <div class="shadow-md border rounded-lg mx-2 my-2 px-4 relative bg-white">
        <!-- Message header -->
        <div class="flex justify-between py-1 mt-1">
          <p
            class="text-xs font-bold"
            :style="
              `color: rgb(${getColor.red}, ${getColor.green}, ${getColor.blue});`
            "
          >
            {{ getUser.username }}
          </p>
          <p class="text-xs text-gray-600 ml-3">~{{ getUser.email }}</p>
        </div>

        <!-- Message body -->
        <div class="mb-2">
          <p class="text-left mr-8">{{ message.body }}</p>
        </div>

        <!-- Time data -->
        <div class="absolute" style="right: 10px; bottom: 5px;">
          <p class="text-xs text-gray-600">{{ time }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import dateFormat from "dateformat";

import { colorOffsets, getHash } from "@/global/variables.js";

export default {
  props: {
    message: {
      type: Object,
      required: true
    }
  },
  computed: {
    time() {
      return dateFormat(new Date(this.message.timestamp), "hh:MM");
    },
    getUser() {
      let users = Object.values(this.$store.state.users);
      let user = users.find(el => el.id === this.message.author);
      return user;
    },
    getColor() {
      let username = this.getUser.username;
      let { red, green, blue } = colorOffsets;
      red = (getHash(username) + red) ** 2 % 256;
      green = (getHash(username) + green) ** 2 % 256;
      blue = (getHash(username) + blue) ** 2 % 256;
      return {
        red,
        green,
        blue
      };
    }
  },
  methods: {
    markMessageAsRead() {
      setTimeout(() => {
        // Timeout to avoid race condition with markRoomAsRead
        if (this.message.id in this.$store.state.unreadMessages) {
          this.$store.dispatch("markMessageAsRead", this.message.id);
        }
      }, 100);
    }
  },
  created() {
    this.markMessageAsRead();
  }
};
</script>
