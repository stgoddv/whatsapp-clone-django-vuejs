<template>
  <div class="send-form flex items-center border rounded-lg border-teal-500">
    <input
      class="ml-3 text-lg appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
      type="text"
      placeholder="Send a message"
      aria-label="Enter text"
      v-model="body"
      ref="inputText"
      @keyup.enter="sendMessage()"
    />
    <button
      class="flex-shrink-0 select-none bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded"
      :class="{
        'cursor-not-allowed bg-teal-700 border-teal-700': !$store.state
          .selectedRoom
      }"
      type="button"
      style="transition: background-color 0.3s;"
      @click.prevent="sendMessage()"
    >
      <send-icon size="1.5x" class="custom-class inline-block"></send-icon>
      <p class="inline-block mx-3 text-lg">Enviar</p>
    </button>
  </div>
</template>

<script>
import uuid4 from "uuid4";

import { SendIcon } from "vue-feather-icons";
import { checkText } from "smile2emoji";

export default {
  data() {
    return {
      body: ""
    };
  },
  components: {
    SendIcon
  },
  methods: {
    sendMessage() {
      if (this.$store.state.selectedRoom) {
        this.body = checkText(this.body);
        let front_key = uuid4();
        let sendingMessage = {
          room: this.$store.state.selectedRoom,
          body: this.body,
          is_owner: true,
          sending: true,
          timestamp: new Date().toString(),
          front_key
        };
        this.$store.commit("LINK_MESSAGES_TO_ROOM", [sendingMessage]);
        this.$store.commit("ADD_MESSAGE_TO_SENDING", sendingMessage);
        this.$store.dispatch("sendMessage", {
          room: this.$store.state.selectedRoom,
          body: this.body,
          front_key
        });
        this.body = "";
        this.$refs["inputText"].focus();
      }
    }
  }
};
</script>
