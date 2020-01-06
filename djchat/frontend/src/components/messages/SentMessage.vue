<template>
  <div class="sent-message max-w-lg ml-auto">
    <div class="shadow-md border rounded-lg m-5 px-4 relative bg-green-200">
      <div class="mb-3 mt-2">
        <p class="text-left">{{ message.body }}</p>
      </div>

      <p v-if="message.sending">Enviando</p>

      <div
        class="absolute"
        style="right: 10px; bottom: 5px;"
      >
        <p class="text-xs text-gray-600">{{ time }}</p>
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
  }
};
</script>
