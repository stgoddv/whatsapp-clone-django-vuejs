<template>
  <div class="home overflow-hidden">
    <div
      @click="
        leftSidenav = rightSidenav = false;
        toggleOverlay(false);
      "
      id="overlay"
    ></div>

    <invitation-modal ref="invitation-modal" />

    <div class="flex flex-wrap">
      <div class="w-1/3">
        <div class="relative bg-white h-screen">
          <!-- Left sidenav -->
          <user-profile
            :leftSidenav="leftSidenav"
            @toggleLeftSidenav="toggleLeftSidenav"
          />

          <!-- Seccion conversaciones  -->
          <users-section
            class="border-b"
            @profile="toggleLeftSidenav"
            @whosWriting="setWriting($event)"
            @invite-action="openInvitationModal"
          />

          <!-- Seccion Invitaciones -->
          <invitations @invite-action="openInvitationModal" />
        </div>
      </div>

      <div class="w-2/3">
        <div
          class="relative flex flex-col justify-between border-l bg-white h-screen"
        >
          <!-- Right sidenav -->
          <contact-profile
            :rightSidenav="rightSidenav"
            @toggleRightSidenav="toggleRightSidenav"
          />

          <!-- Seccion de mensajes -->
          <messages-section @profile-sidenav="toggleRightSidenav" />

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
    </div>
  </div>
</template>

<script>
import SendForm from "@/components/SendForm.vue";
import MessagesSection from "@/components/messages/MessagesSection.vue";
import UsersSection from "@/components/users/UsersSection.vue";
import Invitations from "@/components/invitations/Invitations.vue";
import InvitationModal from "@/components/invitations/InvitationModal.vue";
import ContactProfile from "@/components/profiles/ContactProfile.vue";
import UserProfile from "@/components/profiles/UserProfile.vue";

import { colorOffsets, getHash } from "@/global/variables.js";

export default {
  components: {
    SendForm,
    MessagesSection,
    UsersSection,
    Invitations,
    InvitationModal,
    ContactProfile,
    UserProfile
  },
  data() {
    return {
      whosWriting: "",
      leftSidenav: false,
      rightSidenav: false
    };
  },
  computed: {
    selectedRoom() {
      return this.$store.state.selectedRoom;
    },
    getColor() {
      // let username = this.room.group_name;
      let username = "A";
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
  watch: {
    selectedRoom() {
      this.whosWriting = "";
    }
  },
  methods: {
    openInvitationModal() {
      this.$refs["invitation-modal"].open();
    },
    setWriting(data) {
      const { value, room } = data;
      if (this.selectedRoom === room) {
        this.whosWriting = value;
      }
    },
    toggleOverlay(show) {
      if (show) {
        document.getElementById("overlay").style.display = "block";
      } else {
        document.getElementById("overlay").style.display = "none";
      }
    },
    toggleLeftSidenav() {
      this.leftSidenav = !this.leftSidenav;
      this.toggleOverlay(this.leftSidenav);
    },
    toggleRightSidenav() {
      this.rightSidenav = !this.rightSidenav;
      this.toggleOverlay(this.rightSidenav);
    }
  }
};
</script>

<style scoped>
.closebtn {
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
  margin-left: 30px;
}

.avatar-main-circle {
  width: 180px;
  height: 180px;
  border-radius: 50%;
  font-size: 130px;
  color: #fff;
  line-height: 180px;
  text-align: center;
  font-weight: 600;
}

#overlay {
  position: fixed; /* Sit on top of the page content */
  display: none; /* Hidden by default */
  width: 100%; /* Full width (cover the whole page) */
  height: 100%; /* Full height (cover the whole page) */
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5); /* Black background with opacity */
  z-index: 2; /* Specify a stack order in case you're using a different order for other elements */
}
</style>
