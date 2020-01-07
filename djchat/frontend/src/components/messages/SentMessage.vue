<template>
  <div class="flex">
    <div class="sent-message ml-auto max-w-md">
      <div class="shadow-md border rounded-lg mx-2 my-1 px-4 bg-green-200">
        <!-- Message body -->
        <div class="mt-1">
          <p class="text-right">{{ message.body }}</p>
        </div>

        <!-- Time data -->
        <div class="flex justify-end mb-1">
          <p class="text-xs text-gray-600">{{ time }}</p>

          <!-- Sending icons -->
          <i
            v-if="message.sending"
            class="material-icons ml-2"
            style="font-size: 16px;"
          >access_time</i>
          <i
            v-if="message.all_received"
            class="material-icons ml-2"
            :class="{ 'font-bold text-teal-400': message.all_read }"
            style="font-size: 16px;"
          >done_all</i>
          <i
            v-if="!message.sending && !message.all_received"
            class="material-icons ml-2"
            style="font-size: 16px;"
          >done</i>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import dateFormat from "dateformat";

export default {
  props: {
    message: {
      type: Object,
      required: true
    }
  },
  computed: {
    time() {
      let time = dateFormat(new Date(this.message.timestamp), "hh:MM");
      return time;
    }
  },
  created() {
    if (this.message.id in this.$store.state.unreadMessages) {
      this.$store.dispatch("markMessageAsRead", this.message.id);
    }
  }
};
</script>
