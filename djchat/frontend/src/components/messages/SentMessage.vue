<template>
  <div class="sent-message max-w-lg ml-auto">
    <div class="shadow-md border rounded-lg m-5 px-4 relative bg-green-200">
      <div class="mb-3 mt-2">
        <p class="text-left">{{ message.body }}</p>
      </div>

      <div class="absolute flex" style="right: 10px; bottom: 5px;">
        <p class="text-xs text-gray-600">{{ time }}</p>
        <clock-icon v-if="message.sending" size="1x" class="ml-2"></clock-icon>
        <check-icon v-else size="1x" class="ml-2"></check-icon>
      </div>
    </div>
  </div>
</template>

<script>
import { ClockIcon } from "vue-feather-icons";
import { CheckIcon } from "vue-feather-icons";

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
  components: {
    ClockIcon,
    CheckIcon
  }
};
</script>
