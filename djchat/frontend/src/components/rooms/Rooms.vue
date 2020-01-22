<template>
  <div class="rooms">
    <div
      class="relative flex flex-col justify-between border-l bg-white h-screen"
    >
      <!-- Right sidenav -->
      <contact-profile
        :rightSidenav="rightSidenav"
        @toggleRightSidenav="$emit('toggleRightSidenav')"
      />

      <!-- Seccion de mensajes -->
      <messages-section @profile-sidenav="$emit('toggleRightSidenav')">
        <slot />
      </messages-section>

      <!-- Envio de mensaje -->
      <div class="relative">
        <p v-if="whosWriting" class="absolute left-0 text-xs ml-3">
          {{ whosWriting }} is writing...
        </p>
        <send-form class="mt-5 mx-5" />
      </div>

      <!-- Footer Copyright -->
      <div class="text-right mr-5">
        <a style="font-size: 9px;" href="http://www.freepik.com"
          >Background vector created by kjpargeter - www.freepik.com</a
        >
      </div>
    </div>
  </div>
</template>

<script>
import ContactProfile from "@/components/profiles/ContactProfile.vue";
import SendForm from "@/components/SendForm.vue";
import MessagesSection from "@/components/messages/MessagesSection.vue";

export default {
  props: {
    rightSidenav: {
      type: Boolean,
      required: true
    },
    whosWriting: {
      type: String,
      required: true
    }
  },
  components: {
    MessagesSection,
    SendForm,
    ContactProfile
  }
};
</script>
