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
          <clock-icon
            v-if="message.sending"
            size="1x"
            class="ml-2"
          ></clock-icon>
          <check-icon
            v-else
            size="1x"
            class="ml-2"
          ></check-icon>
        </div>
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
