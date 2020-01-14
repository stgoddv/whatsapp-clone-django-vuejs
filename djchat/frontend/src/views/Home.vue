<template>
  <div class="home">
    <div class="flex flex-wrap py-5 px-12">
      <div class="w-1/3">
        <div
          class="border border-r-0 rounded-l-lg bg-white"
          style="height: 90vh;"
        >
          <!-- Seccion conversaciones  -->
          <users-section class="border-b" @whosWriting="setWriting($event)" />

          <!-- Seccion Invitaciones -->
          <invitations />
        </div>
      </div>

      <div class="w-2/3">
        <div
          class="flex flex-col justify-between border rounded-r-lg bg-white"
          style="height: 90vh;"
        >
          <!-- Seccion de mensajes -->
          <messages-section />

          <!-- Envio de mensaje -->
          <div class="relative">
            <p v-if="whosWriting" class="absolute left-0 text-xs">
              {{ whosWriting }} is writing...
            </p>
            <send-form class="mt-5 mx-5" />
          </div>

          <!-- Footer Copyright -->
          <div class="text-right">
            <a style="font-size: 9px;" href="http://www.freepik.com"
              >Background vector created by kjpargeter - www.freepik.com</a
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SendForm from "@/components/SendForm.vue";
import MessagesSection from "@/components/messages/MessagesSection.vue";
import UsersSection from "@/components/users/UsersSection.vue";
import Invitations from "@/components/invitations/Invitations.vue";

export default {
  components: {
    SendForm,
    MessagesSection,
    UsersSection,
    Invitations
  },
  data() {
    return {
      whosWriting: ""
    };
  },
  computed: {
    selectedRoom() {
      return this.$store.state.selectedRoom;
    }
  },
  watch: {
    selectedRoom() {
      this.whosWriting = "";
    }
  },
  methods: {
    setWriting(data) {
      const { value, room } = data;
      if (this.selectedRoom === room) {
        this.whosWriting = value;
      }
    }
  }
};
</script>
