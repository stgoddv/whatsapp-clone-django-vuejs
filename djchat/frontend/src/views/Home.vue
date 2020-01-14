<template>
  <div class="home overflow-hidden">
    <div
      @click="
        leftSidenav = rightSidenav = false;
        toggleOverlay(false);
      "
      id="overlay"
    ></div>

    <div class="flex flex-wrap py-5 px-12">
      <div class="w-1/3">
        <div
          class="relative border border-r-0 rounded-l-lg bg-white"
          style="height: 90vh;"
        >
          <!-- Left Sidenavs -->
          <div
            class="absolute my-profile-sidenav border"
            :style="
              `height: 100%; width: 100%; 
            background-color: white; z-index:10; 
            transform: translate(-${leftSidenav ? 0 : 150}%);
            transition: transform 0.5s ease-out;`
            "
          >
            <p class="closebtn" @click="toggleLeftSidenav">cross</p>
            hola
          </div>

          <!-- Seccion conversaciones  -->
          <users-section
            class="border-b"
            @profile="toggleLeftSidenav"
            @whosWriting="setWriting($event)"
          />

          <!-- Seccion Invitaciones -->
          <invitations />
        </div>
      </div>

      <div class="w-2/3">
        <div
          class="relative flex flex-col justify-between border rounded-r-lg bg-white"
          style="height: 90vh;"
        >
          <!-- Right Sidenavs -->
          <div
            class="absolute user-profile-sidenav right-0 border"
            :style="
              `height: 100%; width: 25rem; 
            background-color: white; z-index:10; 
            transform: translate(${rightSidenav ? 0 : 150}%);
            transition: transform 0.5s ease-out;`
            "
          >
            <p class="closebtn" @click="toggleRightSidenav">cross</p>
            hola
          </div>

          <!-- Seccion de mensajes -->
          <messages-section @profile-sidenav="toggleRightSidenav" />

          <!-- Envio de mensaje -->
          <div class="relative">
            <p v-if="whosWriting" class="absolute left-0 text-xs">
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

export default {
  components: {
    SendForm,
    MessagesSection,
    UsersSection,
    Invitations
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
  margin-left: 50px;
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
