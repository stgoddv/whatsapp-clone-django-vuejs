<template>
  <div class="home overflow-hidden">
    <div
      @click="
        leftSidenav = rightSidenav = false;
        toggleOverlay(false);
      "
      id="overlay"
    ></div>

    <div class="flex flex-wrap">
      <div class="w-1/3">
        <div class="relative bg-white h-screen">
          <!-- Left Sidenavs -->
          <div
            class="absolute my-profile-sidenav bg-gray-200"
            :style="
              `height: 100%; width: 100%; z-index:10; 
            transform: translate(-${leftSidenav ? 0 : 150}%);
            transition: transform 0.5s ease-out;`
            "
          >
            <div class="relative w-full">
              <!-- Close Button -->
              <button
                aria-label="close"
                class="absolute top-0 right-0 text-xl text-white mx-2 closebtn"
                @click.prevent="toggleLeftSidenav"
              >
                ×
              </button>

              <!-- Header -->
              <div class="bg-teal-500" style="height: 10vh;">
                <p class="text-white pt-3 text-left mx-6 text-xl">My Profile</p>
              </div>

              <!-- User Details -->
              <div class="user-details">
                <div class="bg-white shadow py-8">
                  <!-- Avatar -->
                  <div
                    class="avatar-main-circle flex-none mx-auto 
                  select-none cursor-pointer hover:shadow-md"
                    :style="
                      `background-color: rgb(${getColor.red},${getColor.green},${getColor.blue}); 
          transition: box-shadow 0.3s;`
                    "
                  >
                    <!-- {{ room.group_name.charAt(0).toUpperCase() }} -->
                    A
                  </div>

                  <!-- Username -->
                  <div class="text-center mt-3">
                    <p class="text-lg">Admin</p>
                  </div>
                </div>

                <!-- Description -->
                <form class="bg-white shadow py-3 px-6 mt-3">
                  <p class="text-left text-sm text-teal-500">Description</p>
                  <div
                    class="flex items-center border-b border-b-2 border-teal-500 py-2"
                  >
                    <input
                      class="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
                      type="text"
                      placeholder="Add some info."
                      aria-label="Description"
                    />
                    <button
                      class="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded"
                      type="button"
                    >
                      Save
                    </button>
                  </div>
                </form>
              </div>
            </div>
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
          class="relative flex flex-col justify-between border-l bg-white h-screen"
        >
          <!-- Right Sidenavs -->
          <div
            class="absolute user-profile-sidenav right-0 bg-gray-200"
            :style="
              `height: 100%; width: 25rem; z-index:10; 
            transform: translate(${rightSidenav ? 0 : 150}%);
            transition: transform 0.5s ease-out;`
            "
          >
            <div class="relative w-full">
              <!-- Close Button -->
              <button
                aria-label="close"
                class="absolute top-0 left-0 text-xl text-white mx-2 closebtn"
                @click.prevent="toggleRightSidenav"
              >
                ×
              </button>

              <!-- Header -->
              <div class="bg-teal-500" style="height: 10vh;">
                <p class="text-white pt-3 text-center text-xl">
                  Contact Details
                </p>
              </div>

              <!-- User Details -->
              <div class="user-details">
                <div class="bg-white shadow py-8">
                  <!-- Avatar -->
                  <div
                    class="avatar-main-circle flex-none mx-auto 
                  select-none cursor-pointer hover:shadow-md"
                    :style="
                      `background-color: rgb(${getColor.red},${getColor.green},${getColor.blue}); 
          transition: box-shadow 0.3s;`
                    "
                  >
                    <!-- {{ room.group_name.charAt(0).toUpperCase() }} -->
                    A
                  </div>

                  <!-- Username -->
                  <div class="text-center mt-3">
                    <p class="text-lg">Admin</p>
                  </div>
                </div>

                <!-- Description -->
                <form class="bg-white shadow py-3 px-6 mt-3">
                  <p class="text-left text-sm text-teal-500">Description</p>
                  <div
                    class="flex items-center border-b border-b-2 border-teal-500 py-2"
                  >
                    <input
                      class="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
                      type="text"
                      placeholder="Add some info."
                      aria-label="Description"
                    />
                    <button
                      class="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded"
                      type="button"
                    >
                      Save
                    </button>
                  </div>
                </form>
              </div>
            </div>
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

import { colorOffsets, getHash } from "@/global/variables.js";

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
