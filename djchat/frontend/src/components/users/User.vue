<template>
  <div
    class="user-row border-b px-3 py-3 
    cursor-pointer rounded-lg hover:shadow hover:bg-green-200"
    style="transition: box-shadow 0.3s, background-color 0.3s;"
    :class="{ 'bg-green-100':isSelected }"
  >
    <div class="flex items-center">
      <img
        class="w-10 h-10 rounded-full mr-4 mr-5 ml-2"
        src="@/assets/avatars/jonathan.jpg"
        alt="Avatar of Jonathan Reinink"
      >
      <div class="text-sm w-full">
        <div class="flex justify-between">
          <p class="text-gray-900 text-left">{{ room.group_name }}</p>
          <p class="text-gray-600 text-xs text-left">{{ lastActivity }}</p>
        </div>
        <div class="flex justify-between">
          <p
            v-if="lastMessage"
            class="text-gray-600 text-md text-left"
          >{{ lastMessage.body }}</p>
          <p v-else></p>
          <p class="circle mx-1">5</p>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import dateFormat from "dateformat";

export default {
  computed: {
    lastActivity() {
      let last_activity = dateFormat(
        new Date(this.room.last_activity),
        "hh:MM"
      );
      return last_activity;
    },
    lastMessage() {
      const messages = this.room.messages;
      const _lastMessage = messages[messages.length - 1];
      return this.$store.state.messages.find(
        message => message.id === _lastMessage
      );
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
</style>