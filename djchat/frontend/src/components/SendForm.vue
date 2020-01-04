<template>
  <div class="send-form flex items-center border rounded-lg border-teal-500">
    <input
      class="ml-3 text-lg appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
      type="text"
      placeholder="Send a message"
      aria-label="Enter text"
    >
    <button
      class="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded"
      type="button"
      style="transition: background-color 0.3s;"
    >
      <send-icon
        size="1.5x"
        class="custom-class inline-block"
      ></send-icon>
      <p class="inline-block mx-3 text-lg">Enviar</p>
    </button>
  </div>
</template>

<script>
import { SendIcon } from "vue-feather-icons";

export default {
  components: {
    SendIcon
  }
};
</script>